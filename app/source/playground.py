from string import punctuation

s = "hella.long?stirng?"
# s = s.strip("long")
s = ''.join(c for c in s if c not in punctuation)
print(s)
