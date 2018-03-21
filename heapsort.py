# Heap sort implementation in Python

'''
What is Heap sort algorithm?
Heap sort is a comparison-based sorting algorithm. Heap sort can be thought of as an improved selection sort.

Like that algorithm, it divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region.

The improvement consists of the use of a heap data structure rather than a linear-time search to find the maximum

ALGORITHM:
# heapify
for i = n/2:1, sink(a,i,n)
→ invariant: a[1,n] in heap order

# sortdown
for i = 1:n,
    swap a[1,n-i+1]
    sink(a,1,n-i)
    → invariant: a[n-i+1,n] in final position
end

# sink from i in a[1..n]
function sink(a,i,n):
    # {lc,rc,mc} = {left,right,max} child index
    lc = 2*i
    if lc > n, return # no children
    rc = lc + 1
    mc = (rc > n) ? lc : (a[lc] > a[rc]) ? lc : rc
    if a[i] >= a[mc], return # heap ordered
    swap a[i,mc]
    sink(a,mc,n)

'''

arr = [10,9,7,8,6,5,4,2,3,1]
n = len(arr)

# function to swap largest element in the heap
def maxheap(arr, i):
    left = 2*i
    right = 2*i + 1
    maxx = i
    if left <= n and arr[left] > arr[i] :
        maxx = left
    if right <= n and arr[right] > arr[maxx]:
        maxx = right
    if maxx != i:
        #swap(arr, i, maxx)
        #maxheap(arr, maxx)

def heapify(unsorted_arr):
    for x in range()