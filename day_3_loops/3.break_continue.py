#demonstrating break and continue in loops

#break example: stop loop when number recahes 5
for i in range(1,11):
    if i == 5:
        print("stopping at :",i)
        break
    print(i)

#continue example:now skipping 5 in loop
for i in range(1,11):
    if i == 5:
        print("skipping this number")
        continue
    print(i)