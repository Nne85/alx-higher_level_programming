#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            div = 0
            if i < len(my_list_1):
                if isinstance(my_list_1[i], (int, float)):
                    div = my_list_1[i]
                else:
                    raise TypeError
            else:
                raise IndexError("out of range")
            if i < len(my_list_2):
                if isinstance(my_list_2[i], (int, float)):
                    div /= my_list_2[i]
                else:
                    raise TypeError
            else:
                raise IndexError("out of range")
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError as e:
            print(e)
            div = 0
        finally:
            new_list.append(div)
    return new_list
