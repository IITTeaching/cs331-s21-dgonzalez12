import urllib.request
import unittest
from typing import TypeVar, Callable, List

T = TypeVar('T')
S = TypeVar('S')

#################################################################################
# EXERCISE 1
#################################################################################
def mysort(lst: List[T], compare: Callable[[T, T], int]) -> List[T]:
    """
    This method should sort input list lst of elements of some type T.

    Elements of the list are compared using function compare that takes two
    elements of type T as input and returns -1 if the left is smaller than the
    right element, 1 if the left is larger than the right, and 0 if the two
    elements are equal.
    """
    for i in range(1, len(lst)): #loops through each element starting at the second one
        for j in range(i, 0, -1): #loops through each element coming before i starting at i and going backwards
            if compare(lst[j], lst[j-1]) < 0: #checks to see if the previous element is smaller than the current (by saying <0 we keep the sort stable as well)
                lst[j], lst[j-1] = lst[j-1], lst[j] #if they are, we switch them
            else:
                break #if they are not, we know that the element is in its proper place
    return lst

def mybinsearch(lst: List[T], elem: S, compare: Callable[[T, S], int]) -> int:
    """
    This method search for elem in lst using binary search.

    The elements of lst are compared using function compare. Returns the
    position of the first (leftmost) match for elem in lst. If elem does not
    exist in lst, then return -1.
    
    
    OLD CODE:
    lower = 0
    upper = len(lst)-1
    mid = 0
    while lower <= upper:
        mid = int((lower + upper) / 2)
        if compare(lst[mid], elem) > 0: #meaning that elem is in the lower half
            upper = mid - 1 #makes new upper bound right below mid
        elif compare(lst[mid], elem) < 0: #meaning that elem is in the upper half
            lower = mid + 1 #makes lower bound right above mid
        else:
            return mid
    return -1 #if the while loop runs and doesn't catch then we return -1
    """

    lower = 0
    upper = len(lst)-1
    mid = 0
    while lower <= upper:
        mid = int((lower + upper) / 2)
        if compare(lst[mid], elem) > 0: #meaning that elem is in the lower half
            upper = mid - 1 #makes new upper bound right below mid
        elif compare(lst[mid], elem) < 0: #meaning that elem is in the upper half
            lower = mid + 1 #makes lower bound right above mid
        else:
            while(not(mid == 0) and compare(lst[mid-1], elem) == 0):
                mid-= 1
            return mid
    return -1 #if the while loop runs and doesn't catch then we return -1

class Student():
    """Custom class to test generic sorting and searching."""
    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.name == other.name

# 30 Points (total)
def test1():
    """Tests for generic sorting and binary search."""
    print(80 * "#" + "\nTests for generic sorting and binary search.")
    test1_1()
    test1_2()
    test1_3()
    test1_4()
    test1_5()

# 6 Points
def test1_1():
    """Sort ints."""
    print("\t-sort ints")
    tc = unittest.TestCase()
    ints = [ 4, 3, 7, 10, 9, 2 ]
    intcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
    sortedints = mysort(ints, intcmp)
    tc.assertEqual(sortedints, [2, 3, 4, 7, 9, 10])

# 6 Points
def test1_2():
    """Sort strings based on their last character."""
    print("\t-sort strings on their last character")
    tc = unittest.TestCase()
    strs = [ 'abcd', 'aacz',  'zasa' ]
    suffixcmp = lambda x,y: 0 if x[-1] == y[-1] else (-1 if x[-1] < y[-1] else 1)
    sortedstrs = mysort(strs,suffixcmp)
    tc.assertEqual(sortedstrs, [ 'zasa', 'abcd', 'aacz' ])

# 6 Points
def test1_3():
    """Sort students based on their GPA."""
    print("\t-sort students on their GPA.")
    tc = unittest.TestCase()
    students = [ Student('Josh', 3.0), Student('Angela', 2.5), Student('Vinesh', 3.8),  Student('Jia',  3.5) ]
    sortedstudents = mysort(students, lambda x,y: 0 if x.gpa == y.gpa else (-1 if x.gpa < y.gpa else 1))
    expected = [ Student('Angela', 2.5), Student('Josh', 3.0), Student('Jia',  3.5), Student('Vinesh', 3.8) ]
    tc.assertEqual(sortedstudents, expected)

