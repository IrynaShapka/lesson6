# # HW1
# import string
# lst = str(string.ascii_letters[:])
# text1 = str(input("enter first letters: "))
# text2 = str(input("enter second letters: "))
# t = "%s-%s" % (text1, text2)
# print(t)
# print(lst.index(text1))
# print(lst.index(text2))
# i = lst.index(text1)
# j = lst.index(text2)
# if i <= j:
#     print(lst[i:j+1])
# else:
#     print("Error: swap the letters")

# #HW2
# import string
# number = int(input("enter the number: "))
# print(number)
# d = number // 86400
# h = (number - 86400 * d) // 3600
# m = (number - 86400 * d - 3600 * h) // 60
# s = (number - 86400 * d - 3600 * h - 60 * m)
#
# if d >= 5 and d % 10 != 1 and d % 10 != 2 and d % 10 != 3:
#     t = "%d днів, %s:%s:%s" % (d, str(h).zfill(2), str(m).zfill(2), str(s).zfill(2))
#     print(t)
# elif d == 0:
#     t = "%d днів, %s:%s:%s" % (d, str(h).zfill(2), str(m).zfill(2), str(s).zfill(2))
#     print(t)
# elif d % 10 == 1:
#     t = "%d день, %s:%s:%s" % (d, str(h).zfill(2), str(m).zfill(2), str(s).zfill(2))
#     print(t)
# elif d == 1:
#     t = "%d день, %s:%s:%s" % (d, str(h).zfill(2), str(m).zfill(2), str(s).zfill(2))
#     print(t)
# else:
#     t = "%d дні, %s:%s:%s" % (d, str(h).zfill(2), str(m).zfill(2), str(s).zfill(2))
#     print(t)

#HW3
number = int(input("enter the number: "))
print(number)

while number > 9:
    number1 = str(number)
    number = 1
    for i in number1:
        number *= int(i)
    print(number)

