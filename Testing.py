#%%
from Game import *

#%%
myGame=Game()
myGame.setOnWin(lambda player:print(player,"Wins!!!!\nYay!\nCelebrate!"))
#%%
player=1
while True:
  print(myGame)
  print("player"+str(player)+"'s move")
  myGame.makeMove(player,int(input("enter column:")))
  player*=-1
# %%

