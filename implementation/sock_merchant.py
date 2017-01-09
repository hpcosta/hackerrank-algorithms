#!/bin/python

# https://www.hackerrank.com/challenges/sock-merchant

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

c.sort()
pairs = 0
flag = False
for i in range(0, len(c)):
	if flag:
		flag = False
		continue
	if i+1 < len(c):
		if c[i] == c[i+1]:
			pairs += 1
			flag = True

print(pairs)