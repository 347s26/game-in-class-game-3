# Ultimate Tic-Tac-Toe
- player
  - many to one game

- game # Made up of 9 squares
  - one to many square
  - player x unique id
  - player o unique id
  - state ordered (Win Lose Draw In Progress)

- square # Made up of 9 spaces
  - one to many parent square
  - many to many symbol inside
  - many to one children square (nullable)

- space # Can contain an X, an O, or nothing
  - many to one square
  - char symbol

