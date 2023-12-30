string = 'radar'

def kalimatDecorator(func):
    def wrapper(*args, **kwargs):
        hasil = func(*args, **kwargs)
        if hasil:
            return "Kalimat merupakan palindrome."
        else:
            return "Kalimat bukan palindrome."
    return wrapper

@kalimatDecorator
def isPalindrome(s):
    clean_str = ''.join(filter(str.isalnum, s)).lower()
    return clean_str == clean_str[::-1]

def palindrome(string):
    return isPalindrome(string)

hasil = palindrome(string)
print(hasil)