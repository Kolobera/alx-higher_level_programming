#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    lp = []

    while i < list_length:
        try:
            err = ""
            result = my_list_1[i]/my_list_2[i]
        except (TypeError, ValueError):
            result = 0
            err = "wrong type"
        except ZeroDivisionError:
            result = 0
            err = "division by 0"
        except IndexError:
            result = 0
            err = "out of range"
        finally:
            if err != "":
                print(err)
        lp.append(result)
        i += 1
    return lp
