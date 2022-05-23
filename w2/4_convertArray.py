#converting a circular array to a linear array


circularArray = [40, 50, 0, 0, 0, 0, 0, 0, 10, 20, 30]

def linearize(circular,start,size):

    linear = [0]*len(circular)

    index = start
    i = 0

    while (i<size):
        linear[i] = circular[index]

        index=(index+1)%len(circular)

        i+=1

    # print(linear)
    return linear



lineared = linearize(circularArray,8,5)
print(lineared)

# output: [10, 20, 30, 40, 50, 0, 0, 0, 0, 0, 0]

