'''
Created on 23 Sep 2015

@author: tobydobbs
'''

import math

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    
def insertionSort(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            swap(array, j, j-1)
            j = j - 1

def bubbleSort(array):
    swapped = True
    while(swapped == True):
        swapped = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                swapped = True
    return array

def selectionSort(array):
    for i in range(len(array)):
        minimum = i
        for j in range(i+1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        swap(array, i, min)
        
def quickSort(array, lo, hi):
    if lo < hi:
        p = partition(array, lo, hi)
        quickSort(array, lo, p - 1)
        quickSort(array, p + 1, hi)

def partition(array, lo, hi):
    wall = lo
    pivot = hi
    for i in range(lo, hi):
        if array[i] < array[pivot]:
            swap(array, wall, i)
            wall += 1 # move the wall up one space
    swap(array, wall, hi)
    return wall

def mergeSort(array):
    print "array: " + str(array)
    if len(array) == 1:
        return array
    left, right, middle = [], [], int(math.floor(len(array)/2))
    for i in range(middle):
        left.append(array[i])
    for i in range(middle, len(array)):
        right.append(array[i])
        
    left = mergeSort(left)
    right = mergeSort(right)
    
    return merge(left, right)

def merge(left, right):
    print "left: " + str(left) + ", right: " + str(right)
    result = []
    while len(left) and len(right):
        if left[0] <= right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]
    while len(left):
        result.append(left[0])
        del left[0]
    while len(right):
        result.append(right[0])
        del right[0]
    return result

def main():
    array = [1,5,6,3,9,4,6,2,4,5,3,8]
    print array
    quickSort(array, 0, len(array) - 1)
    print array
    
if __name__ == "__main__":
    main()      
