from Model.GreedyString import GreedyStringMerger 
from Model.MinimumRotatedSortedArray import MinimumRotatedSortedArray
from Model.CombinationSum import CombinationSum

if __name__ == "__main__":
    # string list 
    # stringList_greedy = []
    # stringList_minirotate = [4,5,6,7,0,1,2]
    stringList_combinsum = [10,1,2,7,6,1,5]
    target = 8
    # merger = GreedyStringMerger(stringList_greedy)
    # merger = MinimumRotatedSortedArray(stringList_minirotate)
    merger = CombinationSum(stringList_combinsum, target) 
    result = merger.run()
    print("Your result is:", result)