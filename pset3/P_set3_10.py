


def readfromtext(file_name):
    with open(file_name) as F:
        data=F.read()

    return data

s1=readfromtext("ditherSequence1.txt")
s2=readfromtext("ditherSequence2.txt")

print(s1.count("H"),s1.count("T"))
print(s2.count("H"),s2.count("T"))
