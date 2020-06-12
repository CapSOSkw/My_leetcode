def quicksort(array, ascending = True):
    if array.__len__() < 2:
        return array  # the array is ordered if it has 1 or 0 element

    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        if ascending == False:
            return quicksort(greater, ascending=False) + [pivot] + quicksort(less, ascending=False)
        else:
            return quicksort(less) + [pivot] + quicksort(greater)



if __name__ == '__main__':
    print(quicksort([5,6,2,4,1,3]))