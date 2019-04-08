from collections import deque

que = deque([])
que.append(10)
que.append(20)
que.append(30)
que.append(40)
que.popleft()
print(que)
que.pop()  # pop right
print(que)
que.appendleft(5)
print(que)

print("_"*50)

que.clear()
if not que:
    print("Que is empty")
else:
    print("Que has values")
