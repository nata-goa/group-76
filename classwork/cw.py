#შექმენი სია რომელშიც იქნება მხოლოდ int ტიპის ელემენტები,ამ სიიდან წაშალე 
# ყველა რიცხვი რომელიც არის კენტი,დაბჭდე სია

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers [:]:
    if num % 2 != 0:
        numbers.remove(num)
print(numbers)

#შექმენი რამე სიტყვის ცხვლადი და გადაიყვანე uppercase

word = "natali"
print(word.upper())

