def total_sum(lst):
    total=0
    for num in lst:
        total+=num
    return total

size=int(input("Enter the size of the list :"))
sample=[]
for i in range(size):
    value=int(input("Enter the number :"))
    sample.append(value)
print(sample)
print("sum of all numbers in list :", total_sum(sample))


