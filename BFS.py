from copy import copy, deepcopy
import time

class Node:
    def __init__(self):
        self.parent = None
        self.state = None
        self.pathCost = 0
        self.depth = 0

class Queue :
    def __init__(self):
        self.Q =[];
    def isEmpty(self):
        if self.Q == []:
            return True
        else:
            return False
    def put(self,item):
        self.Q.insert(0,item)
    def take(self):
        return self.Q.pop()
    def size(self):
        return len(self.Q)


def Search(initialNode,goalState):
    numberOfNode = 0
    solution = [Node()]
    fringe = Queue()
    fringe.put(initialNode)
    while not fringe.isEmpty():
        numberOfNode += 1
        node=fringe.take()
        if(node.state == goalState):
            while node:
                solution.append(node)
                node=node.parent
            break
        fringe = BFS(node,fringe)
    print("number of node opened:{}".format(numberOfNode))
    return solution


def BFS(node,fringe):
    stateOfNode = [row[:] for row in node.state]
    x = 0
    y = 0
    for i in range(len(stateOfNode)):
        for j in range(len(stateOfNode[i])):
            if stateOfNode[i][j] == ' ':
                x = i
                y = j
    for i in range(-1,2):
        if i != 0:
            if x + i >= 0 and x + i <= 2:
                newNode = Node()
                newNode.parent = node
                newNode.depth = node.depth + 1
                newNode.pathCost = node.pathCost + 1
                temp = stateOfNode[x + i][y]
                stateOfNode[x + i][y] = stateOfNode[x][y]
                stateOfNode[x][y] = temp
                newNode.state = stateOfNode
                stateOfNode = deepcopy(node.state)
                fringe.put(newNode)
    for j in range(-1, 2):
        if j != 0:
            if y + j <= 2 and y + j >= 0:
                newNode = Node()
                newNode.parent = node
                newNode.depth = node.depth + 1
                newNode.pathCost = node.pathCost + 1
                temp = stateOfNode[x][y + j]
                stateOfNode[x][y + j] = stateOfNode[x][y]
                stateOfNode[x][y] = temp
                newNode.state = stateOfNode
                stateOfNode = deepcopy(node.state)
                fringe.put(newNode)
    return fringe

initialNode = Node()

easy = [['1','3','4'],
        ['8','6','2'],
        ['7',' ','5']]
medium = [['2','8','1'],
          [' ','4','3'],
          ['7','6','5']]
hard = [['2','8','1'],
        ['4','6','3'],
        [' ','7','5']]
goalState = [['1','2','3'],
             ['8',' ','4'],
             ['7','6','5']]


initialNode.state = easy
solution = Search(initialNode,goalState)
count = 0
print("Easy : ")
for sol in solution:
    count += 1
    if count != 1:
        print(sol.state)

print("Meduim : ")
initialNode.state = medium
solution = Search(initialNode,goalState)
count = 0
for sol in solution:
    if count != 1:
        print(sol.state)

print("Hard : ")
initialNode.state = hard
solution = Search(initialNode,goalState)
count = 0
for sol in solution:
    count += 1
    if count != 1:
        print(sol.state)
