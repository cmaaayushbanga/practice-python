def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# easy way to use generators
def my_generator():
    for i in range(5):
        yield i

for j in gen:
    print(j)