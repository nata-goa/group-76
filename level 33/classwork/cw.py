
text = input("შეიყვანე სიტყვა ან ტექსტი: ")

length = len(text)
print("შენი ტექსტის სიგრძეა:", length)

print("ტექსტის თითოეული სიმბოლო:")
for i in range(len(text)):
    print(text[i])
