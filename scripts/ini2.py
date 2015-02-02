#!/usr/bin/python

values = open('rosalind_ini2.txt').read().split()

a = int(values[0])
b = int(values[1])
c = int(a**2+b**2)
ans = str(c)

f = open('rosalind_ini2ans', 'w')
f.write(str(c))