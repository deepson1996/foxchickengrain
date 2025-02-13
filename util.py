def is_valid(state):
    farmer, fox, chicken, grain = state

    # Check for unsafe combinations
    if (chicken == fox and farmer != chicken):  # Chicken and Fox alone
        return False
    if (chicken == grain and farmer != chicken):  # Chicken and Grain alone
        return False
    return True
        
def get_neighbors(state):
    """
    from all the moves check valid moves returns them as list of list 
    """
    farmer, fox, chicken, grain = state
    moves = []
    # move man only
    man_move = [1-farmer, fox, chicken, grain]
    if(is_valid(man_move)):
        moves.append((man_move, "Move farmer"))
    # move man and fox
    man_fox_move = [1-farmer, 1-fox, chicken, grain]
    if is_valid(man_fox_move) and (farmer == fox):
        moves.append((man_fox_move, "Move farmer and fox"))
    # move man and grain
    man_grain_move = [1-farmer, fox, chicken, 1-grain]
    if is_valid(man_grain_move) and (farmer == grain):
        moves.append((man_grain_move, "Move farmer and grain"))
    # move man and chicken  
    man_chicken_move = [1-farmer, fox, 1-chicken, grain]
    if is_valid(man_chicken_move) and (farmer == chicken):
        moves.append((man_chicken_move, "Move farmer and chicken")) 
        
    return moves