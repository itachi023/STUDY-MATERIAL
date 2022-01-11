import os
for i in os.listdir():
    if i.endswith(".py"):
        print(i)