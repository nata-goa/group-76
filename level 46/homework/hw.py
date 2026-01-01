
# 1) 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in nums:  # ვუვლით ასლს
    if i % 2 == 0 or nums.index(i) % 2 !=0:
        nums.remove(i)

print(nums)



# 2)
words = ["strawberry", "banana", "cherry"]

for i in words[:]:
    words.append(i)

print(words)



#3) 
words = ["car", "car", "plane"]
nums = [10, 25, 40, 55, 70]

for i in nums:
    if i > 20 and i < 50:
        words.append(str(i))

print(words)


# 4) 
words = ["apple", "Banana", "cherry", "Dog"]

for i in range(len(words)):
    first = words[i][0]
    if first == first.lower():
        words[i] = first.capitalize() + words[i][1:]

print(words)


# 5) თქვენი სიტყვებით ახსენით რას აკეთებს გავლილი მასალიდან ყველა შესწავლილი სიის და სტრინგის ფუნქციები და for ციკლი.

# for ციკლი გამოიყენება იმისთვის, რომ პროგრამამ ერთი და იგივე მოქმედება რამდენჯერმე შეასრულოს

# append() ამატებს ახალ ელემენტს სიის ბოლოში.

# remove() შლის სიიდან მითითებულ ელემენტს მნიშვნელობით (პირველივე რომელსაც შეხვდება).

# pop() შლის ელემენტს ინდექსით და გვიბრუნებს მას.

# index() გვიბრუნებს ელემენტის ინდექსს სიაში.

# len() აბრუნებს სიის ელემენტების რაოდენობას.

# lower() სტრინგის ყველა ასოს ხდის პატარა ასოდ.

# capitalize() სტრინგის პირველ ასოს ხდის დიდად, დანარჩენებს – პატარად.