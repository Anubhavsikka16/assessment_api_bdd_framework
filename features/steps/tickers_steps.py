import requests
from behave import given, then

from utilities.configreader import read_config
from resources_payload.resources import APIPaths
from resources_payload import payload


@then("I request a tickers list with limit {limit}")
def step_request_tickers(context, limit):
    context.limit = int(limit)
    context.access_key = read_config("API", "API_key")
    url = read_config("API", "endpoint") + APIPaths.tickers + "?access_key=" + context.access_key
    print("URL of the API request: ", url)
    params = payload.tickers_list(limit)
    print("Parameters of the API request: ", params)
    resp = requests.get(url, params=params)
    context.response = resp     
    context.json = resp.json()
    
@then("the status code should be {status_code}")
def step_check_status_code(context, status_code):
    expected = int(status_code)
    actual = context.response.status_code
    assert actual == expected, f"Expected {expected}, got {actual}"

@then("exactly {limit} ticker records should be returned")
def step_exact_limit(context, limit):
    data = context.json["data"]
    expected = int(limit)
    actual = len(data)
    print(f"Number of ticker records returned: {actual}")
    assert actual == expected, f"Expected {expected}, got {actual}"

@then("each ticker record should have non-empty \"ticker\", \"name\"")
def step_tickers_fields(context):
    data= context.json["data"]
    for rec in data:
        assert rec["ticker"], f"Missing or empty ticker in {rec}"
        assert rec["name"], f"Missing or empty name in {rec}"
        
@then('the JSON response should contain the key "data"')
def step_check_json_key(context):
    assert "data" in context.json, "Key 'data' not found in response"
