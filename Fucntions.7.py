# 7. Check if a string is a palindrome
def ispalindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print("7:", ispalindrome("A man a plan a canal Panama"))
print("7:", ispalindrome("Hello"))
