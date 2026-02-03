# Ultimate Tic-Tac-Toe

- square
  - one to many parent square
  - many to many symbol inside
  - many to one children square (nullable)

- game
  - one to many square
  - player x unique id
  - player o unique id
  - state ordered (Win Lose Draw In Progress)

\*\* player
many to one game

- square collection
  -
