def uppercase(str):
    l=""
    for c in str:
        if 65 <= ord(c) <= 90:
            l += c
        else:
            l += chr(ord(c) - 32)
    print(l)
