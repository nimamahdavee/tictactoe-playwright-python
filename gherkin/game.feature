Feature: Game board
  In order to play Tic-Tac-Toe
  As a signed in user
  I want to interact with the game board and actions

  Scenario: Make one valid move
    Given the user is on the game screen as "nima"
    When the user clicks an empty board cell
    Then the selected cell should contain a valid mark

  Scenario: Start a new game
    Given the user is on the game screen as "nima"
    When the user clicks the "New Game" button
    Then the board should be empty

  Scenario: Reset the board
    Given the user is on the game screen as "nima"
    When the user clicks the "Reset" button
    Then the board should be empty
