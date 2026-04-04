from behave import given, when, then

@given("I launch the mobile app")
def launch_app(context):
    print("Launching app...")

@when("I enter valid credentials")
def enter_credentials(context):
    print("Enter crendentials")

@then("I should see the home screen")
def step_verify_home(context):
    print("Home screen displayed")
