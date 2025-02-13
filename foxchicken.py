from search import Node, StackFrontier
from util import get_neighbors

def main():
    start = [0, 0, 0, 0]
    target = [1, 1, 1, 1]
    
    path = get_path(start, target)
    
    for state, action in path:
        print(f"state:{state}, action:{action}")

def get_path(start, target):
    """
    TODO: Your code goes here
    initialize frontier
    iterate until found or not found
        if empty frontier 
            no path found
        remove node
        if node state is target state
            return solution
            
        explore neighbors and add to frontier
        
    """
    pass
            
     
        
if __name__ == "__main__":
    main()
    
    