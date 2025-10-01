import requests
from behave import given, then, when
from utilities.configreader import read_config
from resources_payload.resources import APIPaths
from resources_payload import payload

# We will import pytest fixtures via behave’s context if needed, or we can
# use environment vars. For simplicity, I’ll assume using environment var or global.



@when('I request latest EOD data for symbol "{symbols}"')
def step_request_latest(context, symbols):
    context.access_key = read_config("API", "API_key")
    url = read_config("API", "endpoint") + APIPaths.eod_data + "?access_key=" + context.access_key
    print("URL of the API request: ", url)
    params = payload.eod_data(symbols)
    print("Parameters of the API request: ", params)
    resp = requests.get(url, params=params)
    context.response = resp          # Response object
    context.json = resp.json()

@then('the response status code should be {status_code}')
def step_impl(context, status_code):
    actual = context.response.status_code
    expected = int(status_code)
    assert actual == expected, f"Expected {expected}, got {actual}"



@then('the JSON response should contain keys "{key1}" and "{key2}"')
def step_contain_keys(context, key1, key2):
    j = context.json
    
    assert key1 in j, f"JSON missing key {key1}"
    assert key2 in j, f"JSON missing key {key2}"

@then('the "close" price in the returned record should be numeric')
def step_close_numeric(context):
    data = context.json["data"][0]["close"]
    print("Data received for the close price: ", data)
    # data might be list or object depending on API; assume list
    assert (type(data) is float) or (type(data) is int), f"Close price is not numeric: {data}"
    

@then('the "symbol" in the returned record should match "{symbol}"')
def step_symbol_match(context, symbol):
    data = context.json["data"]
    
    resp_sym = data[0]["symbol"]
    print("Symbol received in response: ", resp_sym)
    
    assert resp_sym == symbol, f"Expected symbol {symbol}, got {resp_sym}"
