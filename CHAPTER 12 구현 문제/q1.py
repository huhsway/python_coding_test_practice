num = input()
n = len(num)

a = 0
b = 0

for i in num[:n]:
    a += int(i)

for i in num[n:]:
    b += int(i)

if a == b:
    print("LUCKY")
else:
    print("READY")