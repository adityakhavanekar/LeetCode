s = "rat"
t = "car"

sl = []
tl = []

for i in s:
    sl.append(i)
for i in t:
    tl.append(i)

print(sl)
print(tl)

sl = sorted(sl)
tl = sorted(tl)

print(sl)
print(tl)

if sl == tl:
    print("true")
else:
    print("false")
