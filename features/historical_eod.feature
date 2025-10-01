Feature: Historical End-of-Day Data Range

  Background: 
    Given I have the valid access key
   

  Scenario Outline: Fetch EOD data for <symbol> between dates
    
    Then I request historical EOD data for symbol "<symbol>" from "<start>" to "<end>"
    Then the response status code is <status_code>
    And the JSON response should contain keys "data" and "pagination"
    And every returned record date should lie between "<start>" and "<end>"
    And every record’s "open", "high", "low", "close" values should be numeric
    And every record symbol should match "<symbol>"

    Examples:
      | symbol | start       | end          | status_code   | 
      | AAPL   | 2025-09-20   | 2025-09-30   | 200          |
      | MSFT   | 2025-09-20   | 2025-09-30  | 200           |
