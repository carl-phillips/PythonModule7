
def make_list():
    input = []
    for i in range(3):
        try:
            input.append(int(get_input()))
        except ValueError:
            print("Error, please enter a number")
    return input


def get_input():
    new_num = 0
    new_num = input("Please enter a number: ")
    return new_num


if __name__ == '__main__':
    list = make_list()
    for i in range(len(list)):
        print(list[i])
