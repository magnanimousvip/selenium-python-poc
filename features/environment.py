from behave import fixture, use_fixture
from config.browser import create_driver

@fixture
def setup_driver(context):
    context.driver = create_driver()
    yield context.driver
    context.driver.quit()

def before_all(context):
    use_fixture(setup_driver, context)