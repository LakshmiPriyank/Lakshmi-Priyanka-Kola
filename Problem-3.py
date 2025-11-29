a = int(input("Enter a number: "))

if a % 2 == 0:
    a -= 1

result = []
for i in range((a + 1)//2):
    result.append(1 + 2*i)

print(result)
