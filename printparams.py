def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    b = 25
    c = [1, 2, 3]
    print(a, b, c)


print_params()


def print_params(a=1, b=2):
    print(a, b)


print_params()


def print_params():
    print()


print_params()


def print_params(*args):
    print(args)


values_list = ['a', 1, True]
print_params(*values_list)


def print_params2(**kwargs):
    print(kwargs)


values_dict = {'a': 1, '1': 'b', 'True': [1, 2, 3]}
print_params2(**values_dict)


def print_params3():
    print(print_params3())


# values_list_2 = ['a', 2]
# print_params3(*values_list_2, 42)
