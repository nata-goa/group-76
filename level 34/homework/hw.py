#1
cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Telavi", "Barcelona", "Paris"]

for city in cities:
    if len(city) > 6:
        print(city)


#2
words = ["ice", "helloworld", "supercalifragilistic", "onetwothreefourfive"]

for word in words:
    if len(word) % 15 == 0:
        print(word)


#3
numbers = [5, 12, 48, 99, 120, 7, 33, 81]

count = 0
for number in numbers:
    count += 1

print("რიცხვების რაოდენობა სიაში:", count)


#4
words = ["apple", "grape", "melon", "plum", "peach", "banana"]

for word in words:
    if len(word) == 5:
        print(word)



#5
sentence = input("შეიყვანეთ წინადადება: ")

# ვითვლით საერთო სიმბოლოების რაოდენობას
length = 0
for char in sentence:
    length += 1

# ვითვლით რამდენი "a" ან "A" არის
a_count = 0
for char in sentence:
    if char == "a" or char == "A":
        a_count += 1

print("სულ სიმბოლოების რაოდენობა:", length)
print("'a' ან 'A' სიმბოლოების რაოდენობა:", a_count)


#6
strings = ["hello", "superman", "extraordinary", "fantastic", "AI", "universe"]

longest = ""
for s in strings:
    if len(s) > len(longest):
        longest = s

print("ყველაზე გრძელი სტრინგია:", longest)

