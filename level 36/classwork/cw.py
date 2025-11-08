
text = "Caravan"
has_a = ('a' in text) or ('A' in text)      
has_car = 'car' in text.lower()

print(has_a)   # True
print(has_car) # True
