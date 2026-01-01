#1) 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   

evens = []   

for i in numbers:        
    if i % 2 == 0:       
        evens.append(i)  

print(evens)  


#2)
numbers = [3, 10, 5, 7, 12, 9, 15, 2, 21]

new_list = []

for i in range(len(numbers)):
    if i % 2 != 0:
        new_list.append(numbers[i])

print(new_list)


#3) 
names = ["გიგი", "ნიკა", "გაგი", "ლევანი", "გუგა", "თათია"]

for i in names:
    if i[0] == "გ" and i[-1] == "ი":
        names.remove(i)

print(names)


#4) 
words = ["Hello", "world", "Apple", "banana", "Car", "dog", "Python"]


#5) 
words = ["Hello", "world", "Apple", "banana", "Car", "dog", "Python"]


