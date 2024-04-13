import os


root = r"nested1"
obj = os.listdir(root)
print(obj)
print(sorted(obj, reverse=True))
