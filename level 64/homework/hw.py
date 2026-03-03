
# 1)
def greet(name):
    return "გამარჯობა, " + name + "!"

print(greet("გიგა"))
print(greet("მარი"))
print(greet("ნიკა"))


# 2)

def sum_numbers(num1, num2):
    return num1 + num2

print(sum_numbers(3, 5))
print(sum_numbers(10, 20))
print(sum_numbers(-4, 7))


# 3)
def square(num):
    return num * num

print(square(2))
print(square(5))
print(square(-3))
print(square(10))


# 4)
def check_age(age):
    if age >= 18:
        return "სრულწლოვანი ხარ"
    else:
        return "არ ხარ სრულწლოვანი"

print(check_age(18))
print(check_age(20))
print(check_age(15))


# 5)
def count_chars(text):
    print(len(text))

count_chars("გამარჯობა")
count_chars("Python")
count_chars("Hello World")



# 6)

def multiply(num1, num2):
    return num1 * num2

print(multiply(3, 4))
print(multiply(5, 6))
print(multiply(-2, 10))



# 7)


def check_score(score):
    if score >= 90:
        return "შესანიშნავი ქულა"
    elif score >= 70 and score <= 89:
        return "კარგი ქულა"
    elif score >= 50 and score <= 69:
        return "დამაკმაყოფილებელი ქულა"
    else:
        return "ჩაჭრილი"

print(check_score(95))
print(check_score(82))
print(check_score(60))
print(check_score(30))


# 8)
def even_or_odd(number):
    if number % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"

print(even_or_odd(4))
print(even_or_odd(7))
print(even_or_odd(0))
print(even_or_odd(13))



# 9)
def first_letter(name):
    return name[0]

print(first_letter("Giorgi"))
print(first_letter("Nika"))
print(first_letter("Mariam"))
print(first_letter("Luka"))


# 10)
def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print(average(3, 6, 9))
print(average(10, 20, 30))
print(average(5, 7, 11))
print(average(-2, 4, 8))


# 11)

def check_password(password):
    if password == "python123":
        return "წვდომა დაშვებულია"
    else:
        return "არასწორი პაროლი"

print(check_password("python123"))
print(check_password("Python123"))
print(check_password("123python"))
print(check_password("mypassword"))


# 12)

def to_uppercase(text):
    return text.upper()

print(to_uppercase("გამარჯობა"))
print(to_uppercase("Python"))
print(to_uppercase("hello world"))
print(to_uppercase("mariam"))