#text = 'the day is sunny the the the sunny is is'
#hashMap = {}
#for word in text.split(' '):
#    if word not in hashMap:
#        hashMap[word] = 1
#    else:
#       hashMap[word] += 1
#
#print hashMap

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#for x in a:
#    if x < 5:
#        print x
#
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c = []
#for x in a:
#    if x in b and x not in c:
#        c.append(x)
#print(c)
#print(list(set(a) & set(b)))


'''
def Fibonacci (entry):
    if entry < 2:
        return entry

    a = 1
    b = 0
    result = 0
    while entry >= 0:
        result = a + b
        a = b
        b = result
        entry -= 1

    return result

def defangIPaddr(address):
    for char in address:
        print(char)

print(defangIPaddr('127.0.0.1'))


def Bracket (entry):
    entry = list(entry)
    for x in range(len(entry)):
        if entry[x] == '.':
            entry[x] = '[.]'

    return ''.join(entry)

print Bracket(entry = '10.253.8.144')

def List (entry):
    entry = list(entry)
    temp = 0
    for x in entry:
        if entry[x] == entry[temp]:
            temp = x + 1
            entry[x] = entry[temp]
        return entry
print List([1, 1, 2, 2, 3, 4, 3, 3, 9, 7, 7])'''




#
#
# def Fibonacci (entry):
#     if entry < 2:
#         return entry
#
#     a = 1
#     b = 0
#     result = 0
#     while entry >= 0:
#         result = a + b
#         a = b
#         b = result
#         entry -= 1
#
#     return result
#
# print Fibonacci(56)
#
#
#
# def Bracket (entry):  #take pound in []
#     entry = list(entry)
#     for x in range(len(entry)):
#         if entry[x] == '.':
#             entry[x] = '[.]'
#
#     return ''.join(entry)
#
# print Bracket(entry = '10.253.8.144')
#
#
#
#
# def TestHardPassword (password):
#     evaluation = 0 # evaluation min = 4, max = 12
#     password = password.replace(' ', '')
#     eva_count = 0
#     if password.__len__() >= 6:
#         print ('Lenght OK')
#         eva_count +=1
#     else:
#         print ('Lenght Fail')
#
#     if password.__len__() in [6, 7, 8]:
#         evaluation += 1
#     if password.__len__() in [9, 10]:
#         evaluation += 2
#     if password.__len__() > 10:
#         evaluation += 3
#
#     s_count, n_count, l_count = 0, 0, 0
#
#     for symbol in password:
#         if symbol in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_']:
#             s_count += 1
#         if symbol.isdigit():
#             n_count = n_count + 1
#         if symbol.isupper():
#             l_count = l_count + 1
#
#     if s_count > 0:
#         print ('Symbol OK')
#         eva_count += 1
#     else:
#         print ('Symbol Fail')
#     evaluation += min(s_count, 3)
#     if n_count > 0:
#         print ('Number OK')
#         eva_count += 1
#     else:
#         print ('Number Fail')
#     evaluation += min(n_count, 3)
#     if l_count > 0:
#         print ('Letter OK')
#         eva_count += 1
#     else:
#         print ('Letter Fail')
#     evaluation += min(l_count, 3)
#     percent = '%'
#     percent_evaluation = 0
#     if eva_count < 4:
#         percent_evaluation = (evaluation * 50 / 4)
#     else: percent_evaluation = ((evaluation - 4) * 50 / 8) + 50
#     # 4 = 50%
#     # 12 = 100%
#     # 8 after 4 = 50%
#     print ("Your password is complex at %d%s" % (percent_evaluation, percent))
#
# TestHardPassword('T%h6gg%6FFyg')













import os

print(os.getcwd())
os.chdir(r"/Users/akulakova/Library/Preferences/PyCharmCE2019.2/dir1")
os.startfile(r'C:\Users\mike\Documents\labels.pdf') #open file
print(os.getcwd())








