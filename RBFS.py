from copy import copy, deepcopy
import time

class Node:
    def __init__(self):
        self.parent = None
        self.state = None
        self.remember = None
        self.heuristic = 0
        self.pathCost = 0
        self.depth = 0

    def __lt__(self, other):
        return self.heuristic < other.heuristic


def Search(initialNode , goalState):
    numberOfNode = 0
    solution = []
    visited = []
    fringe = []
    fringe.insert(0,initialNode)
    while not fringe == []:
        node = RemoveFrom(fringe, visited)
        visited.insert(0,node.state)
        numberOfNode += 1
        if node.state == goalState:
            while node:
                solution.append(node)
                node = node.parent
            break
        fringe = RBFS(node, fringe, visited)
    print("number of node opened:{}".format(numberOfNode))
    return solution


def RemoveFrom(fringe, visited):
    fringe.sort()
    for item in fringe:
        if item.state in visited:
            fringe.remove(item)
    node=fringe[0]
    if len(fringe) > 1:
        if fringe[1].heuristic < node.parent.remember.heuristic :
            node.remember = fringe[1]
        else:
            node.remember = node.parent.remember
    else:
        secondChoice = Node()
        secondChoice.heuristic = float('inf')
        node.remember = secondChoice
    fringe.remove(node)
    return node


def RBFS(node, fringe, visited):
    stateOfNode = [row[:] for row in node.state]
    x = 0
    y = 0
    tempFringe = []
    for i in range(len(stateOfNode)):
        for j in range(len(stateOfNode[i])):
            if stateOfNode[i][j] == ' ':
                x = i
                y = j
    for i in range(-1, 2):
        if i != 0:
            if x + i >= 0 and x + i < 3:
                nextNode = Node()
                nextNode.parent = node
                nextNode.depth = node.depth + 1
                nextNode.pathCost = node.pathCost + 1
                temp = stateOfNode[x + i][y]
                stateOfNode[x + i][y] = stateOfNode[x][y]
                stateOfNode[x][y] = temp
                nextNode.state = stateOfNode
                nextNode.heuristic = Heuristic(nextNode.state, goalState)
                stateOfNode = deepcopy(node.state)
                tempFringe.insert(0, nextNode)
    for j in range(-1, 2):
        if j != 0:
            if y + j < 3 and y + j >= 0 :
                nextNode = Node()
                nextNode.parent = node
                nextNode.depth = node.depth + 1
                nextNode.pathCost = node.pathCost + 1
                temp = stateOfNode[x][y + j]
                stateOfNode[x][y + j] = stateOfNode[x][y]
                stateOfNode[x][y] = temp
                nextNode.state = stateOfNode
                nextNode.heuristic = Heuristic(nextNode.state, goalState)
                stateOfNode = deepcopy(node.state)
                tempFringe.insert(0, nextNode)
    flag = False
    for n in tempFringe:
        if n.heuristic < node.remember.heuristic:
            flag = True
            for m in tempFringe:
                fringe.insert(0, m)
            break
    if not flag:
        tempFringe.sort()
        node.heuristic = tempFringe[0].heuristic
        fringe.insert(0, node)
        node = RemoveFrom(fringe, visited)
        visited.insert(0, node.state)
        fringe = RBFS(node, fringe, visited)
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

initialNode.heuristic = Heuristic(initialNode.state, goalState)
solution = Search(initialNode,goalState)

count = 0
print("Easy : ")
for sol in solution:
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

