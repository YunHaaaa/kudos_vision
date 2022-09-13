import os

fp = open("train.txt", "r")
fw = open("trainval.txt", "a")

for line in fp:
    arr = line.split('.')
    suffix = arr[-1]
    tmp = arr[0].split('/')
    if suffix == 'jpg\n' or suffix == 'png\n':
        fw.write(tmp[-1])
        fw.write("\n")
fw.close()
