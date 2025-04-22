# 8. Remove duplicates and sort words
def convert(s):
    words = set(s.split())
    return ' '.join(sorted(words))

print("8:", convert("hello world and hello universe"))
