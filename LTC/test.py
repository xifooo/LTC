def A():
    def B():
        print("hello")
    return B()

# A()
result = A()
# print(A())
print(result)
