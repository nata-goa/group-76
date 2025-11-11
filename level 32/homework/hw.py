#1
for i in range(1, 51):
    if i % 2 == 0:
        print(f"{i} ლუწია")
    else:
        print(f"{i} კენტია")


#2
for i in range(0, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} იყოფა 3-ზე და 5-ზე")
    elif i % 3 == 0:
        print(f"{i} იყოფა 3-ზე")
    elif i % 5 == 0:
        print(f"{i} იყოფა 5-ზე")
    else:
        print(f"{i} არ იყოფა არცერთზე")


#3
n = int(input("შეიყვანეთ რიცხვი: "))
even_count = 0
odd_count = 0

for i in range(0, n+1):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"ლუწი რიცხვების რაოდენობა: {even_count}")
print(f"კენტი რიცხვების რაოდენობა: {odd_count}")


#4
numbers = [10, 25, 33, 47, 80, 99]
for num in numbers:
    if num > 50:
        print(f"{num} მეტი 50-ზე")
    else:
        print(f"{num} ნაკლები 50-ზე")


#5
total = 0
for i in range(0, 101):
    if i % 2 == 0:
        print(i)
        total += i
print(f"ლუწი რიცხვების ჯამია: {total}")


#6
words = ["apple", "banana", "avocado", "grape", "apricot"]
for word in words:
    if word.lower().startswith('a'):
        print(word)


#7
for i in range(0, 21):
    if i == 0:
        print(f"{i} ნულია")
    elif i % 2 == 0:
        print(f"{i} ლუწია")
    else:
        print(f"{i} კენტია")


#8
numbers = [5, 15, 25, 35, 45, 55]
for num in numbers:
    if num % 5 == 0:
        print(num)


#9
word = input("შეიყვანეთ სიტყვა: ")
for letter in word:
    print(letter)


#10
total = 0
for i in range(1, 11):
    total += i
print(f"ჯამი არის: {total}")
