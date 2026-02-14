
# 1)
sentence = "სწავლა წარმატების გასაღებია"
vowels = "აეიოუ"
count = 0

for i in sentence:
    if i in vowels:
        count += 1

print("ხმოვანი ასოების რაოდენობა:", count)


# 2) 
numbers = [3, 6, 8, 1, 10, 7, 4]
even = 0

for i in numbers:
    if i % 2 == 0:
        even += i

print("ლუწი რიცხვების ჯამი:", even)


# 3) 
numbers = [5, 12, 7, 20, 3, 15]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("სიის ყველაზე დიდი რიცხვია:", largest)



# 4)
password = input("შეიყვანეთ პაროლი: ")

while len(password) < 6:
    print("Your password is correct!")
    password = input("შეიყვანეთ პაროლი: ")

print("Your password is correct!")


# 5)
numbers = [3, 5, 3, 8, 5, 10, 8]
nums = []

for i in numbers:
    if i not in nums:
        nums.append(i)

print(nums)


# 6)
sentence = input("შეიყვანეთ წინადადება: ")
words = sentence.split()
printed = []

for i in words:
    if i not in printed:
        count = 0
        for w in words:
            if w == i:
                count += 1
        print(i, count)
        printed.append(i)



# 7)
secret_number = 7
attempts = 0

guess = int(input("Guess the number: "))
attempts += 1

while guess != secret_number:
    print("Try again!")
    guess = int(input("Guess the number: "))
    attempts += 1

print(f"Correct! Attempts: {attempts}")