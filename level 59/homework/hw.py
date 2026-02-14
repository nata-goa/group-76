
# 2) 
num_word = input("Enter string and integer: ")
nums = "0123456789"
sumof = 0

for i in num_word:
    if i in nums:
        sumof += int(i)

print(sumof)




# 3)
text = input("შეიყვანე წინადადება: ")  
words = text.split()                   
result = ""                             

i = 0
while i < len(words):                  
    result += words[i]               
    if i != len(words) - 1:              
        result += " "                  
    i += 1                               

print(result)              



# 4) 
numbers = [1, 3, 2, 4, 6, 5]  
count = 0                      
i = 1                          

while i < len(numbers):
    if numbers[i] > numbers[i - 1]:  
        count += 1                   
    i += 1                           

print(count)