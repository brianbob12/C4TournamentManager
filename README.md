# C4TournamentManager

## Rules
- Your program can only be running during your turn
  - thraeding allowed but must stop when the program submits its move
- No connection to any outside program
  - No API calls and no acess to non-submitted material
- program size limit of 50GB
- Your program can use no more than 4GB of system memory(RAM) at a time
  - You can hold the RAM between turns
- Your program can use no more than 4GB of grpahics memory(GRAM) at a time
- 1 second time limit per move

## Points system
- \+ 500pts per win
- \- 500pts per loss
-   0pts per draw
- \- 5pnts per second over time limt for each move
  - This is charged in increments of 0.005pnts per millisecond
  - No points awarded for sumbitting a move early
  - If a move is submitted early, no extra time is creditied for other moves
