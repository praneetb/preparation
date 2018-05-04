# Given a string, Determine if the string has all
# unique characters.

# MAX_ASCII_CHARS = 256


def check_unique1(string):
  str_arr = [None]*256
  for i in range(len(string)):
    if str_arr[ord(string[i])]:
      return "False"
    str_arr[ord(string[i])] = 1
  return "True"

def check_unique2(string):
  for i in range(len(string)):
    for j in range(i+1, len(string)):
      if string[i] == string[j]:
        return "False"
  return "True"

def check_unique3(string):
  string = sorted(string)
  for i in range(len(string)-1):
    if string[i] == string[i+1]:
      return "False"
  return "True"
  


def main():
  print "Given a string, Determine if the string has all unique characters."
  string = raw_input("Enter String: ")
  print("String is : " + check_unique1(string))
  print("String is : " + check_unique2(string))
  print("String is : " + check_unique3(string))

if __name__ == '__main__':
  main()
