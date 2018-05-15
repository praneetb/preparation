#
# Stack implementation
#


class Stack:
    def __init__(self):
        self.elements = []

    def push(self, elem):
        self.elements.append(elem)

    def pop(self):
        val = self.elements[-1]
        self.elements.remove(val)
        return val

    def peek(self):
        return self.elements[-1]

    def is_empty(self):
        return True if len(self.elements) == 0 else False

    def sprint(self):
        print self.elements

def main():
  st = Stack()
  st.push(4)
  st.sprint()
  st.push(7)
  st.sprint()
  st.push(3)
  st.sprint()
  st.push(0)
  st.sprint()
  st.pop()
  st.sprint()
  st.pop()
  st.sprint()
  st.pop()
  st.sprint()

if __name__ == '__main__':
  main()
