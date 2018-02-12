"""
Given a string check if it can be constructed by taking a substring of it and appending multiple copies of the substring 
together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

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
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

def is_substring_helper (data):
# =============================================================================
#     Input: string, lowercase, <10000 in length
#     Output: True/False, based on if the there are repeated substring in the input string  
# =============================================================================
    # YOUR CODE HERE
    div=2
    ans=False
    while div<=int(len(data)/2):
        if len(data)%div==0:
            match = 0
            sec_len=int(len(data)/div)
            for n in range(0,div-1):
                if data[sec_len*n:sec_len*(n+1)] in data[sec_len*(n+1):sec_len*(n+2)]:
                    match+=1
                if match == (div-1):
                    ans = True
            if ans == True:
                break
        div+=1
    return ans

#DON NOT CHANGE THIS FUNCTION
def is_substring (string_input):
	return is_substring_helper(string_input)


#test case
def main():
    TEST_CASE1 = "abab"
    TEST_CASE2 = "aba"
    TEST_CASE3 = "abcabcabcabc"

    print ("Testing your code with TEST_CASE1, the expected output is True, your output is {}".format(is_substring(TEST_CASE1)))
    print ("Testing your code with TEST_CASE2, the expected output is False, your output is {}".format(is_substring(TEST_CASE2)))
    print ("Testing your code with TEST_CASE3, the expected output is True, your output is {}".format(is_substring(TEST_CASE3)))

if __name__ == "__main__":
    main()