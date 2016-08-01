#!/usr/bin/python

# https://www.hackerrank.com/challenges/py-introduction-to-sets
# Enter your code here. Read input from STDIN. Print output to STDOUT
inputVal=int(input().strip());
inputArr=input().strip().split(" ");

tmpSet=set()

for n in range(inputVal):
    tmpSet.add(int(inputArr[n]))

print(sum(tmpSet)/len(tmpSet))