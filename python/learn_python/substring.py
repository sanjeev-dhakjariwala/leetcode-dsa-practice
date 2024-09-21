def generateSubstring(s):
    res = []
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            temp = s[i: j + 1]
            res.append(temp)
    print(res)
generateSubstring("aabb")

"""
['a', 'aa', 'aab', 'aabb', 'abb', 'b', 'bb', 'b', 'a', 'ab']
['a', 'aa', 'aab', 'aabb' ,'abb', 'b', 'bb']
"""
