
from behave import given, then
from utilities.configreader import read_config

@given('I have the valid access key')
def step_impl(context):
    context.access_key = read_config("API", "API_key")
    
