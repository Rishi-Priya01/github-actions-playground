from behave import given, when, then

@given("I launch the mobile app")
def step_launch_app(context):
    # Here you can add Appium commands later
    print("Launching the mobile app...")

@when("I enter valid credentials")
def step_enter_credentials(context):
    # Simulate entering username/password
    print("Entering valid credentials...")

@then("I should see the home screen")
def step_see_home(context):
    # Simulate checking home screen
    print("Checking home screen is displayed...")
