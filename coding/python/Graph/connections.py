#
# Connection between two nodes
#

from graph import Graph

connections = [
             ('A', 'B'),
             ('A', 'B'),
             ('A', 'C'),
             ('A', 'D'),
             ('B', 'A'),
             ('C', 'E'),
             ('C', 'F'),
             ('D', 'B'),
             ('D', 'F'),
             ('E', 'A'),
             ('E', 'F'),
             ]


def main():
  print connections
  g = Graph(connections, False)

  print g.is_connected('A', 'B')
  print g.is_connected('A', 'E')
  print g.get_adjacent('A')

if __name__ == '__main__':
  main()
