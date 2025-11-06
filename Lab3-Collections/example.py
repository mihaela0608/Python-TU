import random

s1 = [4, 5, "ab", "abc"]
print(s1[3])
s1[3]= 23
print(s1)

s2 = list()
s2 = "ksi"
print(s2)
s2 = ['k', 's', 'i']
print(s2)

s = []
s.append(5)
s.append(23)
s.append(123)
print(s)

l = list(k for k in range(1, 21) if k%3 == 0)
print(l)


s = [1, 2, 3, 4, 5, 6]
print(s[::-1])
print(s[:-1])
print(s[1:])
print(s[0:2])
print(s[-1:])

s1 = [8, 9]
newS = s + s1
print(newS)

s3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]
print(s3[0][3])
print(s3[1][0])
print(s3[2][1])

s4 = [41 , 54, 87, 96]
for i in s4:
    print(i, end=" ")
print()
print(l.index(3))
print(l.count(2))

print(min(l))
print(max(l))

s4.append(22)
print(s4)
s4+= [4, 8, 58]
print(s4)
s4.insert(0, 90)
print(s4)
s4.pop(0)
print(s4)
s4.remove(4)
print(s4)

random.shuffle(s4)
print(s4)
s4.reverse()
print(s4)
print(random.choice(s4))


k = (7, 5, 3, 6, 1)
print(k[0])
print(k[2:3])
print(7 in k)
print(k * 3)
tup = k + (2, 4)
print(tup)


d = dict()
d1 = dict(name="ivan", last_name="petrov")
d2=dict([ ("name", "polina"), ("last_name", "koleva")])
print(d1)
print(d2)

d["name"] = "Mihaela"
d["last_name"] = "Bataklieva"
print(d)
keys = list(d.keys())
keys.sort()
for key in keys:
    print("{0} => {1}".format(key, d[key]), end=" ")