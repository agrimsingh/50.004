"""
__author__ = "Agrim Singh"
__id__ = "1000748"

"""

import maze
import mazeIO
import sys
#the deque class supports pops from both ends
from collections import deque 

###A class for solving mazes###

class MazeSolver:

    #Initializes the solver with the maze to solve
    #The maze class contains (see maze.py):
        # 1) matrix: the matrix of characters ('W', 'O', 'B', or 'E') 
        #            representing the maze
        # 2) start: the starting square as [row, column]
        # 3) end: the ending square as [row, column]
    def __init__(self, maze):

        self.maze = maze

    #Solves a maze.
    #search_type can be either DFS or BFS,
    #depending on whether you want the maze solved
    #using depth first search or breadth first search,
    #respectively.
    #
    #Returns a path through the maze as a list of [row, column]
    #squares where path[0] = maze.start and
    #path[len(path)-1] = maze.end
    #For every square i, path[i] should be adjacent to
    #path[i+1] and maze.matrix[i] should not be 'W'
    #
    #Also returns all the nodes expanded as a [row, column]
    #list.  These need not be in any particular order and
    #should include the nodes on the path.

    def solve_maze(self, search_type):
        def explore(point): #(y,x)
            #log vertices visited to list
            newly_explored = []
            if (point[1]>=1): #go left
                newly_explored.append([point[0],point[1]-1])
            if (point[1]<=self.maze.rows-2): #go right
                newly_explored.append([point[0],point[1]+1])
            if (point[0]>=1): #go up
                newly_explored.append([point[0]-1,point[1]])
            if (point[0]<=self.maze.cols-2): #go down
                newly_explored.append([point[0]+1,point[1]])
            return newly_explored
        
        #DFS recursive solution
        def search_DFS(cur, pathing):
            if (len(pathing)>0):
                pathing.insert(0,cur)
            else:
                pathing.append(cur)
            if (cur==self.maze.start):
                return pathing
            expanded.append(cur)
            newer = explore(cur)
            for node in newer:
                if (node not in expanded and self.maze.matrix[node[0]][node[1]] != "W"):
                    new_pathing = pathing[:] #shallow copy this list
                    res = search_DFS(node, new_pathing)
                    if (res!=[]):
                        return res
            return []
        
        #BFS solution
        def search_BFS(end):
            i=0
            cur = end
            pathing = [[cur]]
            while (expanded[-1] != cur or cur==end):
                cur = expanded[i]
                if (cur==self.maze.start):
                    return pathing[i]
                newer = explore(cur)
                for node in newer:
                    if (node not in expanded and self.maze.matrix[node[0]][node[1]] != "W"):
                        expanded.append(node)
                        pathing.append([]) #shallow copy path
                        for path in pathing[i]:
                            pathing[-1].append(path)
                        pathing[-1].insert(0,node)
                i+=1
            return []
        
        if (search_type != "DFS" and search_type != "BFS"):
            print "Invalid search type"
            return [], []
        
        if (self.maze.start == []):
            print "Maze does not have starting square"
            return [], []

        if (self.maze.end == []):
            print "Maze does not have ending square"
            return [], []
        
        path = []
        expanded = []

        #######################################
        ############YOUR CODE HERE#############
        #######################################
        if (search_type=="DFS"):
            path = search_DFS(self.maze.end, [])
        else:
            expanded.append(self.maze.end)
            path = search_BFS(self.maze.end)
       
        #print path

        return path, expanded

#This main function will allow you to test your maze solver
#by printing your solution to a ppm image file or ascii text file.
#
#Usage: maze_solver input_filename output_filename <image scaling>
#
#You must specify the input file name and the output file name. 
#The input should be a .ppm or .txt file in the form output by
#the mazeIO class.  See test_maze.ppm and many_paths.txt for examples.
#
#You also need to specify a search type:
#BFS: solves the maze using breadth first search
#DFS: solves the maze using depth first search
#
#For small mazes, a one-to-one
#correspondence between maze squares and pixels will be too small to see
#(ie a 10x10 maze gives an image of 10x10 pixels)
#so the ppm image is scaled when written out.  If you are trying to
#read in a scaled ppm image, you MUST specify image scaling to be
#the correct scaling or you will get a very strange looking solution.
#For example, the scaling used to print out test_maze.ppm was 6 so
#to solve test_maze.ppm using breadth first search and write it out to
#test_path.ppm you would use:
#
#python maze_solver_skeleton.py test_maze.ppm test_path.ppm BFS 6
#
#If you read in an image, the same scaling will be used to output the
#image so in the example test_path.ppm will also be scaled by a factor
#of 6.  The actual maze is 50x50 so both ppm images are 300x300 pixels.
#
#You may read in a maze as a text file and output it as an image file or
#vice-versa.  If you read a maze in as a text file, you can specify a
#scaling just for the output file.

def main(argv):

    if (len(argv) < 4):
        print "Usage: maze_solver input_file output_file search-type <image scaling>"
        return
    infilename = argv[1]
    innameparts = infilename.split('.')
    if (len(innameparts) != 2 or (innameparts[1] != "ppm" \
                                  and innameparts[1] != "txt")):
        print "Must enter an input file name ending in .ppm or .txt"
        return
    outfilename = argv[2]
    outnameparts = outfilename.split('.')
    if (len(outnameparts) != 2 or (outnameparts[1] != "ppm" \
                                   and outnameparts[1] != "txt")):
        print "Must enter an output file name ending in .ppm or .txt"
        return
    if (argv[3] != "DFS" and argv[3] != "BFS"):
        print "Please enter valid search type.  Choose one of: BFS, DFS"
        return
    searchtype = argv[3]
    scaling = 1
    if (len(argv) > 4):
        try:
            scaling = int(argv[4])
        except:
            scaling = 1
    if (scaling <= 0):
        scaling = 1
    if (innameparts[1] == "ppm"):
        maze = mazeIO.ppmIO.read_maze_from_ppm(infilename, scaling)
    else:
        maze = mazeIO.asciiIO.read_maze_from_ascii(infilename)
    solver = MazeSolver(maze)
    path, expanded = solver.solve_maze(searchtype)
    print "Length of path:", len(path), \
        "\nNumber of nodes expanded: ", len(expanded)
    if (outnameparts[1] == "ppm"):
        mazeIO.ppmIO.write_visited_to_ppm(outfilename, maze, expanded, path, scaling)
    else:
        mazeIO.asciiIO.write_visited_to_ascii(outfilename, maze, expanded, path)

if __name__ == "__main__":
    main(sys.argv)

