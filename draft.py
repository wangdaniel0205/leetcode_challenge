from collections import Counter
candidate = [10,1,2,7,6,1,5]
count = Counter(candidate)
group = [[k, count[k]] for k in count.keys()]
print(group)
# %%
s = "eat"
l = []
for c in s:
    i = 0
    for k in l:
        if k >= c:
            break
        i += 1
    l.insert(i,c)
print(hash(tuple(l)))
# %%
h = {'a':[1], 'b':[2]}
print(list(h.values()))
# %%
