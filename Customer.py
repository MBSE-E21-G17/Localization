
class Customer:
    def __init__(self, PATH):
        self.cur_pos = PATH[0]
        self.est_pos = (0, 0)
        self.PATH = PATH
        self._path_ind = 0

    def move(self):
        if len(self.PATH) + 1 == self._path_ind:
            return
        self._path_ind += 1
        self.cur_pos = self.PATH[self._path_ind]


if __name__ == "__main__":

    PATH_1 = [(20, 650), (80, 650)]
    cust1 = Customer(PATH_1)

    for i in range(0, 100):
        cust1.move()
        print(cust1.cur_pos)
    # customers representing carts
    customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
