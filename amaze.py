#random maze generator
#source code: http://stackoverflow.com/questions/27017164/python-maze-generator-explanation

from random import shuffle, randrange
def make_maze(n):
    w = n * 2
    h = n
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["+ "] * w + ['+'] for _ in range(h)] + [[]]
    hor = [["++"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+ "
            if yy == y: ver[y][max(x, xx)] = "  "
            walk(xx, yy)

    walk(randrange(w), randrange(h))
    maze = ""
    for (a, b) in zip(hor, ver):
        maze = maze + (''.join(a + ['\n'] + b)) +"\n"


    #convert the visual maze into a list of indices where the consecutive numbers indicate places where there are walls
    maze_values = list(maze)
    maze_array = []
    count = 0
    for x in maze_values:
        if x == "+":
            maze_array.append(count)
        count = count + 1

    #return dictionary containing the maze array and the intial size of the maze
    response = {"data":  maze_array,
                "size": n}
    return response
    
make_maze(8)
