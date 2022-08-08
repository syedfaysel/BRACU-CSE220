def printArray(array, l):
    # if (l < len(array)-1):
        # print(array[l], end =' ')
        # printArray(array, l+1)
    if (l == len(array)):
        return
    else:
        # print(array[len(array)-1])
        print(array[l],end=" ")
        return printArray(array, l+1)

printArray([10,20,30,40],0)




# input(m):
#     if (m==0):
#         print(" ")
#     else:
#         input(m-1)
#         printSeq()
#         print("\n")

# printSeq(m)
#     if (m==0):
#         print(" ")
#     else:
#         printSeq(m-1)
#         print(m)