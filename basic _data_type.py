lst = []

n = int(input())


for _ in range(n):
    command = input().strip().split()
    action = command[0]
    
    if action == "insert":
        i, e = int(command[1]), int(command[2])
        lst.insert(i, e)
    elif action == "print":
        print(lst)
    elif action == "remove":
        e = int(command[1])
        lst.remove(e)
    elif action == "append":
        e = int(command[1])
        lst.append(e)
    elif action == "sort":
        lst.sort()
    elif action == "pop":
        lst.pop()
    elif action == "reverse":
        lst.reverse()
