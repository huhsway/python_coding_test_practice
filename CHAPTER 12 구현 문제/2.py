data = input()

s = []
n = 0

for i in range(len(data)):
    if data[i].isdigit():
        n += int(data[i])
    if data[i].isalpha():
        s.append(data[i])

s.sort()

result = "".join(s)
result += str(n)

print(result)