from Game import Game
from copy import deepcopy

def minimax(gameState,depth,a,b,player,visited):
    gameString=gameState.__str__()
    if gameString in visited.keys():
        return visited[gameString]
    length=12
    if depth==0:
        visited[gameString]=0
        return 0#estimation
    if gameState.winningPlayer!=0:
        visited[gameString]=500*gameState.winningPlayer
        return 500*gameState.winningPlayer
    children=[]
    if player==1:
        for i in range(length):
            newState=deepcopy(gameState)
            placed,win=newState.makeMove(player,i)
            if not placed:
                continue
            else:
                value=minimax(newState,depth-1,a,b,player*-1,visited)
                if value>=b:
                    break
                a=max(a,value)
                children.append(value)
    else:#player==-1
        for i in range(length):
            newState=deepcopy(gameState)
            placed,win=newState.makeMove(player,i)
            if not placed:
                continue
            else:
                value=minimax(newState,depth-1,a,b,player*-1,visited)
                if value<=a:
                    break
                b=min(b,value)
                children.append(value)
    if len(children)==0:
        visited[gameString]=99999*-1*player
        return(99999*-1*player)
    if player==-1:
        visited[gameString]=max(children)
        return(max(children))
    else:
        visited[gameString]=max(children)
        return(min(children))

