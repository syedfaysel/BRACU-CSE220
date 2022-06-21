def intersection(self, c2):
    
    # To Do
    intersection_with_none=[None]*self.size
    count=0
    k=self.start
    m=None
    for i in range(self.size):        #---- 40, 50, None, None, None, 10, 20, 30
      m=c2.start
      for j in range(c2.size):        #---- 10, 20, 5, None, None, None, None, None, 5, 40, 15, 25
        if self.cir[k]==c2.cir[m]:
          intersection_with_none[count]=self.cir[k]
          count+=1
        m=(m+1)%len(c2.cir)
      k=(k+1)%len(self.cir)

    intersection=[None]*count
    for i in range(len(intersection)):
      intersection[i]=intersection_with_none[i]
    return intersection