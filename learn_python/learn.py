from collections import deque, defaultdict
import heapq

""" s = "Sanjeev Jha"
print(s[::-1])
print(s[0: 5])

original_string = "Hello, World!"
modified_string = original_string[:-1]
print(modified_string)

arr = [1, 2, 3, 4, 5]
print(arr.pop())
arr.append(6)
print(arr) """

# queue = deque()
# queue.append(1)
# queue.append(2)
# queue.append(2)

# doc = defaultdict(list)
# doc["name"].append("Sanjeev")
# doc["name"].append("Naina")
# doc["name"].append("Priyanka")
# print(queue)
# print(doc)

# res = ["1("]
# print(res[0][0])

""" arr = [1, 2, 3, 4, 5]
print(arr[0:3]) """

heap = [1, 36, 2, 3]
heapq.heappush(heap, 5)
heapq.heapify(heap)
print(heap)
""" print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap)) """

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = [1, 2, 3, 4, 5, 6]
print(arr)
