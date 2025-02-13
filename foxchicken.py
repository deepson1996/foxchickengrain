from search import Node, StackFrontier
from util import get_neighbors

def main():
    start = [0, 0, 0, 0]
    target = [1, 1, 1, 1]
    
    path = get_path(start, target)
    
    for state, action in path:
        print(f"state:{state}, action:{action}")

def get_path(start, target):
    pass
            
     
        
if __name__ == "__main__":
    main()
    
    