def simpleGeneratorFun():
    pre1 = 1
    pre2 = 1
    sumValue = 1
    yield sumValue
    for i in range (0, 5):
        yield sumValue
        sumValue = pre1 + pre2
        pre1 = pre2
        pre2 = sumValue

for value in simpleGeneratorFun():
    print(value)
    