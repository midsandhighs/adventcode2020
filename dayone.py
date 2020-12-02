#!python3
from itertools import combinations
with open('input.txt') as f:
    expenses = f.read().splitlines()

# print(expenses)

#part one
for a in range(len(expenses)):  
    for b in range(a,len(expenses)):
        if int(expenses[a])+int(expenses[b])==2020:
            print(int(expenses[a])*int(expenses[b]))

#part two
for a in range(len(expenses)):  
    for b in range(a,len(expenses)):
        for c in range(b,len(expenses)):
            if int(expenses[a])+int(expenses[b])+int(expenses[c])==2020:
                print(int(expenses[a])*int(expenses[b])*int(expenses[c]))