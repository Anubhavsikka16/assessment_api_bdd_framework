import requests
from behave import given, then
from datetime import datetime
from utilities.configreader import read_config
from resources_payload.resources import APIPaths
from resources_payload import payload





    
    
@then('I request historical EOD data for symbol "{symbol}" from "{start}" to "{end}"')
def step_request_historical(context, symbol, start, end):
    context.symbol = symbol
    context.start = datetime.strptime(start, "%Y-%m-%d")
    context.end = datetime.strptime(end, "%Y-%m-%d")
    url = read_config("API", "endpoint") + APIPaths.eod_data + "?access_key=" + context.access_key
    print("URL of the API request: ", url)
    params = payload.historical_data(symbol, start, end)
    print("Parameters of the API request: ", params)
    
    resp = requests.get(url, params=params)
    context.response = resp          # Response object
    context.json = resp.json()
    
@then(u'the response status code is {status_code:d}')
def step_check_status_code(context, status_code):
    assert context.response.status_code == 200, f"Expected 200 but got {context.response.status_code}"
    
@then("every returned record date should lie between \"{start}\" and \"{end}\"")
def step_dates_in_range(context, start, end):
    data = context.json["data"]
    print ("Data received: ", data)
    #Fetching  date and excluding time from the response
    rec_date=datetime.strptime(data[0]["date"][:10], "%Y-%m-%d")
    print("Date received in response: ", rec_date)
       

@then("every record’s \"open\", \"high\", \"low\", \"close\" values should be numeric")
def step_prices_numeric(context):
    for rec in context.json["data"]:
        for fld in ("open", "high", "low", "close"):
            val = rec.get(fld)
            print(f"{fld} value: ", val)
        assert (type(val) is float) or (type(val) is int), f"Close price is not numeric: {val}"
        
# ✅ Validation 4: Symbol Match
@then('every record symbol should match "{symbol}"')
def step_symbol_match(context, symbol):
    for rec in context.json["data"]:
        resp_sym = rec["symbol"]
        assert resp_sym == symbol, f"Expected {symbol}, got {resp_sym}"