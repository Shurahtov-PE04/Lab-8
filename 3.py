def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

print(gcd(36, 14))
print(gcd(100, 5))
print(gcd(-60, 48))