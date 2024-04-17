import time
from behave import given
from utils.urlBuilder import build_url

@given('I launch the URL')
def launch_url(context):

    url = build_url()
    # Navigate to the URL
    context.driver.get(url)

    #Sleep
    time.sleep(5)
