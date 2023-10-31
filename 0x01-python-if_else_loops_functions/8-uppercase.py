#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False


def uppercase(str):
    for c in str:
        if islower(c):
            result += chr(ord(c) - ord('a') + ord('A'))
        else:
            result += c
    print("{}".format(result))
