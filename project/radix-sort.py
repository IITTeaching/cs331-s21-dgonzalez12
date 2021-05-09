import urllib
import requests
from unittest import TestCase

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
   booktxt = urllib.request.urlopen(book_url).read().decode()
   bookascii = booktxt.encode('ascii','replace')
   return bookascii.split()

def maxi(array):
   mx = len(array[0])
   for x in array:
      if len(x) > mx:
         mx = len(x)
   return mx

def radix_a_book(bookurl='https://www.gutenberg.org/files/84/84-0.txt'):
   ans = book_to_words(bookurl) #the list of words
   mx = maxi(ans) #the longest word length
   tomp = [0] * len(ans) #temp to be used in for loop
   for x in range(mx, -1, -1): #loops through length of mx
      counts = [0] * 129  # counts to be used in for loop
      for word in range(0, len(ans)): #loops through each word in ans
         try: #makes temp variable the ascii value for the letter + 1
            temp = ans[word][x] + 1
         except IndexError: #or if there is no letter, makes it 0
            temp = 0
         counts[temp] += 1 #increments the count of the temp
      for i in range(1, 128):
         counts[i] += counts[i - 1] #adds the value of the previous index of count to each index after 0
      for y in range(len(ans) - 1, -1, -1): #goes backwards through ans
         try: #if there is a character at y, gets the count of the value plus 1 (see line 24) and puts it where
               #it's supposed to go
            tomp[counts[ans[y][x] + 1] - 1] = ans[y]
            counts[ans[y][x] + 1] += -1 #decrements counts at that spot
         except IndexError: #does the same thing, except only if there is no character there
            tomp[counts[0] - 1] = ans[y]
            counts[0] += -1
      ans = tomp #makes ans the new version
      tomp = [0] * len(ans) #sets tomp back to all 0 and starts again
   return ans #let's go


def main():
   lst = book_to_words()
   lst.sort()
   wonk = radix_a_book()
   #print(wonk)
   ozy = radix_a_book('https://raw.githubusercontent.com/jordandm/numenta/master/poems/ozymandias.txt')
   yer = book_to_words('https://raw.githubusercontent.com/jordandm/numenta/master/poems/ozymandias.txt')
   yer.sort()
   tc = TestCase()
   tc.assertEqual(lst, wonk)
   print("Let's go")
   tc.assertEqual(yer, ozy)
   print("nice")

if __name__ == '__main__':
   main()
   pass

'''
def countstring(array):
   counts = [0]*128
   fin = [0] * len(array)
   for x in array:
      counts[x] += 1
   for i in range(1,128):
      counts[i] += counts[i-1]
   for y in range(len(array)-1, -1, -1):
      fin[counts[array[y]] - 1] = array[y]

   return fin
'''
