'''
    Greedy matching and merging algorithm

    The program loops through the sentence fragments in the list, 
    compares the repeated parts of each pair of sentences, 
    finds the largest repeated part each time and merges them. 
    After each merge, a new string is created for the string list, 
    and the merged sentences are deleted until all sentences are merged into a complete result.

    Python environment: Python 3.10.9
    Run the program: ```python main.py```
    Input data: The program supports list data format, and each element in the list should be of string type.
    eg: 
    string_list = [
        "all is well",
        "ell that en",
        "hat end",
        "t ends well",
        "new comment added"
    ]

    Unit Tests: The unit test files are located in the tests folder.
    Run the following command to execute all unit tests: ```python -m unittest discover -s tests```
    
'''
from Model.GreedyString import GreedyStringMerger 

if __name__ == "__main__":
    # string list 
    stringList = []

    merger = GreedyStringMerger(stringList)
    result = merger.run()
    print("Your result is:", result)