
def make_list():
    input = []
    for i in range(3):
        input.append(get_input())
    return input


def get_input():
    new_num = 0
    try:
        new_num = int(input("Please enter a number: "))
    except:
        print("Error, please enter a number")
    return new_num


if __name__ == '__main__':
    list = make_list()
    for i in range(len(list)):
        print(list[i])
