Feature: Profile
  Scenario: Open profile page
    Given the user is on the game screen as "nima"
    When the user opens the profile tab
    Then the profile screen should be visible
