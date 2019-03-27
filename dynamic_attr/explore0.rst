# doctests para osconfeed.load utilizando FrozenJson

>>> from explore0 import FrozenJSON
>>> from osconfeed import load
>>> raw_feed = load()
>>> feed = FrozenJSON(raw_feed)
>>> len(feed.Schedule.speakers)
357
>>> sorted(feed.Schedule.keys())
['conferences', 'events', 'speakers', 'venues']
>>> for key, value in sorted(feed.Schedule.items()):
...     print('{:3} {}'.format(len(value), key))
...
  1 conferences
494 events
357 speakers
 53 venues
>>> feed.Schedule.speakers[-1].name
'Carina C. Zona'
>>> talk = feed.Schedule.events[40]
>>> type(talk)
<class 'explore0.FrozenJSON'>
>>> talk.name
'There *Will* Be Bugs'
>>> talk.speakers
[3471, 5199]
