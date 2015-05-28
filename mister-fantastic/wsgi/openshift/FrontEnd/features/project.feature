Feature: project

  Scenario: misterF
    Given I am a visitor
    When I visit url "http://localhost:8081/"
    Then page url "http://localhost:8081/#/login"

  Scenario: project
    Given I am a visitor
    When I visit url "http://localhost:8081/#/login"
      And fill in fields
    Then page url "http://localhost:8081/#/project"
      And page have "Information about project"

  Scenario: project_project
    Given I am a visitor
      And I visit url "http://localhost:8081/#/login"
      And fill in fields
    When click on "#/project"
    Then page url "http://localhost:8081/#/project"
      And page have "Information about project"

  Scenario: project_team
    Given I am a visitor
      And I visit url "http://localhost:8081/#/login"
      And fill in fields
    When click on "#/team"
    Then page url "http://localhost:8081/#/team"
      And there id team

  Scenario: project_programmer
    Given I am a visitor
      And I visit url "http://localhost:8081/#/login"
      And fill in fields
    When click on "#/programmer"
    Then page url "http://localhost:8081/#/programmer"
      And there id programmer


  Scenario: language
    Given I am a visitor
    When I visit url "http://localhost:8081/"
    And click on language
    Then there is a text "Statistics..."

  Scenario: The Good Guys
    Given I am a visitor
    When I visit url "http://localhost:8081/"
    Then there is a href Good Guys


  Scenario: team_team
    Given I am a visitor
      And I visit url "http://localhost:8081/#/login"
      And fill in fields
      And click on "#/team"
    When click on "#/team"
    Then page url "http://localhost:8081/#/team"
      And there id team

  Scenario: team_project
    Given I am a visitor
      And I visit url "http://localhost:8081/#/login"
      And fill in fields
      And click on "#/team"
    When click on "#/project"
    Then page url "http://localhost:8081/#/project"
      And page have "Information about project"


  Scenario: team_programmer
    Given I am a visitor
      And I visit url "http://localhost:8081/#/login"
      And fill in fields
      And click on "#/team"
    When click on "#/programmer"
    Then page url "http://localhost:8081/#/programmer"
      And there id programmer


  Scenario: programmer_programmer
    Given I am a visitor
      And I visit url "http://localhost:8081/#/login"
      And fill in fields
      And click on "#/programmer"
    When click on "#/programmer"
    Then page url "http://localhost:8081/#/programmer"
      And there id programmer

  Scenario: programmer_project
    Given I am a visitor
      And I visit url "http://localhost:8081/#/login"
      And fill in fields
      And click on "#/programmer"
    When click on "#/project"
    Then page url "http://localhost:8081/#/project"
      And page have "Information about project"

    Scenario: programmer_team
    Given I am a visitor
      And I visit url "http://localhost:8081/#/login"
      And fill in fields
      And click on "#/programmer"
    When click on "#/team"
    Then page url "http://localhost:8081/#/team"
      And there id team