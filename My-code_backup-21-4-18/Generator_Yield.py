
def count(limit):
    c = 0
    while c <= limit:

        yield c
        c += 1

gen = count(3)
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
print (next(gen))
# for i in gen:
#     print (i)

