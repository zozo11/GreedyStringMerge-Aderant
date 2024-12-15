# Greedy String Merger
### Project Overview

```GreedyStringMerger``` is a tool based on a greedy algorithm that efficiently merges multiple strings by identifying the maximum overlapping parts. The program iteratively merges strings into a single complete sentence or result.

Key use cases include text concatenation, data processing, and other tasks requiring string merging.

---


### Features

- **Greedy Merging Algorithm**:
Iteratively compares string fragments and merges the pair with the largest overlap.
- **Dynamic Handling**:
Supports dynamic processing of unmerged strings, ensuring all strings are eventually merged.
- **Simple and Efficient**:
Compatible with Python 3.0+ and provides simple function calls to achieve complex merging logic.

---
### Usage Instructions
#### 1. Environment Requirements
- **Python Version**: Python 3.0 or later

#### 2. Running the Program
To execute the program, use the following command in the terminal:
```
python main.py
```
**Input Example**
Define the list of strings to be merged in ```main.py```Example:

```
 stringList = [
    "all is well",
    "ell that en",
    "hat end",
    "t ends well"
]
```
**Output Example**
The program outputs the final merged string:
```
Final Result: all is well that ends well
```
---
### Unit Testing
This project includes comprehensive unit tests located in the tests directory.
**Running Unit Tests**
Execute all tests using the following command:
```
python -m unittest discover -s tests
```
**Test Coverage**
The tests cover the following:

- Core algorithm (find_overlap).
- String merging functionality (greedy_merge).
- Special case handling (process_none_overlay_list).

---

#### File Structure
```
.
├── Model/
│   ├── __init__.py          # Module initialization
│   ├── GreedyString.py      # Core implementation of the greedy algorithm
│
├── tests/
│   ├── __init__.py          # Test module initialization
│   ├── test_greedy_string.py # Unit test file
│
├── main.py                  # Main program entry point
├── README.md                # Project documentation
```

---
#### Core Functionality
**1. find_overlap**
- Purpose: Identifies the maximum overlapping part between two strings and merges them.
- Inputs:
s1: The first string.
s2: The second string.
concat_only: boolean value, handle none overlap case.
- Outputs: Returns the overlap length and the merged string.

**2. greedy_merge**
- Purpose: Merges the pair of strings with the largest overlap.
- Input: A list of strings.
- Output: Updates the string list after merging.

**3. process_none_overlay_list**
- Purpose: Handle the special case of non-overlapping string and add the last non-repeating field to the returned string.
  
**4. string_controller**
- Purpose: Overall control of deleting merged strings and adding new strings. Merged string and drop string key.

**5. run**
- Purpose: Executes the complete string merging process until a single result is achieved.
- Input: A list of strings.
- Output: The final merged string.

--- 

### Contributing
Contributions are welcome! If you have ideas for improvements or enhancements, feel free to submit an issue or a pull request.

---
### Author
If you have any questions or suggestions about the project, feel free to reach out.

- GitHub: [zozo_11](https://github.com/zozo11)





