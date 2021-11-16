
class Customer:
    def __init__(self,cur_pos,speed,PATH):
        self.cur_pos = cur_pos
        self.speed = 1
        self.est_pos = (0,0)
        self.PATH = PATH
        self._path_ind = 0

    def move(self):
        if len(self.PATH) + 1 == self._path_ind:
            return

        if self.cur_pos == self.PATH[self._path_ind]:
            self._path_ind += 1
        
        diff = [0,0]
        diff[0] = self.cur_pos[0] - self.PATH[self._path_ind][0]
        diff[1] = self.cur_pos[1] - self.PATH[self._path_ind][1]

        if diff[0] > 0 and diff[1] > 0:
            self.cur_pos[0] =+ self.speed/2
            self.cur_pos[1] =+ self.speed/2

        elif diff[0] > 0:
            self.cur_pos[0] =+ self.speed
        
        elif diff[1] > 0:
            self.cur_pos[1] =+ self.speed



if __name__ == "__main__":
    

    PATH_1 = [(20,650),(80,650)]
    cust1 = Customer(PATH_1[0],1,PATH_1)

    for i in range(0,100):
        cust1.move()
        print(cust1.cur_pos)
    # customers representing carts
    customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
