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
class GreedyStringMerger:
    def __init__(self, stringList):
        """
            init greedy string
            Params: 
                required strings(list): init string list
                non_merge_list(list): store none overlay string
                drop_pre(int): store first list key using for remove merged string
                drop_aft(int): store second list key using for remove merged string
                merged_string(string): new a merged string add to strings list
        """
        self.string_list = stringList 
        self.non_merge_list = []
        self.drop_pre = 0
        self.drop_aft = 0
        self.merged_string = ""


    def run(self):
        """
            Main process: Execute string merging operations until all strings are merged.                
        """
        while len(self.string_list) > 1:
            if not self.greedy_merge():
                if self.non_merge_list:
                    self.process_none_overlay_list()
                else:
                    break

        return self.string_list[0] if self.string_list else ""


    def greedy_merge(self) -> bool:
        """
            Merge strings using a greedy algorithm, giving priority to string pairs with the largest overlap.。
            Return: Boolean
                    True, all the string are merged
                    False, extract none overlay string need processing
                
        """
        while len(self.string_list) > 1:
            max_overlap = 0
            is_merged = False

            # Split the strings_list into groups of 4 and put them into batches for further processing
            batch_size = min(4, len(self.string_list)) 
            batch = self.string_list[:batch_size]

            for preStr in range(len(batch)):
                for afterStr in range(preStr + 1, len(batch)):
                    overlap, result = self.find_overlap(batch[preStr], batch[afterStr])
                    if overlap > max_overlap:
                        max_overlap = overlap
                        self.drop_pre = preStr 
                        self.drop_aft = afterStr
                        self.merged_string = result
                        is_merged = True
        
            if is_merged:
                self.string_controller()
                return True
            else:
                self.non_merge_list = batch
                return False


    def find_overlap(self, s1: str, s2: str, concat_only: bool = False) -> tuple[int, str]:
        """
            Finds the maximum overlap of two strings and returns the length of the overlap and the combined string.
            Params: 
                s1(string): first string in strings list
                s2(string): second string in strings list
                concat_only(boolean): processing two string concat only default is false
            Return:
                n_overlap(int) : number of overlap character
                result(string) : merged string result 
        """
        n_overlap = 0
        result = ""
        if not concat_only: 
            for i in range(1, min(len(s1),len(s2))+1):
                if s1[-i:] == s2[:i]:
                    n_overlap = i
                    result = s1 + s2[i:]

            for i in range(1, min(len(s1), len(s2)) + 1):
                if s2[-i:] == s1[:i]:
                    if i > n_overlap:
                        n_overlap = i
                        result = s2 + s1[i:]
        
        else:
            result = s2 + " " + s1

        return n_overlap, result
    
    def string_controller(self):
        """
            Add the merged string to the strings list, and remove to merge the strings
                
        """

        self.string_list.append(self.merged_string)
        self.string_list.pop(self.drop_aft)
        self.string_list.pop(self.drop_pre)
        

    def process_none_overlay_list(self):
        """
            Process non-overlapping string lists and try to merge non-overlapping string lists
            When all the contents of the list are merged, clear the list
        """
        if len(self.non_merge_list) and len(self.non_merge_list) > 1:
            for n_str in range(len(self.non_merge_list)-1):
                overlap, result = self.find_overlap(self.non_merge_list[n_str], self.non_merge_list[n_str+1], True)
                if len(result):
                    self.drop_pre = n_str
                    self.drop_aft = n_str+1
                    self.merged_string = result
        
        self.string_controller()
        self.non_merge_list = []
