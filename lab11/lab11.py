from unittest import TestCase
import random

def quicksort(lst,pivot_fn):
    qsort(lst,0,len(lst) - 1,pivot_fn)

def qsort(lst,low,high,pivot_fn):
    ### BEGIN SOLUTION
    if low < high:
        ind = partition(lst, low, high, pivot_fn)
        qsort(lst, low, ind - 1, pivot_fn)
        qsort(lst, ind + 1, high, pivot_fn)
    ### END SOLUTION

def partition(lst, low, high, pivot_fn):
    pivot = pivot_fn(lst, low, high)
    print(lst)
    print(f"Pivot: {pivot}")
    i = low
    j = high
    while i < j:
        while lst[i] <= pivot and i < len(lst):
            print(i)
            i += 1
            if i >= len(lst):
                break
        print(f"I: {i}")
        while lst[j] > pivot and j >= 0:
            j += -1
            print(f"J1: {j}")
        print(f"J1: {j}")
        #if i >= j:
        #    break
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
        else:
            print(f"End j: {j}")
            return j

def pivot_first(lst,low,high):
    ### BEGIN SOLUTION
    return lst[low]
    ### END SOLUTION

def pivot_random(lst,low,high):
    ### BEGIN SOLUTION
    return lst[random.randrange(low,high+1)]
    ### END SOLUTION

def pivot_median_of_three(lst,low,high):
    ### BEGIN SOLUTION
    return median(lst[low], lst[(low + high) // 2], lst[high])
    ### END SOLUTION

################################################################################
# TEST CASES
################################################################################
def randomize_list(size):
    lst = list(range(0,size))
    for i in range(0,size):
        l = random.randrange(0,size)
        r = random.randrange(0,size)
        lst[l], lst[r] = lst[r], lst[l]
    return lst

def test_lists_with_pfn(pfn):
    lstsize = 20
    tc = TestCase()
    exp = list(range(0,lstsize))

    lst = list(range(0,lstsize))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    lst = list(reversed(range(0,lstsize)))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    for i in range(0,100):
        lst = randomize_list(lstsize)
        quicksort(lst, pfn)
        tc.assertEqual(lst,exp)

# 30 points
def test_first():
    test_lists_with_pfn(pivot_first)

# 30 points
def test_random():
    test_lists_with_pfn(pivot_random)

# 40 points
def test_median():
    test_lists_with_pfn(pivot_median_of_three)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_first,
              test_random,
              test_median]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
