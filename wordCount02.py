import string  # import for stripping away punctuation

lines = []
words = []
wc = {string: int}

myFile = open(input("Type in your file name: "), 'r')

for x in myFile:
    lines.append(x.strip())

myFile.close()

for x in lines:
    words.extend(x.split())

words.sort()

for x in words:
    for c in string.punctuation:  # stripping away punctuation
        x = x.replace(c, "")

    if x not in wc:
        wc[x] = 1

    else:
        wc[x] = (wc.get(x) + 1)

i = 0
for x in wc:
    print("{:2}. {} {}".format(i, x, wc.get(x)))
    i = i + 1



