#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        # try inside for loop, each element is tried independently
        # try outside for loop, loop stops after first error
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list


# Another solution - Using zip() + enumerate()
'''
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i, (a, b) in enumerate(zip(my_list_1, my_list_2)):
        if i > list_length:
            break
        try:
            result = a / b
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    # zip() iterates two lists, it will stop at the shortest one
    # range(len(new_list), list_length) will be filled with 0 to ensure new_list_length = list_length
    for i in range(len(new_list), list_length):
        print("out of range")
        new_list.append(0)
    return new_list
'''

# Another solution - Using while loop
'''
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while i < list_length:
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
        i += 1
    return new_list
'''
