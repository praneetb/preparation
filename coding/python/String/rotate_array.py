#
# Rotate Array by a given numer
# Example:
#  with n = 7 and k = 3, the array [1,2,3,4,5,6,7]
#  is rotated to [5,6,7,1,2,3,4].
#

def reverse(arr, i, j):
  while i < j:
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    i += 1
    j -= 1

def rotate_by(arr, r):
  alen = len(arr)
  reverse(arr, 0, alen-r-1)
  reverse(arr, alen-r, alen-1)
  reverse(arr, 0, alen-1)

def main():
  arr = [1,2,3,4,5,6,7,8,9]
  rotate_by(arr, 4)
  print arr

if __name__ == '__main__':
  main()

