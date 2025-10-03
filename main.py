from pyscript import document


def createOrder(e):
    # User's name
    fname = document.getElementById('name').value
    # User's home address
    address = document.getElementById('address').value
    # User's phone number
    number = document.getElementById('number').value

    #  Set prices to each menu item
    prices = {
        'salmonCheese': 90,
        'spicyTuna': 130,
        'californiaMaki': 120,
        'eggNigiri': 160,
        'tunaSaladRoll': 140
    }

    # Start total price at 0
    total = 0

    # Check each menu item to see if it's checked
    for i, price in prices.items():
        box = document.getElementById(i)

        # If checked, add its price to total
        if box.checked:
            total = total + price

    # summary of costumer's order and total price
    order_summary = f"Order for: {fname} <br> Address: {address} <br> Contact number: {number} <br> Total:  ₱{total}"

    document.getElementById('output').innerHTML = order_summary