"""
Given a string check if it can be constructed by taking a substring of it and
appending multiple copies of the substring
together. You may assume the given string consists of lowercase English letters
only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc"
twice.)
"""


def is_substring_helper(data):
    # test case 'abcabdabcabdabcabd'
    # recursive solution?
    substring_bool = False
    if len(data) < 2:
        return(substring_bool)
    char1_idx = [i for i, e in enumerate(data) if e == data[0]]
    possible_intervals = []
    for i in range(1, len(char1_idx)-1):    # need to check only ~half these?
        all_divisible = True
        for j in range(i+1, len(char1_idx)):
            if char1_idx[j] % char1_idx[i] != 0:
                all_divisible = False
        if all_divisible == True:
            possible_intervals.append(char1_idx[i])
    #for i in range(1, (len(data)//2)+1):
    #    print(data[i])
    #    if data[i] == char1:
    #        if data[:i] == data[i:2*i]:
    return(substring_bool)


#DO NOT CHANGE THIS FUNCTION
def is_substring(string_input):
    return is_substring_helper(string_input)


#test case
def main():
    TEST_CASE1 = "abab"
    TEST_CASE2 = "aba"
    TEST_CASE3 = "abcabcabcabc"

    print("Testing your code with TEST_CASE1, the expected output is True, \
          your output is {}".format(is_substring(TEST_CASE1)))
    print("Testing your code with TEST_CASE2, the expected output is False, \
          your output is {}".format(is_substring(TEST_CASE2)))
    print("Testing your code with TEST_CASE3, the expected output is True, \
          your output is {}".format(is_substring(TEST_CASE3)))


if __name__ == "__main__":
    main()
