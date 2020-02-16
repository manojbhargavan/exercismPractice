count = 0


def get_count():
    return count


def set_count(number):
    # Python needs to be explicitly told to use global variable else it creates a new local variable
    global count
    count = number


print(get_count())
set_count(10)
print(get_count())