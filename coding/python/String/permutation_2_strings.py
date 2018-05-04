# How to determine if two strings are permutations
# of each other

def check_permutation1(str1, str2):
  str1 = sorted(str1)
  str2 = sorted(str2)
  if str1 == str2:
    return "True"
  return "False"

def check_permutation2(str1, str2):
  l1 = [0]*256
  l2 = [0]*256

  for i in range(len(str1)):
    l1[ord(str1[i])] += 1

  for i in range(len(str2)):
    l1[ord(str2[i])] -= 1

  if l1 == l2:
    return "True"

  return "False"

def main():
  print "How to determine if two strings are permutations of each other"

  str1 = raw_input("Enter string 1:")
  str2 = raw_input("Enter string 2:")
  res = check_permutation1(str1, str2)
  print "String %s and %s are permutation of each other: %s" %(str1, str2, res)
  res = check_permutation2(str1, str2)
  print "String %s and %s are permutation of each other: %s" %(str1, str2, res)

if __name__ == '__main__':
  main()

