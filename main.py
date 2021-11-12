from Customer import *
from Path import *
import random
import time
import datetime

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    i = 0
    # empty shop list
    shop = []

# loop for customer entering the shop
while i < 2:

    cart = random.sample(Customer.customers, 1)
    print('Customer ID: ' + str(cart))
    shop.append(cart)

    now = datetime.datetime.now()
    datetime1 = now.strftime("%H:%M:%S:%f %p")
    print("Customer with cart id {}, entered at {}".format(cart[0], datetime1))
    selectedPath = random.sample(Path.path, 1)
    cust = Customer(selectedPath)
    print("And the selected path is {}".format(selectedPath))

    for k in selectedPath:
        cust.move()

    # time.sleep(4)
    i += 1
    time.sleep(random.randrange(0, 5))
    print("Customer with cart id {} is at the checkout, at time {}".format(
        shop[0], datetime1))
    print(" ")
    shop.pop(0)
