#Tamrin 1
#BFS
#Faezeh Movahedi
             
#Open Maze:
file = open ("Maze.txt" , "r")
maze = file.read().split()
for i in maze:
    print (i)


class Node:  
    def __init__(self , s , p , d):
        self.state= s
        self.parent = p
        self.depth = d
        #state = (x,y)
        #parent = Pointing to the parent node
        

goal_state = maze[15][30]
# print (goal_node)



def BFS():
    #start_point = maze[15][0] => state = (15,0)
    start_node = Node ([15,0] , None , 0)
    # print('\n' , maze[start_node.state[0]][start_node.state[1]])
    if start_node.state == [15,30]:
        return (start_node)
    
    explored = []
    frontier = [start_node]

    while frontier:
        print ('\n************************************************************')
        print ('Frontier = {')
        for x in frontier:
            print ( x.state)
        print ('}')
        print ('\nexpelored = ' , explored) 

        if frontier is None:
            print ("goal is not find")
            return 0 
        n = frontier.pop(0)
        print ('\n' , n.state , ' is poped')
        explored.append(n.state)
   
        # check for vhild --> first right then left, top and bottom 
        
        if ((maze[n.state[0]][n.state[1] + 1] == '1') and ([n.state[0] , n.state[1] + 1] not in explored)):
            child = Node ([n.state[0] , n.state[1] + 1] , n , n.depth + 1)
            if (child.state == [15,30]):
                print ("\nGoal is findddd between " , child.state , "childs :)))))")
                return child
            else:
                frontier.append(child)
            

        if ((maze[n.state[0]][n.state[1] - 1] == '1') and (n.state != [15,0]) and ([n.state[0] , n.state[1] - 1] not in explored)):
            child = Node ([n.state[0] , n.state[1] - 1] , n , n.depth + 1)
            if (child.state == [15,30]):
                print ("\nGoal is findddd between " , child.state , "childs :)))))")
                return child
            else:
                frontier.append(child)

        if ((maze[n.state[0] + 1][n.state[1]] == '1') and ([n.state[0] + 1 , n.state[1]] not in explored)):
            child = Node ([n.state[0] + 1 , n.state[1]] , n , n.depth + 1)
            if (child.state == [15,30]):
                print ("\nGoal is findddd between " , child.state , "childs :)))))")
                return child
            else:
                frontier.append(child)
        
        if ((maze[n.state[0] - 1][n.state[1]] == '1') and ([n.state[0] - 1, n.state[1]] not in explored)):
            child = Node ([n.state[0] - 1 , n.state[1]] , n , n.depth + 1)
            if (child.state == [15,30]):
                print ("\nGoal ([15,30]) is findddd between " , child.state , "childs :)))))")
                return child
            else:
                frontier.append(child)

# def IDS():
#     #start_point = maze[15][0] => state = (15,0)
#     start_node = Node ([15,0] , None , 0)
#     for L in range():
#         if start_node.state == [15,30]:
#             print ('goal is find')
#             return start_node
#         elif start_node.depth == L:
#             print ("goal is not find in L = " , L)
#             print('**********************************************')
#         else:
#             for 



        

    


goal = BFS()  

direction = [goal.state]
goal_parent = goal
while ([15,0] not in direction):
    goal_parent = goal_parent.parent
    direction.append(goal_parent.state)

print('Goal direction = {')

direction.reverse()
for x in direction:
    print (x)
print ('}')










        

