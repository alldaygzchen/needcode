https://docs.google.com/spreadsheets/d/1Z6BECY1EIo3ZLYON8f-YlHwo_QAH1yApBUlu8Qs11i8/edit#gid=0

# Arrays (Implement Stack):

1. 1 byte = 8bits (e.g. 00000001)
2. ASCII code=> e.g. 1 = 4 bytes , a= 1 bytes
3. RAM is measured by byte
4. array index has a mapping relationship with the address in RAM
5. Complexity [Static/Dynamic array] :
   - r/w ith element <=>O(1)
   - Insert/Remove element (Suppose is empty) <=> O(1)
   - Insert/Remove middle <=> O(n)
6. Creating an array of length 8 took (not including moving value): 1+2+4+8<=2(8)~O(2n)
7. Amortized Complexity: Creating double space has O(n) but in average pushing a value is O(1)
8. Subarray problems => sliding window
9. two pointer => l &lt; R
10. if not divide and conquer => iterative, if divide=>recursion

# Stacks :

1. Last In First Out
2. Complexity
   - Insert/Remove <=> O(1)
   - Peek <=> O(1)

# Linked Lists (Implement Queues):

1. Linked Lists\Double Linked List Complexity
   - r/w ith element <=>O(n)
   - Insert/Remove element (assuming having reference node[head or tail]) <=> O(1)
   - Insert/Remove middle (assuming having reference node[head or tail]) <=>O(1)

# Advance Linked Lists

1. Fast and Slow Pointer :

- Find the middle of a linked list. (if the length is even, fast pointer will be at len(arr) and slow pointer will be at the larger middle point)
- Determine if a Linked List has a cycle. (Using hash set need additional complexity)
- Determine if a Linked List has a cycle and return the head. (need mathematical proof)

# Queues

1. First In First Out
2. push <=> enqueue, shift<=>dequeue
3. Complexity
   - enqueue <=> O(1)
   - dequeue <=> O(1)
4. arrays cannnot achieve queue when dequeue but can acheive stack
5. linked list can acheive queue

# Recursion

1. one branch and two branch recursion
2. recursion: iteration or divide and conquer
3. I wrote a overall comparison in fibonacci.py which is great

# Sorting(Requires recursion and swap)

1. stable (Insertion,Merge) vs unstable order(Quick,Bucket)
2. Insertion order: sorted(O(n)), not sorted(O(n^2)), O(n) space memory [compare the insertion and all the lements before]
3. merge sort:O(nlog(n)) [recursion] [divided to 2 sorted array and use pointer to merge]
4. quick sort:O(n\*\*2) can be modified to O(nlogn) by selecting best pivot point [use pivot point to divide 2 sorted arrays ]
5. bucket sort:O(n) constraint: finite range, O(c) space memory

# Binary Search

1. L &le; R
2. Time complexity:O(logn) Space complexity:O(1)

# Trees

## Binary Tree

1. leaf node: nodes without children
2. root node
3. no cycles
4. height of the node: including itselt and its desendant
5. depth of the node: including itself and the root node

## Binary Search Trees (BST)

1. every single node of the left subtree is strictly lower than the parent node
2. every single node of the right subtree is strictly greater than the parent node
3. no duplicates
4. search for O(logn) [balance tree]. To be more precise it is O(h)
5. Although has two branch, since it goes to one direction thus it is one branch recursion
6. Balance: for every node, the left and right subtree height is differ by one
7. Inserting and deleting in sorted array is O(n), but binary tree is O(logn)

# BST Insert and Remove:

1. inserting and deleting in binary tree is O(logn)

# Advance trees algorithm

## Trie (prefix tree)

1. insert word: O(n) [the word has n character] (this can be done by hashmap)
2. search word: O(n) [the word has n character] (this can be done by hashmap)
3. search prefix: O(n)
4. A trie is a tree with each node a character with no value in root node and no redundant node

## Union Find

1. union: since both have a path to the root, the children is connected

## Segment Tree

1. find the middle and split in two half [0,M] [M+1,len(arr)-1], where [] is a closed set
2. update O(logn) and queryRange O(4log(n)) [prefix sum with array, the prefix need to be calculated if it is updated ]
3. update, build, rangeQuery are all divide and conquer
4. we store the value in the segment node for cache, so there is no need to go to the end

## Iterative DFS

1. inorder: if curr left or curr right is None, pop the stack
2. preorder: if curr left, pop the stack

# Depth First Search:

1. bst traversal is inorder (left->node->right), time complexity:O(n)
2. creating a sorting array: time complexity O(n+nlog(n))=>O(nlog(n)) [create a tree O(nlog(n)) and traversal O(n)]
3. preorder traversal
4. postorder traversal

# Breadth First Search:

