# put your python code here
import math


def heron(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area


s1 = int(input())
s2 = int(input())
s3 = int(input())

print(heron(s1, s2, s3))
