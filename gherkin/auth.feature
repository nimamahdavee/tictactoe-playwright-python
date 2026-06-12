Feature: Authentication
  In order to use the application
  As a player
  I want to create an account, log in, and log out

  Scenario: Create account for user nima
    Given the user opens the application
    When the user enters the name "nima"
    And clicks the "Create Account" button
    Then the game screen should be displayed
    And the greeting for user "nima" should be visible

  Scenario: Log out after successful access
    Given the user is on the game screen as "nima"
    When the user clicks the "Log Out" button
    Then the authentication screen should be displayed
