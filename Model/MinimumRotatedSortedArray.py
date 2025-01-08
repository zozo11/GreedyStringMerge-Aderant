class MinimumRotatedSortedArray:
    def __init__(self, stringList):
        self.sList = stringList

    
    def run(self):
        '''
        Separate this list. Since it is in ascending order, 
        it may be 4567 and 0123 after ascending order. 
        Divide the sequence into two parts and compare from the first part. 
        If 4 is greater than 0, narrow the array range to the second part and start searching. 
        Left stores unique
        '''
        left, right = 0, len(self.sList) -1
        
        while left < right:
            mid = (left + right) // 2
            #//2 is equal to integer
            if self.sList[mid] < self.sList[right]:
                right = mid
            elif self.sList[mid] > self.sList[right]:
                left = mid
            else: 
                right -= 1
            
        return self.sList[left]


