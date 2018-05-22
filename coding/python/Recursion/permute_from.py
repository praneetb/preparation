# permutation of a string from a position

def permute(prefix, s):
  if len(s) == 0:
    print prefix
    return
 
  for i in range(len(s)):
    nprefix = prefix + s[i]
    ns = s[0:i] + s[i+1:]
    permute(nprefix, ns)

def main():
  s = raw_input("Enter string :")
  n = input("Enter position :")
  permute(s[0:n], s[n:])

if __name__ == '__main__':
  main()



