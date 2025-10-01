Feature: End-of-Day latest data
  As a user of Marketstack API
  I want to retrieve the latest EOD data for a symbol
  So I can see the latest closing price, open, etc.

Background: 
    Given I have the valid access key
    

  Scenario Outline: Fetch latest EOD data for given symbol
    
    When I request latest EOD data for symbol "<symbols>"
    Then the response status code should be <status_code>
    And the JSON response should contain keys "data" and "pagination"
    And the "close" price in the returned record should be numeric
    And the "symbol" in the returned record should match "<symbols>"

    Examples:
        | symbols | status_code |
        | AAPL   | 200          |
        | MSFT   | 200          |
