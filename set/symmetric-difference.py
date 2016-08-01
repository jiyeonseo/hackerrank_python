#!/usr/bin/python

# https://www.hackerrank.com/challenges/symmetric-difference
a = input().strip()
aset = set(list(map(int,input().strip().split())))
b = input().strip()
bset = set(list(map(int,input().strip().split())))

adiffset = aset.difference(bset)
bdiffset = bset.difference(aset)

ablist = list(adiffset.union(bdiffset))
ablist.sort()

for n in range(len(ablist)):
    print(ablist[n])