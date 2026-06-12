Feature: History
  Scenario: Open history page
    Given the user is on the game screen as "nima"
    When the user opens the history tab
    Then the history screen should be visible
