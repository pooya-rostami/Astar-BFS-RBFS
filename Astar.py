from copy import copy, deepcopy
import time


class Node:
    def __init__(self):
        self.parent = None
        self.state = None
        self.pathCost = 0
        self.depth = 0
        self.heuristic = 0


def Search(initialNode, goalState):
    numberOfNode = 0
    javab = [Node()]
    fringe = [Node()]
    fringe.insert(0,initialNode)
    while not fringe == []:
        numberOfNode += 1
        node = RemoveFrom(fringe)
        if node.state == goalState:
            while node:
                javab.append(node)
                node = node.parent
            break
        fringe = AStar(node, fringe)
    print("number of node opened:{}".format(numberOfNode))
    return javab


def RemoveFrom(fringe):
    tempNode = Node()
    min = float('inf')
    for fringeNode in fringe:
        if (fringeNode.heuristic + fringeNode.pathCost) < min and fringeNode.state:
            min = fringeNode.heuristic + fringeNode.pathCost
            tempNode = fringeNode
    fringe.remove(tempNode)
    return tempNode


def AStar(node, fringe):
    nodeState = [row[:] for row in node.state]
    x = 0
    y = 0
    for i in range(len(nodeState)):
        for j in range(len(nodeState[i])):
            if nodeState[i][j] == ' ':
                x = i
                y = j
    for i in range(-1, 2):
        if i != 0:
            if x + i >= 0 and x + i <= 2:
                nextNode = Node()
                nextNode.parent = node
                nextNode.depth = node.depth + 1
                nextNode.pathCost = node.pathCost + 1
                temp = nodeState[x + i][y]
                nodeState[x + i][y] = nodeState[x][y]
                nodeState[x][y] = temp
                nextNode.state = nodeState
                nextNode.heuristic = Heuristic(nextNode.state, goalState)
                nodeState = deepcopy(node.state)
                fringe.insert(0,nextNode)
    for j in range(-1, 2):
        if j != 0:
            if y + j <= 2 and y + j >= 0 :
                nextNode = Node()
                nextNode.parent = node
                nextNode.depth = node.depth + 1
                nextNode.pathCost = node.pathCost + 1
                temp = nodeState[x][y + j]
                nodeState[x][y + j] = nodeState[x][y]
                nodeState[x][y] = temp
                nextNode.state = nodeState
                nextNode.heuristic = Heuristic(nextNode.state, goalState)
                nodeState = deepcopy(node.state)
                fringe.insert(0,nextNode)
    return fringe


def Heuristic(state, goalState):
    heuristic=0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goalState[i][j] and state[i][j] != ' ':
                if state[i][j] == '1':
                    heuristic += ((abs(i - 0)) + (abs(j - 0)))
                if state[i][j] == '2':
                    heuristic += ((abs(i - 0)) + (abs(j - 1)))
                if state[i][j] == '3':
                    heuristic += ((abs(i - 0)) + (abs(j - 2)))
                if state[i][j] == '4':
                    heuristic += ((abs(i - 1)) + (abs(j - 2)))
                if state[i][j] == '5':
                    heuristic += ((abs(i - 2)) + (abs(j - 2)))
                if state[i][j] == '6':
                    heuristic += ((abs(i - 2)) + (abs(j - 1)))
                if state[i][j] == '7':
                    heuristic += ((abs(i - 2)) + (abs(j - 0)))
                if state[i][j] == '8':
                    heuristic += ((abs(i - 1)) + (abs(j - 0)))
    return heuristic


initialNode=Node();

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

initialNode.heuristic = Heuristic(initialNode.state, goalState)
solution = Search(initialNode,goalState)

print("Easy : ")
count = 0
for sol in solution:
    # for i in sol.state:
    count += 1
    if count != 1:
        print(sol.state)

count = 0
print("Meduim : ")
initialNode.state = medium

initialNode.heuristic = Heuristic(initialNode.state, goalState)
solution = Search(initialNode,goalState)

for sol in solution:
    count += 1
    if count != 1:
        print(sol.state)

count = 0
print("Hard : ")
initialNode.state = hard

initialNode.heuristic = Heuristic(initialNode.state, goalState)
solution = Search(initialNode,goalState)

for sol in solution:
    count += 1
    if count != 1:
        print(sol.state)

