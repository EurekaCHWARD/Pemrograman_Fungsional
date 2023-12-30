def isPalindrome(kata):
    return kata == kata[::-1]

def filterPalindromes(kalimat):
    kataKata = kalimat.split()
    palindromes = filter(lambda kata: isPalindrome(kata.lower()), kataKata)
    nonPalindromes = filter(lambda kata: not isPalindrome(kata.lower()), kataKata)
    return list(palindromes), list(nonPalindromes)

string = "Ada apa dengan Eureka Diaandisy"
palindromes, nonPalindromes = filterPalindromes(string)

print("Data =", string.split())
print("Palindrome =", palindromes)
print("Non-Palindrome =", nonPalindromes)