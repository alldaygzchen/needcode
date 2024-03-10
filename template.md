# while template

```
i=0
while True:
    if i == len(arr):
        return "Done"
    print(i)
    i+=1
```

```
for i in range(len(arr)):
    print(i)
return "Done"
```

# backtracking template

```
explore all the solutions, we use backtracking
```

1. define global variables
2. create helper function with params for current value (id) and current state
3. create ending cases for backtracking and the process to go to another helper function using current state

# fast and slow pointer (linked lists cycle detection)

```

    slow = head
    fast = head
    idx = 0

    # cycle detection

    while True:

        if slow == fast and idx!=0:
            break

        if not (fast and fast.next):
            return None

        slow = slow.next
        fast = fast.next.next
        idx+=1


            slow2 = head

    # get value

    while True:
        if slow == slow2:
            return slow

        slow =slow.next
        slow2 = slow2.next
        idx+=1

```

# two heaps template

```
1. create small value max heap and large value min heap
2. insert and check length
3. get median
```

# dynamic programming template