# 6 Points
def test1_4():
    """Binary search for ints."""
    print("\t-binsearch ints")
    tc = unittest.TestCase()
    ints = [ 4, 3, 7, 10, 9, 2 ]
    intcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
    sortedints = mysort(ints, intcmp)
    tc.assertEqual(mybinsearch(sortedints, 3, intcmp), 1)
    tc.assertEqual(mybinsearch(sortedints, 10, intcmp), 5)
    tc.assertEqual(mybinsearch(sortedints, 11, intcmp), -1)

# 6 Points
def test1_5():
    """Binary search for students by gpa."""
    print("\t-binsearch students")
    tc = unittest.TestCase()
    students = [ Student('Josh', 3.0), Student('Angela', 2.5), Student('Vinesh', 3.8),  Student('Jia',  3.5) ]
    stcmp = lambda x,y: 0 if x.gpa == y.gpa else (-1 if x.gpa < y.gpa else 1)
    stbincmp = lambda x,y: 0 if x.gpa == y else (-1 if x.gpa < y else 1)
    sortedstudents = mysort(students, stcmp)
    tc.assertEqual(mybinsearch(sortedstudents, 3.5, stbincmp), 2)
    tc.assertEqual(mybinsearch(sortedstudents, 3.7, stbincmp), -1)

#################################################################################
# EXERCISE 2
#################################################################################
class PrefixSearcher():

    def __init__(self, document, k):
        """
        Initializes a prefix searcher using a document and a maximum
        search string length k.
        """
        doc = document
        self.n = k
        lst = []
        for l in range(1, self.n+1): #loops through every substring up to n
            for i in range(0, len(doc)-l): #loops through each index up to the length - l because that's where we need to start chopping up
                lst.append(doc[i:i+l]) #adds it to the list
            for i in range(len(doc)-l, len(doc)): #loops through the last indices that need to be chopped
                lst.append(doc[i:]) #adds them to the list as well
        self.ststr = lambda x, y: 0 if x == y else (-1 if x < y else 1) #creates the compare function
        self.sortedList = mysort(lst, self.ststr) #sorts the list and stores it
        '''
        for i in range(0, len(doc) - k):
            lst.append(doc[i:i + k])
        for i in range(len(doc) - k, len(doc)):
            lst.append(doc[i:])
        '''
    def search(self, q):
        """
        Return true if the document contains search string q (of

        length up to n). If q is longer than n, then raise an
        Exception.
        """
        if len(q) > self.n: #checks to see if the length of q is larger than n
            raise Exception("q cannot be larger than n") #raises an exception if it is
        return mybinsearch(self.sortedList, q, self.ststr) >= 0 # returns True if q is found in the list and False if it's not
# 30 Points
def test2():
    print("#" * 80 + "\nSearch for substrings up to length n")
    test2_1()
    test2_2()

# 15Points
def test2_1():
    print("\t-search in hello world")
    tc = unittest.TestCase()
    p = PrefixSearcher("Hello World!", 1)
    tc.assertTrue(p.search("l"))
    tc.assertTrue(p.search("e"))
    tc.assertFalse(p.search("h"))
    tc.assertFalse(p.search("Z"))
    tc.assertFalse(p.search("Y"))
    p = PrefixSearcher("Hello World!", 2)
    tc.assertTrue(p.search("l"))
    tc.assertTrue(p.search("ll"))
    tc.assertFalse(p.search("lW"))

# 20 Points
def test2_2():
    print("\t-search in Moby Dick")
    tc = unittest.TestCase()
    md_url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
    md_text = urllib.request.urlopen(md_url).read().decode()
    p = PrefixSearcher(md_text[0:1000],4)
    tc.assertTrue(p.search("Moby"))
    tc.assertTrue(p.search("Dick"))

