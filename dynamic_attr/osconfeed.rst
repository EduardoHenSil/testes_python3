# doctests para osconfeed.load
>>> from osconfeed import load
>>> feed = load()
>>> sorted(feed['Schedule'].keys())
['conferences', 'events', 'speakers', 'venues']
>>> for key, value in sorted(feed['Schedule'].items()):
...     print('{:3} {}'.format(len(value), key))
...
  1 conferences
494 events
357 speakers
 53 venues
>>> feed['Schedule']['speakers'][-1]['name']
'Carina C. Zona'
>>> feed['Schedule']['speakers'][-1]['serial']
141590
>>> feed['Schedule']['events'][40]['name']
'There *Will* Be Bugs'
>>> feed['Schedule']['events'][40]['speakers']
[3471, 5199]
