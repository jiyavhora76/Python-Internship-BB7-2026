numbers = [12, 45, 23, 12, 67, 45, 89, 23, 90, 67, 34, 12, 56, 89, 10]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("Original list:", numbers)
print("List without duplicates:", result)