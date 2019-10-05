def sort_list(list):
    for num in range(len(list)-1,0,-1):
        for i in range(num):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

    return list         #I decided to return this list so that we can reuse this in the future
                        #instead of listing it here we can portion that part out depending on what we want to do with it

def search_list():
    list = [1,2,4,5,3]
    looking_for = int(input("What number are you looking for: "))
    for i in list:
        if int(i) == int(looking_for):
            print("Found number at place " + str(list[i]))
            return list[i]
    print("Found no number in list matching " + str(looking_for))
    return -1


if __name__ == '__main__':
    search_list()
    list = sort_list([3,5,7,2,1,4])
    print(list)
