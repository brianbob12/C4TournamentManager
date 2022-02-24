# 0  - empty
# 1  - player 1
#-1  - player 2

class Game:
  
  def __init__(self,length=7,height=6,target=4):
    self.length=length
    self.height=height
    self.target=target
    self.onWin=None

    #list of positions on the board
    keySet=[]

    for i in range(length):
      for j in range(height):
        keySet.append(self.getKey(i,j))

    self.keyset=tuple(keySet)

    emptyBoard={}
    for key in self.keyset:
      emptyBoard[key]=0

    self.currentBoardState=emptyBoard
    self.history=[self.currentBoardState]


  #args: player
  def setOnWin(self,onWinCallback):
    self.onWin=onWinCallback

  def getKey(self,x,y):
    return(str(x)+"-"+str(y))

  #checks if there is a winner
  #lastPlayerToMove 1 for player 1 and -1 for player 2
  #returns False if no win and True if the last player to make a move won
  def checkWin(self,lastPlayerToMove,lastMoveX,lastMoveY):
    for xDirection in range(-1,2):
      for yDirection in range(-1,2):
        if xDirection==0 and yDirection==0:
          continue
        count=1
        for i in range(1,4):
          newPosX=lastMoveX+xDirection*i
          newPosY=lastMoveY+yDirection*i
          if newPosX>=self.length or newPosX<0:
            break
          if newPosY>=self.height or newPosY<0:
            break
          if self.currentBoardState[self.getKey(newPosX,newPosY)]==lastPlayerToMove:
            count+=1
          else:
            break
        if count==4:
          return True
    return False

  #returns validMove(bool),winningMove(bool)
  def makeMove(self,player,column):
    newBoard=self.currentBoardState.copy()
    lastY=None
    placed=False
    for j in range(self.height):
      if(newBoard[self.getKey(column,j)]==0):
        newBoard[self.getKey(column,j)]=player
        lastY=j
        placed=True
        break
    if not placed:
      return False,False
    #else
    self.currentBoardState=newBoard
    self.history.append(self.currentBoardState) 
    win=self.checkWin(player,column,lastY)
    if win:
      if self.onWin!=None:
        self.onWin(player)
    return True,win


  def __str__(self):
    out="Board Object" 
    out+="\n\n"
    out+="      "
    for i in range(self.length):   
      out+=str(i)
      out+="   "
    out+="\n"

    for j in range(self.height-1,-1,-1):
      out+="  ||  "
      for i in range(self.length):
        piece=self.currentBoardState[self.getKey(i,j)]
        if piece==0:
          out+=" "
        elif piece==1:
          out+="X"
        elif piece==-1:
          out+="O"
        if i!=self.length-1:
          out+=" | "
      out+="  ||  \n"
    return out

