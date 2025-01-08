'''
1. Sorting the array:
Sorting is a critical step because it makes it easier to avoid repeated combinations and prune in advance during the traversal process to reduce unnecessary calculations.
2. Remove unnecessary candidate numbers:
If a number is larger than the target, skip it directly because it alone exceeds the target value and cannot appear in the final combination.
3. Accumulate step by step and search recursively:
Start from the first number in the array and try to add combinations in turn, and check whether the accumulated sum is equal to the target.
If the current accumulated sum exceeds the target, skip it directly (prune).
If the current accumulated sum is exactly equal to the target, add the current combination to the result set.
If the sum is less than the target, continue to recursively add the next number.
4. Avoid repeated combinations:
Use a sorted array to ensure that the same number is not selected repeatedly. For example, if two adjacent numbers are equal, we only need to consider the first number.
5. Recursion and backtracking:
In each recursion, dynamically update the current combination, and backtrack to the previous step at the end of the recursion to try other possible combinations.
'''

class CombinationSum:
    def __init__(self, candidates, target):
        # Sorting to facilitate subsequent handling of duplicates
        self.candidates = sorted(candidates)
        self.target = target
        self.result = []

    def run(self):
        # 从第一个元素开始递归搜索
        self.backtrack(0, [], 0)
        return self.result

    def backtrack(self, start, current_combination, current_sum):
        # If the current sum is equal to the target value, save the result
        if current_sum == self.target:
            self.result.append(list(current_combination))
            return

        # If the current sum exceeds the target value, stop the recursion and backtrack to delete the last value.
        if current_sum > self.target:
            return

        # Traverse the candidate number, starting from the start index
        for i in range(start, len(self.candidates)):
            # Skip Duplicates
            if i > start and self.candidates[i] == self.candidates[i - 1]:
                continue
            # Add the current number to the combination
            current_combination.append(self.candidates[i])
            # Recursive call, note that i + 1 here means that each number can only be used once
            self.backtrack(i + 1, current_combination, current_sum + self.candidates[i])
            
            # Backtrack and remove the last number added
            current_combination.pop()