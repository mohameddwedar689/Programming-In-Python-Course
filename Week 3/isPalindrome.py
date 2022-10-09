# Algorithm For Palindrome String

def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for i in str:
        if str[startIndex] != str[endIndex]:
            return False
    
    return True

str1 = "abba"
str2 = "abab"
print(isPalindrome(str1))
print("--------")
print(isPalindrome(str2))