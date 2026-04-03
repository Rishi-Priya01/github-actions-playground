from behave import given, when, then

@given("I launch the mobile app")
def step_launch_app(context):
    print("Launching the mobile app...")

@when("I enter valid credentials")
def step_enter_credentials(context):
    print("Entering username and password...")

@then("I should see the home screen")
def step_verify_home(context):
    print("Home screen displayed")
