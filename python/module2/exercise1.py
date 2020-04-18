import sys
digit = int(sys.argv[1])

print((digit > -15 and digit <= 12) or (digit > 14 and digit < 17) or (digit >= 19))