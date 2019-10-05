
def make_list():
    input = []
    for i in range(3):
        input.append(int(get_input()))
    return input


def get_input():
    new_num = 0
    new_num = input("Please enter a number: ")
    if int(new_num) < 1 or int(new_num) > 50:
        raise ValueError

    return new_num


if __name__ == '__main__':
    list = make_list()
    for i in range(len(list)):
        print(list[i])
