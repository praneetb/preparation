#
# Queue implementation
#


class Queue:
    def __init__(self):
        self.elements = []

    def queue(self, elem):
        self.elements.append(elem)

    def dequeue(self):
        return self.elements.remove(self.elements[0])

    def is_empty(self):
        return True if len(self.elements) == 0 else False

    def sprint(self):
        print self.elements

def main():
  st = Queue()
  st.queue(4)
  st.sprint()
  st.queue(7)
  st.sprint()
  st.queue(3)
  st.sprint()
  st.queue(0)
  st.sprint()
  st.dequeue()
  st.sprint()
  st.dequeue()
  st.sprint()
  st.dequeue()
  st.sprint()

if __name__ == '__main__':
  main()
