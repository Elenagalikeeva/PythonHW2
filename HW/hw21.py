import os
os.makedirs("PythonHW2/nested1/nested2/nested3")

root = r"nested1"
obj = os.listdir(root)
objs = list(map(lambda i: os.path.join(root, i), obj))
print(objs)