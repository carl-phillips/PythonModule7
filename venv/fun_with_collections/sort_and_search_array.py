"""Carl Phillips
This program sorts an array given, and searches an array for a value the user provides
"""
import array as arr

def sort_array(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array.tolist()       #I decided to return a list isntead of an array,
                                #this way it is easier to get values
                                #I also decided to return so that we can more easily use this in the future
def search_array():
    a = arr.array('i', [6,3,4,1,8,7])
    looking_for = int(input("What number are you looking for: "))
    try:
        print("Found number at place " + str(a.index(looking_for) + 1))
        return a.index(looking_for)
    except ValueError:
        print("Found no number in list matching " + str(looking_for))
        return -1


if __name__ == '__main__':
    search_array()
    array = sort_array(arr.array('i', [3,5,7,2,1,4]))
    print(array)
