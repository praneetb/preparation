# List Unique Characters
#

def unique_chars(string):
  l = [""]*256
  for i in range(len(string)):
    l[ord(string[i])] = string[i]
  return "".join(l)

def main():
  string = raw_input("enter string:")
  print("Unique charcaters: " + unique_chars(string))

if __name__ == '__main__':
  main()
