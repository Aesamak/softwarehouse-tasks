
import time
def random(x,y):
    a = 1664525
    c = 1013904223
    m = 2**32
    seed = int(time.time() * 1000000) % m
    seed = (a * seed + c) % m
    random_in_range = x + (seed % (y - x + 1))
    return random_in_range

x = int(input("Enter the start of the range: "))
y = int(input("Enter the end of the range: "))

print(random(x, y))
def from_list(lis):
    l=len(lis)-1
    i=random(0,l)
    print(lis[i])
lis=[1,2,3,4,5]
from_list(lis)