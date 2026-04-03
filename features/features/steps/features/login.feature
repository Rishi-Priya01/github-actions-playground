Feature: Mobile Login

  Scenario: Successful login
    Given I launch the mobile app
    When I enter valid credentials
    Then I should see the home screen
