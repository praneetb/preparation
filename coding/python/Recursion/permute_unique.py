# permutation of a string

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
  permute('', s)

if __name__ == '__main__':
  main()



