Feature: Tickers List API

  Background: 
    Given I have the valid access key
    

  Scenario Outline: Fetch tickers list with limit <limit>
    Then I request a tickers list with limit <limit>
    Then the status code should be <status_code>
    And exactly <limit> ticker records should be returned
    And each ticker record should have non-empty "ticker", "name"
    And the JSON response should contain the key "data"


    Examples:
      | limit | status_code |
      | 5     | 200 |
      | 10    | 200 |
