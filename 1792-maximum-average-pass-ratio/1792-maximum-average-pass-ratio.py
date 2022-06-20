class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        #create heap of difference values
        #while extrastudents, pop element off the heap
        #increase pass and total by 1, push new tuple to heap, decrement extra students
        #go through each element in the heap, get the pass and total and add it to sum
        #divide this sum by len of classes
        
        h = []
        for passCount, total in classes:
            heapq.heappush(h,((float(passCount)/float(total))-((float(passCount+1))/float(total+1)), passCount, total))
            
        while extraStudents > 0:
            ratio, passCount, total = heapq.heappop(h)
            passCount += 1
            total += 1
            heapq.heappush(h, ((float(passCount)/float(total))-(float(passCount+1)/float(total+1)), passCount, total))
            extraStudents -= 1
                       
        average = 0
        for el in h:
            ratio, passCount, total = el
            average += float(passCount)/float(total)
            
        return average/len(classes)
                     
                       
                      