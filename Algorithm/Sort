array = [8,4,6,2,5,1,3,7,9]

def bubble_sort(array): #O(n^2)
    n = len(array)
    for i in range(n-1):
        for j in range(n - i -1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        print(array)
        
def selection_sort(array): #O(n^2)
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        print(array)

def insertion_sort(array): #O(n^2)
    n = len(array)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j - 1], array[j] = array[j], array[j - 1]
        print(array)
        
def merge_sort(array): #O(n*logn) . 2n개의 메모리 공간필요
    if len(array) < 2:
        return array
    mid = len(array) // 2
    low_arr = merge_sort(array[:mid])
    high_arr = merge_sort(array[mid:])
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    print(merged_arr)
    return merged_arr

def quick_sort(array): # O(n^2)
    if len(array) <= 1:
        return array
    pivot = len(array) // 2
    front_arr, pivot_arr, back_arr = [], [], []
    for value in array:
        if value < array[pivot]:
            front_arr.append(value)
        elif value > array[pivot]:
            back_arr.append(value)
        else:
            pivot_arr.append(value)
    print(front_arr, pivot_arr, back_arr)
    return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)

def counting_sort(array): # O(n+k)
    count = [0] * (max(array) + 1)
    result = [0] * (len(array))
    for num in array:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]
    for num in array:
        index = count[num]
        result[index - 1] = num
        count[num] -= 1
    print(result)
    
'''출처
https://seongonion.tistory.com/130
https://velog.io/@jguuun/%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
'''
