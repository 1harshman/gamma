#!/usr/bin/env python

values = open('rosalind_ini3.txt').read().split()

s = str(values[0])
a = int(values[1])
b = int(values[2])
c = int(values[3])
d = int(values[4])

first = str(s[a:b+1])
second = str(s[c:d+1])

f = open('rosalind_ini3ans.txt', 'w')
ans = str(first + ' ' + second)
f.write(ans)