#################################################################################
# EXERCISE 3
#################################################################################
class SuffixArray():

    def __init__(self, document: str):
        """
        Creates a suffix array for document (a string).
        """
        #makes a list of len(doc)
        self.doc = document
        self.ststr = lambda x, y: 0 if x == y else (-1 if x < y else 1)  # creates the compare function
        self.stlst = lambda x, y: 0 if x[1] == y[1] else (-1 if x[1] < y[1] else 1)  # creates the compare function
        self.comp = lambda x, y: 0 if self.doc[x:x + len(y)] == y else (
            -1 if self.doc[x:x + len(y)] < y else 1)
        self.sarray = []
        for i in range(0, len(self.doc)): #goes through each index in the doc
            temp = [] #makes a temp list
            temp.append(i) #adds index to list
            temp.append(self.doc[i:]) #adds suffix at index to temp
            self.sarray.append(temp) #adds temp to sarray
        self.sarray = mysort(self.sarray, self.stlst) #sorts array
        for i in range(0, len(self.sarray)):
            self.sarray[i] = (self.sarray[i])[0]
        '''
        print(self.sarray)
        print(f"The length of the suffix array is {len(self.sarray)}")
        print(f"The last element of suffix array is {self.sarray.index(0, 0, len(self.sarray))}")
        print(f"First 8 letters of doc at index 34 are {self.doc[34:43]}")
            
        self.doc = document
        self.ststr = lambda x, y: 0 if x == y else (-1 if x < y else 1)  # creates the compare function
        self.stlst = lambda x, y: 0 if x[1] == y[1] else (-1 if x[1] < y[1] else 1)  # creates the compare function
        self.sarray = []
        for i in range(0, len(self.doc)-1): #goes through each index in list
            temp = [str(i)] #creates a temp to append later
            for k in range(i+1, len(self.doc)): #goes through each index following current i index
                temp.append(self.doc[i:k]) #adds substrings to temp
            self.sarray.append(temp)
        self.sarray = mysort(self.sarray, self.stlst)'''
    '''
    def comp(self, ind, el):
        length = len(el)
        if ind > (len(self.doc) - len(el)):
            length = len(self.doc[ind:])
        if self.doc[ind:ind+length] == el[:length]:
            return 0
        elif self.doc[ind:length] < el[:length]:
            return -1
        else:
            return 1
    '''


    def positions(self, searchstr: str):
        """
        Returns all the positions of searchstr in the documented indexed by the suffix array.
        """
        indices = []
        index = mybinsearch(self.sarray, searchstr, self.comp)
        if index >= 0:
            indices.append(index)
        return indices


    def contains(self, searchstr: str):
        """
        Returns true of searchstr is contained in document.

        self.stList = lambda x, y: 0 if x[len(y)] == y else (-1 if x[len(y)] < y else 1)  # list must come second
        def stList(x, y):
            if len(y) > len(x):
                return -1
            if x[len(y)] == y:
                return 0

        search = mybinsearch(self.sarray, searchstr, self.stList)
        if(search < 0):
            return False
        return True
        """
        index = mybinsearch(self.sarray, searchstr, self.comp)
        if index < 0:
            return False
        return True

# 40 Points
def test3():
    """Test suffix arrays."""
    print(80 * "#" + "\nTest suffix arrays.")
    test3_1()
    test3_2()


# 20 Points
def test3_1():
    print("\t-suffixarray on Hello World!")
    tc = unittest.TestCase()
    s = SuffixArray("Hello World!")
    tc.assertTrue(s.contains("l"))
    tc.assertTrue(s.contains("e"))
    tc.assertFalse(s.contains("h"))
    tc.assertFalse(s.contains("Z"))
    tc.assertFalse(s.contains("Y"))
    tc.assertTrue(s.contains("ello Wo"))


# 20 Points
def test3_2():
    print("\t-suffixarray on Moby Dick!")
    tc = unittest.TestCase()
    md_url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
    md_text = urllib.request.urlopen(md_url).read().decode()
    s = SuffixArray(md_text[0:1000])
    tc.assertTrue(s.contains("Moby Dick"))
    tc.assertTrue(s.contains("Herman Melville"))
    tc.assertEqual(s.positions("Moby Dick"), [427])


#################################################################################
# TEST CASES
#################################################################################
def main():
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()
