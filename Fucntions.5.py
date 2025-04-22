# 5. Check if a string is a pangram
def ispangram(s):
    import string
    alphaset = set(string.ascii_lowercase)
    return alphaset <= set(s.lower())

print("5:", ispangram("The quick brown fox jumps over the lazy dog"))
print("5:", ispangram("Hello world"))
