# Rate of Growth (exponential).
# The following must be satisfied while solving the problem.

#  Assuming we have the following:
    # -3 disks.
    # -3 towers.

# 1. Only one disc can be moved at any given time.
# 2. Only the top most disc can be moved at any given time.
# 3. Disc must be placed in ascending order where discs are placed from the largest to the smallest with the largest sitting a the very bottom and the smallest at the top.
# 4. The larger disc cannot be placed on top of a smaller disk.


def Hanoi(n, tower_b, tower_e, tower_m):
    if n == 1:
        print("Move disk 1 from tower", tower_b, "to tower" , tower_e)
        return
    Hanoi(n-1, tower_b, tower_m, tower_e)
    print("Move disk ", n , "from tower", tower_b, "to tower", tower_e)
    Hanoi(n-1, tower_m, tower_e, tower_b)
    
n = 3
Hanoi(n, 'A', 'C', 'B')
# name of towers = A, C, B

    
        
        
# n = total number of disks
# tower_b = begining tower (source or start)
# tower_e + end tower (destination or stop)
# tower_m = middle tower (intermediate)