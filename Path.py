import matplotlib.pyplot as plt
import numpy as np
import random
import math

from parameters import *


class Path:
    def __init__(self):
        self.path = self._CreateRandomPath()

    def _CreateRandomPath(self, startAtEntrance=False):

        def _OutOfBounds(x, y):
            if x < 0 or x > (S_XMAX / S_R) or y < 0 or y > (S_YMAX / S_R):
                return True;
            else:
                return False;

        x = [];
        y = [];
        direction = [];
        dirPrev = [];
        dirXPrev = [];
        dirYPrev = [];
        path = [];

        if (startAtEntrance == True):
            x.append(S_XE / S_R);
            y.append(S_YE / S_R);
            dirPrev.append(0);
            dirXPrev.append(0);
            dirYPrev.append(1);
            path.append((x[0], y[0]));
        else:
            x.append(random.uniform(0.05 * S_XMAX, 0.95 * S_XMAX) / S_R);
            y.append(random.uniform(0.05 * S_YMAX, 0.95 * S_YMAX) / S_R);
            dirPrev.append(random.uniform(P_DirMin, P_DirMax));
            dirXPrev.append(math.sin(dirPrev[0]));
            dirYPrev.append(math.cos(dirPrev[0]));
            path.append((x[0], y[0]));

        random.seed();
        v = random.uniform(P_SMin, P_SMax) / np.sqrt(2) * P_R / S_R;

        for i in range(P_Length - 1):

            # if out of bounds
            if _OutOfBounds(x[i] + dirXPrev[i] * v, y[i] + dirYPrev[i] * v):
                while _OutOfBounds(x[i] + dirXPrev[i] * v, y[i] + dirYPrev[i] * v):
                    # fix direction
                    direction = random.uniform(P_DirMin, P_DirMax);
                    dirPrev[i] = direction;
                    dirXPrev[i] = math.sin(direction);
                    dirYPrev[i] = math.cos(direction);

                # memory update
                dirPrev.append(dirPrev[i]);
                dirXPrev.append(dirXPrev[i]);
                dirYPrev.append(dirYPrev[i]);

            # if it is a time to change direction           
            elif i % P_Hold == 0:
                # change direction in respect to the last one
                direction = dirPrev[i] + P_DirChangeFact * random.uniform(P_DirMin, P_DirMax);

                # memory update
                dirPrev.append(direction);
                dirXPrev.append(math.sin(direction));
                dirYPrev.append(math.cos(direction));

            else:
                # memory update
                dirPrev.append(dirPrev[i]);
                dirXPrev.append(dirXPrev[i]);
                dirYPrev.append(dirYPrev[i]);

            x.append(x[i] + dirXPrev[i] * v);
            y.append(y[i] + dirYPrev[i] * v);
            path.append((x[i] + dirXPrev[i] * v, y[i] + dirYPrev[i] * v));

            v = random.uniform(P_SMin, P_SMax) / np.sqrt(2) * P_R / S_R;
            # print(np.array(path).reshape(-1,2).T *S_R)
        # return np.array(path).reshape(-1,2).T * S_R
        return self._scale_path(path)

    def _scale_path(self, path):
        tmp = []
        for pos in path:
            tmp.append((pos[0] * S_R, pos[1] * S_R))
        return tmp

    # def ShowPath(self):
    #     plt.figure(dpi=1200);
    #     plt.plot(self.path[0, :], self.path[1, :])
    #     plt.axis([0, S_XMAX, 0, S_YMAX]);
    #     plt.show()
