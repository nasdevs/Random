'''
@name : python exercise from pytnaticve.com
@authon : Nas...
'''

# ---------------------------------------------------
# list 

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# for i in range(0, len(list1)):
#     a = list1[i] + list2[i]
#     list3.append(a)
# print(list3)

# numbers = [1, 2, 3, 4, 5, 6, 7]
# powNumbers = [i**2 for i in numbers]
# print(powNumbers)

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# list3 = []

# for i in list1:
#     for j in list2:
#         a = list1[i] + list2[j]
#         list3.append(a)

# print(list3)

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list2.reverse()

# for i in range(len(list1)):
#     print(list1[i], ' ', list2)


# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# result = list(filter(None, list1))
# print(result)

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)

# ---------------------------------------------------
# loop

# limit = 5
# for i in range (0, limit+1):
#     for j in range(0, i):
#         print(j, end=' ')
#         if j == i-1: print('')

# a = int(input('Input : '))
# sum = 0
# for i in range(1, a+1):
#     sum+=i
# print(sum)

# num = 2
# limit = num*10
# for i in range(num, limit+1, num):
#     print(i)

# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i%5 == 0:
#         if i > 500: break
#         if i > 150: continue
#         print(i)

# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=' ')
#         if j == 1: print('')

# list1 = [10, 20, 30, 40, 50]
# list1.reverse()
# for i in list1:
#     print(i)

# for i in range(-10, 0, 1):
#     print(i)

# for i in range(5):
#     print(i)
#     if i == 5-1:
#         print('Done !')

# ---------------------------------------------------
# Dictonary

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# result = dict(zip(keys, values))
# print(result)

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# result = {**dict1, **dict2}
# print(result)

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# # solution 1
# print(sampleDict.get('class').get('student').get('marks').get('history'))
# # solution 2
# print(sampleDict['class']['student']['marks']['history'])

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# result = dict.fromkeys(employees, defaults)
# print(result)
