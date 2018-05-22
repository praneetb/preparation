# Stacked Canonballs
# example:
#  one canonball stacked on 4 stacked on 9 over a square. height is 3
# Write code to take height and return number of canonballs.

def get_cannonballs(height):
  if height <= 0:
    return height
  return height*height + get_cannonballs(height-1)

def main():
  height = input("Enter height :")
  num_cb = get_cannonballs(height)
  print("Number of Cannonballs = %d" %(num_cb))

if __name__ == '__main__':
  main()
