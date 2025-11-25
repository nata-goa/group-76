#1
name = input("Enter your name: ")
print(name.upper())


#2
name = input("Enter your name (uppercase): ")
print(name.lower())


#3
name = input("Enter your name (lowercase): ")
print(name.capitalize())


#4
names = ["nika", "ana", "luka", "mari"]

for n in names:
    print(n.upper())


#5
names = ["NIKA", "ANA", "LUKA", "MARI"]

for n in names:
    print(n.lower())


#6
names = ["nika", "ana", "luka", "mari"]

for n in names:
    print(n.capitalize())


#7
lst = [1, 2, 3, 4, 5]
print(len(lst))


#8
text = "ალექსანდრე"
print(len(text))


#9
numbers = [1, 2, 3, 4, 5, 6, 8, 9]
count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print(count)


#10
numbers = [1, 2, 3, 4, 5, 6, 8, 9]
count = 0

for num in numbers:
    if num % 2 == 1:
        count += 1

print(count)


#11
start = int(input("Enter start: "))
end = int(input("Enter end: "))
step = int(input("Enter step: "))

for i in range(start, end, step):
    if i % 2 == 0:
        print(i)
