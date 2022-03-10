from Game import Game


def minimax(gameState,depth,player):
    length=12
    if depth==0:
        return 0#estimation
    if gameState.winningPlayer!=0:
        return 500*gameState.winningPlayer
    children=[]
    for i in range(length):
        newState=gameState.makeMove(player,i)
        children.append(minimax(newState,depth-1,player*-1))
    if player==-1:
        return(min(children))
    else:
        return(max(children))
