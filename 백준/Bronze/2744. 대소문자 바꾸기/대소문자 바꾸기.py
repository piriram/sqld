before = input()
after = ""
# A:65~90
# a:97~122
for element in before:
    e = ord(element)
    if e >= 97 and e<=122:
        after += chr(e-26-6)
    elif e>=65 and e<=90:
        after += chr(e+26+6)
    else:
        after += e

print(after)