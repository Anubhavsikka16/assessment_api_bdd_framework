import requests
from behave import given, then
from utilities.configreader import read_config
from resources_payload.resources import APIPaths
from resources_payload import payload



@then("I request the exchanges list")
def step_request_exchanges(context):
    context.access_key = read_config("API", "API_key")
    url = read_config("API", "endpoint") + APIPaths.exchanges + "?access_key=" + context.access_key
    print("URL of the API request: ", url)
    resp = requests.get(url)
    context.response = resp    
    context.json = resp.json()
    
@then(u'verify the response {status_code:d}')
def step_check_status_code(context, status_code):
    expected = int(status_code)
    actual = context.response.status_code
    assert actual == expected, f"Expected {expected}, got {actual}"

    
@then('the JSON response should contain key \"data\"')
def step_check_json_key(context):
    assert "data" in context.json, "Key 'data' not found in response"

@then("at least one exchange should have non-empty \"mic\" and \"name\"")
def step_one_valid_exchange(context):
    data = context.json["data"]
    
    for rec in data:
        assert rec["mic"], f"Missing or empty ticker in {rec}"
        assert rec["name"], f"Missing or empty name in {rec}"
        
@then('the response should contain a valid pagination object')
def step_check_pagination(context):
    
    body = context.response.json()

    pagination = body.get("pagination")
    assert pagination, "Missing 'pagination' object in response"

    required_keys = ("limit", "offset", "count", "total")
    for key in required_keys:
        assert key in pagination, f"Missing {key} in pagination object"


    assert isinstance(pagination["limit"], int), "limit must be integer"
    assert isinstance(pagination["offset"], int), "offset must be integer"
    assert isinstance(pagination["count"], int), "count must be integer"
    assert isinstance(pagination["total"], int), "total must be integer"

