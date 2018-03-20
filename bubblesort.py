# Bubblesort Implementation In Python
'''
for i = 1:n,
    swapped = false
    for j = n:i+1,
        if a[j] < a[j-1],
            swap a[j,j-1]
            swapped = true
    → invariant: a[1..i] in final position
    break if not swapped
end

What are Properties of Bubble Sort?
- Stable
- O(1) extra space
- O(n2) comparisons and swaps
- Adaptive: O(n) when nearly sorted

What is Performance of Bubble Sort?
- Worst-case performance	O(n^{2})
- Best-case performance	O(n)
- Average performance	 O(n^{2})
- Worst-case space complexity	O(1) auxiliary

'''


def bubblesort(unsorted_arr):
    for x in range(len(unsorted_arr)):        
        for y in range(len(unsorted_arr)-1):
            n = y + 1
            if unsorted_arr[y] > unsorted_arr[n]:
                swap(n,y,unsorted_arr)
        print(unsorted_arr)

def swap(a, b, array):    
    temp2 = array[a]
    array[a] = array[b]
    array[b] = temp2    

arr = [0,1,22,3,13,0]
print("Unsorted: ", arr)
bubblesort(arr)
print("Sorted: ", arr)