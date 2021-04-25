N, M = map(int, input().split())
people = set(list(map(int, input().split()))[1:])
left = [] 
for i in range(M): 
    x = list(map(int, input().split()))[1:]
    if len(people.intersection(set(x))) != 0: 
        people = people.union(set(x))
    else:
        left += [x]

left_c = [1 for c in range(len(left))]
for _ in range(len(left)): 
    for i, p in enumerate(left): 
        if len(people.intersection(set(p))) != 0:
            people = people.union(set(p))
            left_c[i] = 0
print(sum(left_c))
