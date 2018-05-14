#
# ['geeksforgeeks', 'geeks', 'geek', 'geezer']
# "gee"
#

def min(l1, l2):
  if l1 < l2:
    return l1
  return l2

def get_cmn_pfx(str1, str2):
  cmn = []
  l = min(len(str1), len(str2))
  i = 0
  while (i<l):
    if str1[i] == str2[i]:
      cmn.append(str1[i])
      i+=1
    else:
      break

  return "".join(cmn)
    

def get_longest_prefix(sdict):
  pfx = sdict[0]
  for i in range(1, len(sdict)):
    pfx = get_cmn_pfx(pfx, sdict[i])
  return pfx

def main():
  str_dict = ['geksforgeeks', 'geeks', 'geek', 'geezer']
  cmn_pfx = get_longest_prefix(str_dict)
  print "Common Prefix is : " + cmn_pfx

if __name__ == '__main__':
  main()
