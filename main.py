from Customer import *
from Path import *
from Reciver import *
import random
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    i = 0
    # empty shop list
    shop = []

# loop for customer entering the shop
while i < 1:
    # GET TWO CART FOR TWO CUSTOMER ENTERING
    cart = random.sample(Customer.customers, 2)
    # print('Customer ID: ' + str(cart[0]))
    # print('Customer ID: ' + str(cart[1]))

    # ADD CART IN THE SHOP
    shop.append(cart[0])
    shop.append(cart[1])
    print("Customer with cart id {}, entered at {}".format(cart[0], timeNow()))
    print("Customer with cart id {}, entered at {}".format(cart[1], timeNow()))

    selPath0 = random.sample(Path.path, 1)
    selPath1 = random.sample(Path.path, 1)

    # Assign path to the customer
    cust0 = Customer(selPath0)
    cust1 = Customer(selPath1)

    print("Customer of id {} has path {}".format(cart[0], selPath0))
    print("Customer of id {} has path {}".format(cart[1], selPath1))

    if len(selPath0) > len(selPath1):
        max = len(selPath0)
    else:
        max = len(selPath1)

    a = 0
    while a < max:
        cust0.move()
        cust1.move()
        a += 1

    # AFTER THE END OF LOOP THE CUSTOMER GOES TO CHECK OUT
    time.sleep(random.randrange(0, 7))
    print("Customer with cart id {} is at the checkout, at time {}".format(
        shop[0], timeNow()))
    time.sleep(random.randrange(0, 5))
    print("Customer with cart id {} is at the checkout, at time {}".format(
        shop[1], timeNow()))

    shop.pop(0)
    print(" ")

    i += 1
