#
# Graph library
#

from collections import defaultdict

class Graph:

  def __init__(self, connections, directed):
    self._graph = defaultdict(set)
    self._directed = directed
    self._add_connections(connections)

  def _add_connections(self, connections):
    for n1, n2 in connections:
      self.add(n1, n2)

  def add(self, n1, n2):
    self._graph[n1].add(n2)
    if not self._directed:
       self._graph[n2].add(n1)

  def remove(self, n):
    for i, ns in self._graph.iteritems():
      try:
        ns.remove(n)
      except KeyError:
        pass

  def get_adjacent(self, n):
    return self._graph[n]

  def is_connected(self, n1, n2):
    return n1 in self._graph and n2 in self._graph[n1]
    


