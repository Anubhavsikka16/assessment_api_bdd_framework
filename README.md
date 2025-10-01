# assessment_api_bdd_framework
Assessment Test
API: https://marketstack.com/documentation_v2
API key: a83a0773b6f49bb8371d7e224323156e

Screenshot of all 4 API runs on the local machine: 

<img width="1440" height="900" alt="Screenshot 2025-10-01 at 7 06 42 PM" src="https://github.com/user-attachments/assets/33f70346-a37d-47ee-86d1-73cb2eb25194" />



A BDD automated framework is implemented using Behave for API: https://marketstack.com/documentation_v2: 

| API               | Description                               |
|-------------------|-------------------------------------------|
| End-of-Day Data   | Fetches EOD for stock tickers             | 
| Historical Data   | Obtains historical data between timelines | 
| Exchanges         | Fetches stock exhanges information        | 
| Tickers List      | Fetches full list of supported tickers    | 

Descriptions of Validations: 

## API Validations – Marketstack EOD Endpoint

| **Validation**          | **What it Does**  | **Why it’s Important** |
|--------------------------|------------------|-------------------------|
| **Status Code Check**   | Ensures the API returns the expected HTTP status code | Confirms request was successful and no error (e.g., 401, 404) occurred. |
| **Key Presence Check**  | Verifies that important JSON keys (`data`, `pagination`) are present. | Ensures the response follows the expected schema for reliable parsing. |
| **Close Price Numeric** | Checks that the `"close"` price field is numeric (`int` or `float`). | Guarantees data can be used in calculations (no invalid strings or nulls). |
| **Symbol Match**        | Validates the `"symbol"` in the response matches the requested symbol (e.g., `AAPL`). | Ensures business correctness — response data matches the query.|

## API Validations – Marketstack Historical EOD Endpoint

| **Validation**                | **What it Does** | **Why it’s Important** |
|--------------------------------|------------------|-------------------------|
| **Status Code Check**          | Confirms the API response returns `200 OK`. | Ensures the request was successful and no server or auth error occurred. |
| **Date Range Validation**      | Verifies that every record’s `date` field lies between the requested `start` and `end` dates. | Guarantees the API respects query parameters and returns correct historical range. |
| **Price Fields Numeric**       | Checks that each record’s `open`, `high`, `low`, `close` values are numeric (`int` or `float`). | Ensures financial data is valid for calculations and analysis (no strings/nulls). |
| **Symbol Match**               | Validates the symbol sent in API query matches the API response| Ensure correct symbol is received and matches one sent in API request |

## API Validations – Marketstack Exchanges Endpoint

| **Validation**              | **What it Does**     | **Why it’s Important**|
| ----------------------------| ---------------------|-----------------------|
| **1. Response Status Code**                                 |  Ensures the API returns the expected status code (`200 OK`).           | Confirms that the request was successful and the server responded correctly.|
| **2. JSON Response Contains `data` Key**                    | Verifies that the response includes the top-level key `data`            | Ensures the API is structured as documented and the actual exchange data is accessible.|
| **3. Non-Empty `mic` and `name` in at Least One Exchange**  | Checks that at least one exchange record has valid values for `mic` (Market Identifier Code) and `name`.| Validates the usefulness of the response and ensures exchange records are not empty or malformed.  |
| **4. Pagination Object Validation**                         | Ensures `pagination` contains required fields (`limit`, `offset`, `count`, `total`) and they are integers. | Confirms that large datasets can be navigated correctly |

## API VALIDATIONS - MarketStack Ticker Lists Endpoint

| **Validation**                         |**What it Does**                                                                     | **Why it’s Important**                                |
| -------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------
| **1. Response Status Code**            | Checks that the API returns the expected status code (e.g., `200 OK`).              | Confirms the API request was successful and the server responded correctly.                     |
| **2. Exact Limit of Records Returned** | Validates that the number of ticker records returned matches the requested `limit`. | Ensures the API respects query parameters and returns the correct amount of data.               |
| **3. Non-Empty `ticker` Field**        | Verifies that each record contains a non-empty `ticker` value.                      | Guarantees that each record can be uniquely identified by its ticker symbol.                    |
| **4. Non-Empty `name` Field**          | Ensures that each ticker record has a valid `name` value.                           | Confirms that ticker records provide meaningful and readable information, not just identifiers. |
| **JSON Response Contains `data` Key** | Verifies that the top-level key `data` exists in the response. | Ensures that the API response structure is valid and that the actual ticker records are accessible for further validations. |




