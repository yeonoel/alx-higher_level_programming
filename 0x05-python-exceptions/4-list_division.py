#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    test = []
    for i in range(list_length):
        try:
            div = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            text = "division by 0"
            div = 0
            print("division by 0")
        except TypeError:
            text = "wrong type"
            div = 0
            print("wrong type")
        except IndexError:
            text = "out of range"
            div = 0
            print("out of range")
        finally:
            test.append(div)
    return (test)