1. Does not suit recursion since left and right are meaningless
2. also called level order traversal
3. time complexity: O(n)

# BST Sets and Maps:

1. set and map are implemented at binary search tree or hashset and hashmap
2. For python map created by binary search tree is called treeMap

```
from sortedcontainers import SortedDict
```

# Backtracking

1. Based on DFS apply to binary tree
2. Brute force approach
3. trees are mostly divide and conquer problem, thus using recursion is suitable
4. check the root head before recursion

# Advance Backtracking

1. subsets and combinations are quite same but adding constriction
2. commonly subset and combination pattern is to add current element and move foward

# Heap and Priority Queue(it is not binary search tree) (swap like array)

1. linked list create queue. binary heap creates priority queue
2. priority queue. Same as queue but can get min/max k items dynamically when pushing
3. satisfies complete binary tree: no holes except leaf nodes
4. added left to right in every level
5. every left and right subtree should be greater or equal than the root node value
6. can have duplicates, while binary search tree not
7. we can apply using array since its structure and order property (leftchild=2i, rightchild=2i+1, parent=i//2)
8. insert:O(log(n)),remove: O(log(n)), min/maxsearch: O(c)
9. Percolating up and down the end of the list satisfies the structure and order property
10. heapify: creating heap there are n elements:O(nlog(n)), however using heapify from input array cost O(n) [Percolating down is more efficient since less number node from the top should execute]
11. we can also use heap to sort array since remove is O(log(n)) thus O(nlog(n))
12. heaps disadvantage: search, heap advantage: sort and min/max search

# Advance heaps algorithm

1. calculate median for unsorting array(nlog(n))
2. considering array inserting a new value, it takes O(n) and finding the median is O(1)
3. streaming value: 1.inserting O(logn) 2. check length and 3.get median O(1)
4. python does not have max heap (for small values)

# Hashing

1. treemap: insert:O(logn) remove:O(logn) search:O(logn) sorting:O(n)  
   hashmap: insert:O(1) remove:O(1) search:O(1) sorting:O(nlogn)
2. creating a hashmap: time complexity O(n) sapce complexity:O(n)
3. Implementation: hashing key to index and store the object in the element in array
4. Like dynamic array, we could increase the hashmap length to decrease collison
5. Also we can change the value to linked list = to decrease collision
6. Another solution is open addressing (find the next available to push the object)
7. prime number is a better solution for hashmap length

# Graphs

1. Vertices == node, edges==connection
2. Number of vertices\*\*2 &ge; number of edges
3. Directed graph: edges have direction e.g. tree, linked list
4. Ways of representing graphs: matrix, adjacency matrix, adjacency list
5. Matrix [undirected edge]: 0 is node, 1, is blocked
6. Adjacency Matrix [directed edge]: index represent nodes, the value ==1 means edge exists
7. Adjancecy list: create graph node class with property neighbor (less space complexity than adjacency matrix)
8. Matrix Dfs: time complexity O(4^(n\*m)), space complexity:O(n\*m)
9. two methods for matrix dfs: traversal and divide and conquer
10. bfs has better time complexity since it does not duplicate unnecessary steps

# Advance graphs algorithm

1. Dijkstra: time complexity O(Elog(V^2))
2. Prims: Find Minimum spanning Tree (connecting all the nodes (edges = nodes -1) without a cycle and minimize the total cost of the edges)
3. Kruskal: Find Minimum spanning Tree where Time complexity: O(Elog(V)) and space complexity:O(E)
4. time complexity: O(Elog(V^2)), space complexity:O(E)
5. trees: undirected connected graph

# Dynamic programming

1. memoization search can be only used in dfs divide and conquer not dfs traversal
2. dynamic programming have a better time complexity than memoization
3. all dynamic programming call be transfer to memoization
4. memoization is more suitable for more complex problems
5. overall, dfs backtracking seems to have the worst time complexity
6. dynamic ends at n+1,while memoization starts at n.

# Advance Dynamic programming algorithm

1. knapsack: skip or include
2. unbounded knapsack: skip or include
3. lcs:
   - subsequence may not be continous comparing to subarray
   - subsequence consider order while subset not

# Bit manipulation

1. base 10 (2)vs base 2 (...000010)e.g. 2
2. 23&1 => 10111& 00001=> 00001
3. <<1 : shift left by one place (multiply current value with 2 )

# Leetcode thought:

1. consider step to step or recursive(backtracking [preorder] or divide and conquer) [basic_algo\recursion\fibonacci.py]
2. if recursive, consider a backtracking [exploring all solutions] or divide and conquer[overlapping subproblems] (since it is dfs, create the base case)
3. if divide and conquer, consider the divide and conquer adding memoization or dp

# Tricks

1. if len(arr)==0, for loop will skip
