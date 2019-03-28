# i = 0
# number = int(input("Enter the number"))
# sum1 = 0
# while number > 0:
#     i = number%10
#     sum1 = sum1 + i
#     number = number//10
# print(sum1)



student = []
sorted_score = []
names = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
student.sort(key = lambda x: x[1])
sorted_score = student
largest = max(sorted_score(key = lambda x:x[1]))
for i in range(sorted_score.count()):
    if largest == max(sorted_score(key = lambda x:x[1])):
        names.append(sorted_score.remove(max(sorted_score(key = lambda x:x[1]))))

names.sort(key = lambda x:x[0])
print(names)