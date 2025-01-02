'''
simulate the behavior of the guard

create a guard class
    direction -> queue
        peek the queue to find a new place to traverse
        if path is blocked(), pop dir from queue and add to end
    coordinates

create a map class
    methods
        blocked(coords) -> bool
        off_da_grid(coords) -> bool:
            termination condition
'''
from collections import deque

class guard:
    def __init__(self, starting):
        self.dirs = deque([0, 1, 2, 3]) # 0-> up, 1-> right 2-> down 3-> left
        self.cords = starting
        self.seen = set((starting))

    def move(self, lab: ground) -> None:
        '''
        if the dir is valid (free()), move the guard 'dir' direction
        '''

        dir = self.dirs[0]
        x, y = self.cords 

        if dir == 0 and lab.free(x + 1, y):
            self.cords = (x + 1, y)
        elif dir == 1 and lab.free(x, y + 1):
            self.cords = (x, y + 1)
        elif dir == 2 and not lab.free(x - 1, y):
            self.cords = (x - 1, y)
        elif dir == 3 and not lab.free(x, y - 1):
            self.cords = (x, y - 1)
        else:
            _ = self.dirs.pop()
            self.dirs.append(dir)
            return self.move(lab)
        
        self.seen.add(self.cords)
            
class ground:
    def __init__(self, map):
        self.map = map
        self.rows = len(map)
        self.cols = len(map[0])

    def free(self, coords: (int, int)) -> bool:
        x, y = coords
        if self.off_da_grid(coords):
            return True
        if self.map[x][y] != "#":
            return True
        return False

    def off_da_grid(self, coords):
        x, y = coords
        
        if x >= self.rows or x < 0:
            return True
        if y >= self.cols or y < 0:
            return True
        return False

# get data
g = guard()
lab = ground()
while (not lab.off_da_grid(g.cords)):
    g.move(lab)

print(len(g.seen) - 1)