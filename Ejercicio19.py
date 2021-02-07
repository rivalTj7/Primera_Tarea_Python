# 19  Dot an Cross

from numpy import *
n = int(input())
A = array([list(map(int,input().split()))for _ in range(n)])
B = array([list(map(int,input().split())) for _ in range(n)])

X = dot(A,B)
print(X)
