Feature: Exchanges API

Background: 
    Given I have the valid access key

  Scenario Outline: Fetch exchanges list and validate content
    Then I request the exchanges list
    Then verify the response <status_code>
    And the JSON response should contain key "data"
    And at least one exchange should have non-empty "mic" and "name"
    And the response should contain a valid pagination object
    Examples:
    |status_code|
    |200        |

