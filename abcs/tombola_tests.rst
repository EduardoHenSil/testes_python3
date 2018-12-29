==================
Testes de Tombola
=================
Toda subclasse concreta de Tombola deve passar nesses testes

Cria e carrega instância a partir de um iterável::
    >>> balls = list(range(3))
    >>> globe = ConcreteTombola(balls)
    >>> globe.loaded()
    True
    >>> globe.inspect()
    (0, 1, 2)

Escolhe e reúne as bolas::
    >>> picks = []
    >>> picks.append(globe.pick())
    >>> picks.append(globe.pick())
    >>> picks.append(globe.pick())

Verifica estado e resultados::
    >>> globe.loaded()
    False
    >>> sorted(picks) == balls
    True

Recarrega::
    >>> globe.load(balls)
    >>> globe.loaded()
    True
    >>> picks = [globe.pick() for i in balls]
    >>> globe.loaded()
    False

Verifica de 'LookupError' (ou uma subclasse) é a exceção
lançada quando o dispositivo está vazio::
    >>> globe = ConcreteTombola([])
    >>> try:
    ...     globe.pick()
    ... except LookupError as exc:
    ...     print('OK')
    OK
