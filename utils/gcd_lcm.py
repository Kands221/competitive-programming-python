import math

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
