def frequency(s):
    from collections import Counter
    words = s.split()
    freq = dict(Counter(words))
    return dict(sorted(freq.items()))

print("10:", frequency("this is a test this is only a test"))
