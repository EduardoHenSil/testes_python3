#!/usr/bin/python3
# coding: utf-8

import sys
import queue
import random
from collections import namedtuple

DEPARTURE_INTERVAL = 5
Event = namedtuple('Event', 'time proc action')

def taxi_process(ident, trips, start_time=0):
    """Cede o controle ao simulador gerando um evento a cada mudança de estado"""
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')
    yield Event(time, ident, 'going home')


def compute_duration(event):
    return random.randint(1, 50)

class Simulator:

    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        """Agenda e exibe eventos até o tempo acabar"""
        # agenda o primeiro evento para cada taxi
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)
        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id * ' ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))

if __name__ == '__main__':
    num_taxis = sys.argv[1] if len(sys.argv) > 1 else 3
    taxis = {i: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL) for i in range(num_taxis)}

    sim = Simulator(taxis)
    sim.run(160)
