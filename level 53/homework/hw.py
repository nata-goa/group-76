
# 2)
words = ["game", "GOAL", "Nice", "giga", "Hello", "NOTE", "test"]

new_list = []

for w in words:
    if w.islower() and w[0] == "g":
        new_list.append("Goga")
    elif w.isupper() or w[0] == "N":
        new_list.append("Nika")
    else:
        new_list.append("ლიდერი")

print(new_list)



# 3)
nums = [1, 2, 3, 4, 5, 6]
new_list = []

i = 0
while i < len(nums):
    if nums[i] % 2 == 0 or i % 2 == 0:
        new_list.append(nums[i] ** 2)
    else:
        new_list.append(nums[i] * 2)
    i += 1

print(new_list)



# 4)
words = ["PYTHON", "coding", "HELLOOO", "Nika", "World"]
new_list = []

i = 0
while i < len(words):
    if len(words[i]) > 6 or words[i].isupper():
        new_list.append(words[i].lower())
    else:
        new_list.append(words[i] * 2)
    i += 1

print(new_list)



# 5)
numbers = "0123456789"
new_list = []

for i in range(len(numbers)):
    digit = int(numbers[i])
    if i % 2 == 0 or digit > 7:
        new_list.append(digit)

print(new_list)



numbers = "0123456789"
new_list = []

i = 0
while i < len(numbers):
    digit = int(numbers[i])
    if i % 2 == 0 or digit > 7:
        new_list.append(digit)
    i += 1

print(new_list)