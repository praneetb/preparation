#
# Given an input string, reverse the string word by word.
# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing
# spaces and the words are always separated by a single space.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#


def main():
  sentence = raw_input('Enter sentence:')
  word_list = sentence.split(' ')[::-1]
  rsentence = ' '.join(word_list)
  print "Reversed sentence is %s" % (rsentence)

if __name__ == '__main__':
    main()
