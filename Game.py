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
    for xDirection in range(2):
      for yDirection in range(2):
        if xDirection==0 and yDirection==0:
          continue
        count=1
        distance=0
        x=lastMoveX
        y=lastMoveY
        direction=1#switches to -1 when edge reached
        while True:
          x+=xDirection*direction
          y+=yDirection*direction
          distance+=1
          if x>=self.length or x<0:
            if direction==-1:
              #no more switching
              break 
            else:
              #switch direction
              direction=-1
              x=lastMoveX
              y=lastMoveY
              distance=0
          if y>=self.height or y<0:
            if direction==-1:
              break
            else:
              #switch direction
              direction=-1
              x=lastMoveX
              y=lastMoveY
              distance=0
          if distance==self.target:
            if direction==-1:
              break
            else:
              #switch direction
              direction=-1
              x=lastMoveX
              y=lastMoveY
              distance=0

          #no we have our position, check it
          if self.currentBoardState[self.getKey(x,y)]==lastPlayerToMove:
            count+=1
          else:
            if direction==-1:
              break
            else:
              #switch direction
              direction=-1
              x=lastMoveX
              y=lastMoveY
              distance=0

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

