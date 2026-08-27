"""
logged_in = True

def profile():
    if logged_in:
        print("Welcome to your profile")
    else:
        print("first, login")

def orders():
    if logged_in:
        print("You can oder items")
    else:
        print("first, login then orders")

def setting():
    if logged_in:
        print("Change your setting, if you want")
    else:
        print("first, login then can control your setting")

profile()
orders()
setting()
"""


from functools import wraps
logged_in = True
def login_required(func):
    @wraps(func)
    def wrapper():
        if logged_in:
            func()
        else:
            print("Please login first")
    return wrapper

@login_required
def profile():
    print("Welcome to your profile")

profile()
        
