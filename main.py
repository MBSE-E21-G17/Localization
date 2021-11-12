from Customer import *
from Path import *
import random
import datetime
import time


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    i = 0
    # empty shop list
    shop = []
    # Calling object of Customer class
    customer = Customer()
    # Calling object of Path class
    paths = Path()

# loop for customer entering the shop
while i < 5:

    cart = random.sample(customer.customers, 1)
    print('Customer ID: ' + str(cart))
    shop.append(cart)
    # print("Carts inside shop : {}".format(shop[i]))
    now = datetime.datetime.now()
    datetime1 = now.strftime("%H:%M:%S:%f %p")
    print("Customer with cart id {}, entered at {}".format(cart[0], datetime1))
    # for j in range(5):
    selectPath = random.sample(paths.path, 1)
    for k in selectPath:
        for y in k:
            # selectPath = random.choice(paths.path[random.randrange(0, len(paths.path))])
            # shop.append(cart)
            time.sleep(random.randrange(0, 5))
            now = datetime.datetime.now()
            datetime1 = now.strftime("%H:%M:%S:%f %p")
            # print("===========")
            print("Selected path is : {}, at time {}".format(y, datetime1))
            # print("===========")
    time.sleep(4)
    i += 1

# while len(shop) > 0:
    time.sleep(random.randrange(0, 5))
    now = datetime.datetime.now()
    datetime1 = now.strftime("%H:%M:%S:%f %p")
    print("Customer with cart id {} is at the checkout, at time {}".format(
        shop[0], datetime1))
    print(" ")
    shop.pop(0)
