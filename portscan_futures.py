#!/usr/bin/python3
# coding: utf-8

import socket
import sys
import time
from collections import namedtuple 
from concurrent import futures

Status = namedtuple('Status', 'ip port msg')

def getsocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    return s

def closesocket(socket):
    socket.close()

def check_port(ip, port):
    sock = getsocket()
    try:
        sock.connect((ip, port))

    except ConnectionRefusedError:
        return Status(ip, port, "Porta Fechada!")

    except socket.timeout:
        return Status(ip, port, "Host Inalcansável!")

    except Exception as e:
        return Status(ip, port, type(e))

    else:
        return Status(ip, port, "Porta Aberta!")

    finally:
        closesocket(sock)

def main(ip, show_only_opened=False):
    future_list = []
    executor = futures.ThreadPoolExecutor(max_workers=10)
    t0 = time.time()
    for port in range(100):
        future = executor.submit(check_port, ip, port)
        future_list.append(future)
    for future in futures.as_completed(future_list):
        status = future.result()
        if show_only_opened and status.msg != "Porta Aberta!":
            continue
        print("{} ==> {}".format(status.port, status.msg))
    elapsed = time.time() - t0
    print("Execução em {:.2f}s".format(elapsed))

if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Exemplo: {} {}".format(sys.argv[0], '192.168.0.1'))
        exit()

    soo = False

    if len(sys.argv) == 3 and sys.argv[2] == 'nv':
        soo = True

    main(sys.argv[1], soo)
