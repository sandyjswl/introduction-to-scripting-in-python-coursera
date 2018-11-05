"""
Demonstration of else and elif.
"""

def greet(friend, money):
    """
    Greet people.  Say hi if they are your friend.  Give them
    $20 if they are your friend and you have enough money.  Steal
    $10 from them if they are not your friend.
    """
    if friend and (money > 20):
        print("Hi!")
        money = money - 20
    elif friend:
        print("Hello")
    else:
        print("Ha ha!")
        money = money + 10
    return money


money = 15

money = greet(True, money)
print("Money:", money)
print()

money = greet(False, money)
print("Money:", money)
print()

money = greet(True, money)
print("Money:", money)
print()
