a = 'first'
b = 'last'
k = 'b' if a is b else 'b' or 'a'
out = eval(k)
print(out, type(out))
