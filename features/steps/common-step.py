import time
from behave import given
from utils.urlBuilder import build_url

@given('I launch the URL')
def launch_url(context):

    url = build_url()
    context.driver.get(url)
    time.sleep(5)
