def bubblesort(mylist):
    '''Bubble Sort'''
    length = len(mylist)
    for i in range(length - 1):
        print(mylist)
        for j in range(length - 1 - i):    # After every iteration you don't compare the last one as they already sorted
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
    return(mylist)


def insertionsort(mylist):
    '''Insertion Sort'''
    length = len(mylist)
    for i in range(1, length):
        print(mylist)
        for j in range(i - 1, -1, -1):          # want array indexes from reverse order like 5,4,3,2,1. As this would be sorted array
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
            else:
                break
    return(mylist)


def selectionsort(mylist):
    '''Selection Sort'''
    length = len(mylist)
    # Outer loop we always go for one less that length because element will not compare with itself. Applicable for all sort
    for i in range(0, length - 1):
        print(mylist)
        minindex = i
        for j in range(i + 1, length):
            if mylist[minindex] > mylist[j]:
                minindex = j
        if minindex != i:
            mylist[i], mylist[minindex] = mylist[minindex], mylist[i]
    return(mylist)

# Merge Sort


def merge(A, B):  # Merge A[0:m],B[0:n]
    (m, n, C) = (len(A), len(B), [])
    (i, j) = (0, 0)  # current position in A and B
    while i + j < m + n:  # i+j is number of elements merged so far
        if(i == m):  # Case-1 : A is empty
            C.append(B[j])
            j += 1
        elif(j == n):  # Case-2 : B is empty
            C.append(A[i])
            i += 1
        elif(A[i] < B[j]):  # Case-3 : Head of A is small
            C.append(A[i])
            i += 1
        elif(B[j] < A[i]):  # Case-4 : Head of B is small
            C.append(B[j])
            j += 1
    return C


def mergesort(A, left, right):
    # Sort the slice A[left:right]
    if right - left <= 1:  # Base case
        return (A[left:right])
    if right - left > 1:  # Recursive Call
        mid = (left + right) // 2
        L = mergesort(A, left, mid)
        R = mergesort(A, mid, right)
        return(merge(L, R))


# L = list(range(10000, 0, -1))
L = [5, 9, 4, 8]

print("Original Array : ", L)
print("Bubble")
print("*" * 50)
after_sort = bubblesort(L)
print(after_sort)

print("Insertion")
print("*" * 50)
L = [5, 9, 4, 8]
after_sort = insertionsort(L)
print(after_sort)

print("Selection")
print("*" * 50)
L = [5, 9, 4, 8]
after_sort = selectionsort(L)
# after_sort = mergesort(L, 0, len(L))
print(after_sort)


# Refernce:
# https://www.youtube.com/watch?v=Nkw6Jg_Gi4w&list=PLj8W7XIvO93rJHSYzkk7CgfiLQRUEC2Sq&index=1
# https://www.youtube.com/watch?v=V7fvTmhqokM&list=PL3pGy4HtqwD02GVgM96-V0sq4_DSinqvf&index=19
