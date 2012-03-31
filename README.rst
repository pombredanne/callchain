*callchain* strings arbitrary callables, components, and event listeners into
one lazily evaluated processing chain. 

Some highly contrived examples:

`chain <https://en.wikipedia.org/wiki/Fluent_interface>`_ style:

>>> from callchain import aachainq as chainq
>>> chainqueue = chainq()
>>> chainqueue(('a', 1), ('b', 2), ('c', 3)).reup().wrap(dict).map().value()
{'a': 1, 'b': 2, 'c': 3}

Object-oriented style:

>>> chainqueue(('a', 1), ('b', 2), ('c', 3))
>>> chainqueue.reup()
>>> chainqueue.wrap(dict)
>>> chainqueue.map()
>>> chainqueue.value()
{'a': 1, 'b': 2, 'c': 3}

Mirrored at https://github.com/kwarterthieves/callchain/