# Selection Sort Implementation in Python

'''
How does it work?

for i = 1:n,
    k = i
    for j = i+1:n, if a[j] < a[k], k = j
    → invariant: a[k] smallest of a[i..n]
    swap a[i,k]
    → invariant: a[1..i] in final position
end

What is selection sort?

The selection sort algorithm is a combination of searching and sorting. 
It sorts an array by repeatedly finding the minimum/maximum element from unsorted part
and putting it at the end.
In selection sort, the inner loop finds the next smallest (or largest) value and the outer 
loop places that value into its proper location.

'''

def selection_sort(unsorted_arr):
    for x in range(len(unsorted_arr)):
        # store current position
        n = x
        # search for the position of the next smallest value
        for y in range(x+1, len(unsorted_arr)):
            if unsorted_arr[y] < unsorted_arr[n]:
                n = y
        # swap next smallest value into postition
        swap(x,n,unsorted_arr)
        print(unsorted_arr)

def swap(a, b, array):    
    temp2 = array[a]
    array[a] = array[b]
    array[b] = temp2    

arr = [10,9,7,8,6,5,4,2,3,1]
print("Unsorted: ", arr)
selection_sort(arr)
print("Sorted: ", arr)