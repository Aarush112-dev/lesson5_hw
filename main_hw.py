list = [64,5,42,24,8,10,51,1,82,91,73]

question = input("Select a sorting method: \na) bubble sort \nb) insertion sort \nc) merge sort")

def bubble(n):
    for i in range(len(n)):
        flag = False
        for j in range(i,len(n)):
            if n[i] > n[j]:
                flag = True
                n[i], n[j] = n[j], n[i]
    print(n)
    return flag

def insertion(n):
    for i in range(len(n)):
        key = n[i]
        j = i-1
        while key < n[j] and j >= 0:
            n[j+1] = n[j]
            j-=1
        n[j+1] = key
    print(n)

def merge(array):
    if len(array) > 1:
        midpoint = len(array)//2
        left_half = array[:midpoint]
        right_half = array[midpoint:]
        merge(left_half)
        merge(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            array[k] = left_half[i]
            k += 1
            i += 1
        while j < len(right_half):
            array[k] = right_half[j]
            k += 1
            j += 1
            print(array)

if question == "a":
    bubble(list)
elif question == "b":
    insertion(list)
else:
    merge(list)

question2 = int(input("What number are you looking for? "))

def binary_search(n):
    low = 0
    high = len(list)-1
    while low <= high:
        medium = (low + high)//2
        if n < list[medium]:
            high = medium-1
        elif n > list[medium]:
            low = medium + 1
        else:
            print("Number is in index {}".format(medium))
            return
    else:
        print("Number is not in list")

binary_search(question2)
