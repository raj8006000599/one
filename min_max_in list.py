
def result(list):
    minn, maxx = list[0], list[0]
    for number in list[1:]:
        if number < minn:
            minn = number

        elif number > maxx:
            maxx = number
    return minn,  maxx

list = [1, 2, 3, 6, 1, 0, 8, 10, 7, 2]

minn, maxx = result(list)
print(minn, maxx)





















