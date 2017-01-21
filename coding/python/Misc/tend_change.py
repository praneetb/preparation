#
# Write a Python program that can make change. Your program should take
# two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any
# current or former government. Try to design your program so that it
# returns as few bills and coins as possible.
#


class TendChange():
    def __init__(self, charged, given):
        self.charged = int(charged*100)
        self.given = int(given*100)
        self.den = (1, 5, 10, 25, 100, 500, 1000, 2000)
        self.den_names = ('penny', 'nickle', 'dime', 'quarter', '1$', 'five$', 'ten$', 'twenty$')
        self.den_back = [0, 0, 0, 0, 0, 0, 0, 0]

    def process_transaction(self):
        import pdb; pdb.set_trace()
        change_back = self.given - self.charged
        index = len(self.den)-1
        while change_back > 0:
            while change_back >= self.den[index]:
                change_back -= self.den[index]
                self.den_back[index] += 1
            index -= 1
        return

    def print_return_denominations(self):
        for idx in range(len(self.den_back)):
            if self.den_back[idx]:
                print 'returned %s %s' %(self.den_back[idx], self.den_names[idx])

def main():
    charged = input('Item Price:')
    given = input('Customer Amount Given:')
    while given < charged:
        given = input('Need More! Customer Amount Given:')

    change = TendChange(charged, given)
    change.process_transaction()
    change.print_return_denominations()

if __name__ == '__main__':
    main()
