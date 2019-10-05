def sort_list():
    list = [1,2,4,5,3]
    looking_for = int(input("What number are you looking for: "))
    for i in list:
        if int(i) == int(looking_for):
            print("Found number at place " + str(list[i]))
            return list[i]
    print("Found no number in list matching " + str(looking_for))
    return -1


def search_list():
    pass

def get_list():
    pass


if __name__ == '__main__':
    sort_list()
