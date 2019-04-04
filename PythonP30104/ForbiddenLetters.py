# Author:karhik J
# # Purpose:This is used for checking and prinitng given word contains forbidden string
# # Date:04/04/2019
import itertools
# data=""
# forbiddenData = raw_input("ENTER THE INPUT FOR FORBIDDENNIG THE GIVEN TEXT")
# print forbiddenData
# t = list(itertools.permutations(forbiddenData, len(forbiddenData)))
# print t
# for i in range(0, len(t)):
#     data=''.join(t[i])
#     print type(data)
#     for i in data:
#         print "i value",i
# with open("sample.txt", "r+") as fobj:
#         for words in data :
#             print "www",words
#             for line in fobj:
#                 splittedWords = line.strip()
#                 print "Split words",splittedWords
#                 print "dat", data
#                 if data == splittedWords:
#                     print "dat",data
#                     fobj.write(splittedWords," ")
def forbidden(OriginalData,forbiddenData):
    for forbiddenletter in forbiddenData:
        if forbiddenletter in OriginalData:
            return False
    return True

value=""
count =0
list =[]
with open("sample.txt","r+") as fobj:
    forbiddenData = raw_input("ENTER THE FORBIDDEN LETTER")
    for line in fobj:
        words = line.split()
        for OriginalData in words:
             value=forbidden(OriginalData,forbiddenData)
             if value == True:
                 count = count +1
                 list.append(OriginalData)
    print "Words in the file does not contains forbidden letter",list
