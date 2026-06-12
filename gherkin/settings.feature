Feature: Settings
  Scenario: Change language
    Given the user opens the application
    When the user changes the language
    Then the interface should remain usable

  Scenario: Toggle theme
    Given the user opens the application
    When the user toggles the theme button
    Then the interface should remain usable
