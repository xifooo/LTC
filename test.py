class A:
    def __format__(self, spec):
        if spec == "x":
            return "0XA"
        return "<A>"
    
# print(f"{A()}")
# print(f"{A():x}")

print("{}".format(15))
print("{:b}".format(15))
print("{:x}".format(15))

print(f"{15}")
print(f"{15:b}")
print(f"{15:x}")

