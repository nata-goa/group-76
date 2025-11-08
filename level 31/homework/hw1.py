
# 1)
lst1 = [1, 2, 3, 4, 5, 6]
lst1[2:4] = [10, 20, 30]
print(lst1)
# [1, 2, 10, 20, 30, 5, 6]


# 2)
lst2 = ["apple", "banana", "cherry", "kiwi", "mango"]
lst2[0:2] = ["pear", "plum"]
print(lst2)
# ['pear', 'plum', 'cherry', 'kiwi', 'mango']


# 3)
lst3 = ["a", "b", "c", "d", "e", "f"]
lst3[-3:] = ["x", "y", "z"]
print(lst3)
# ['a', 'b', 'c', 'x', 'y', 'z']


# 4)
lst4 = ["red", "green", "blue", "yellow", "black", "white"]
lst4[2:6] = ["purple", "orange"]
print(lst4)
# ['red', 'green', 'purple', 'orange']


# 5)
lst5 = ["გიორგი", "ირმა", "საბა"]
lst5[:] = ["red", "green", "blue", "yellow", "black", "white"]
print(lst5)
# ['red', 'green', 'blue', 'yellow', 'black', 'white']






