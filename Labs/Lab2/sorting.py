# Sorting method
# This method will sort the values by keeping the start unchanged


def sort(self):

        k = self.start
        s = self.size

        for a in range(s):

            for b in range((a+1), s):

                if (self.cir[(a+k)%len(self.cir)] > self.cir[(b+k)%len(self.cir)]):

                    temp = self.cir[(a+k)%len(self.cir)]
                    self.cir[(a+k)%len(self.cir)] = self.cir[(b+k)%len(self.cir)]
                    self.cir[(b+k)%len(self.cir)] = temp


sort()