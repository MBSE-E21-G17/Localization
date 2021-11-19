from Customer import *
from Path import *
import random
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = 0
    # empty shop list
    shop = []

# loop for customer entering the shop in certain time in seconds
while a <= 1:
    # print(path)
    for i in Customer.customers:
        selectPath = random.sample(Path.paths, 1)
        path = Customer(selectPath)
        Customer.move(path, i)
    # cust[i].move(Path.path_1)
    # print("Customer with cart id {} is at the checkout, at time {}".format(
    # cust[i], timeNow()))
    print(" ")
    a += 1

    # GET TWO CART FOR TWO CUSTOMER ENTERING
    # cart = random.sample(Customer.customers, 2)
    # print('Customer ID: ' + str(cart[0]))
    # print('Customer ID: ' + str(cart[1]))

    # ADD CART IN THE SHOP
    # shop.append(cart[0])
    # shop.append(cart[1])
    # print("Customer with cart id {}, entered at {}".format(cart[0], timeNow()))
    # print("Customer with cart id {}, entered at {}".format(cart[1], timeNow()))

    # selPath0 = random.sample(Path.path, 1)
    # selPath1 = random.sample(Path.path, 1)

    # Assign path to the customer

    # cust1 = Customer(selPath1)

    # print("Customer of id {} has path {}".format(cart[0], selPath0))
    # print("Customer of id {} has path {}".format(cart[1], selPath1))

    # if len(selPath0) > len(selPath1):
    #     max = len(selPath0)
    # else:
    #     max = len(selPath1)

    # a = 0
    # while a < max:
    #     cust0.move()
    #     cust1.move()
    #     a += 1

    # AFTER THE END OF LOOP THE CUSTOMER GOES TO CHECK OUT
    # time.sleep(random.randrange(0, 7))

    # time.sleep(random.randrange(0, 5))
    # print("Customer with cart id {} is at the checkout, at time {}".format(
    # shop[1], timeNow()))

    # shop.pop(0)
