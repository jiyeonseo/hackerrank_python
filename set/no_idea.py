#!/usr/bin/python

# https://www.hackerrank.com/challenges/no-idea
n, m = input().strip().split()
elarray = set(list(map(int,input().strip().split())))
A = set(list(map(int,input().strip().split())))
B = set(list(map(int,input().strip().split())))

## Solution1
#print [(i in A) - (i in B) for i in elarray]

## Solution2
n, m = input().split()
arr = [int(x) for x in input().split()]
A = set([int(y) for y in input().split()])
B = set([int(z) for z in input().split()])
count = [0 + 1 if x in A else 0-1 if x in B else 0 + 0 for x in arr]
print(sum(count))