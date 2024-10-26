from behave import given

@given('a list of products')
def step_impl(context):
    context.products = [{"name": "Product1", "category": "Category1", "price": 10, "available": True}]
