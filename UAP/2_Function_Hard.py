def isPalindrome(s):
    clean_str = ''.join(filter(str.isalnum, s)).lower()
    return clean_str == clean_str[::-1]

string = 'radar'

def palindrome(string):
    return isPalindrome(string)

result = palindrome(string)
print(result)