import numpy as np

def pos_predict(pos_x, pos_y, speed_x, speed_y, wall_l = 0, wall_r = 195, down_limit = 395):
    """
    Parameters
    ----------
    pos_x : int
        the x posision of the ball 
    pos_y : int
        the y posision of the ball
    speed_x : int
        the x direction speed of the ball
    speed_y : int
        the y direction speed of the ball
    wall_l : int
        the left limit of playground
    wall_r : int
        the right limit of playground
    down_limit : int
        the y posision that plateform at
        
    Returns
    -------
    (end_pos_x, end_pos_y)

    """
        

    while (pos_y < down_limit):
        pos_x += speed_x
        pos_y += speed_y
        
        if (pos_x >= wall_r):
            speed_x *= -1
            
        if (pos_x <= wall_l):
            speed_x *= -1
            
    return pos_x

def movement_choice(ball_x, ball_y, speed_x , speed_y, plateform_x):
    command = "NONE"
    rd = np.random.randint(0, 3)
    if (speed_y > 0 and ball_y > 150):
        goal_x = pos_predict(ball_x, ball_y, speed_x , speed_y) 
        if (goal_x - plateform_x > 5): command = "MOVE_RIGHT"
        elif (goal_x - plateform_x < 5): command = "MOVE_LEFT"

        elif (ball_y >= 380):
            if (rd == 0):
                
                if (speed_x > 0): command = "MOVE_RIGHT"
                else: command = "MOVE_LEFT"
            elif(rd == 1):
                command = "NONE"
            else:
                if (speed_x > 0): command = "MOVE_LEFT"
                else: command = "MOVE_RIGHT"
        if (ball_y == 395):
            print(f"ball_x{ball_x}, speed_x{speed_x}, plateform_x{plateform_x}")
    
    elif ((speed_y) < 0 and ball_y > 370):
        if (ball_x - plateform_x > 0): command = "MOVE_RIGHT"
        elif(ball_x - plateform_x < 0): command = "MOVE_LEFT"
        else: command = "NONE"
        
    else:
        if (100 - plateform_x > 0): command = "MOVE_RIGHT"
        elif (100 - plateform_x < 0): command = "MOVE_LEFT"
        else: command = "NONE"
    
    return command

"""
#10
command = "NONE"
    rd = np.random.randint(0, 3)
    if (speed_y > 0 and ball_y > 150):
        goal_x = pos_predict(ball_x, ball_y, speed_x , speed_y) 
        if (goal_x - plateform_x > 5): command = "MOVE_RIGHT"
        elif (goal_x - plateform_x < 5): command = "MOVE_LEFT"

        elif (ball_y >= 380):
            if (rd == 0):
                print("切球")
                if (speed_x > 0): command = "MOVE_RIGHT"
                else: command = "MOVE_LEFT"
            elif(rd == 1):
                command = "NONE"
            else:
                print("反向")
                if (speed_x > 0): command = "MOVE_LEFT"
                else: command = "MOVE_RIGHT"
        if (ball_y == 395):
            print(goal_x - plateform_x)
    
    elif ((speed_y) < 0 and ball_y > 370):
        if (ball_x - plateform_x > 0): command = "MOVE_RIGHT"
        elif(ball_x - plateform_x < 0): command = "MOVE_LEFT"
        else: command = "NONE"
        
    else:
        if (100 - plateform_x > 0): command = "MOVE_RIGHT"
        elif (100 - plateform_x < 0): command = "MOVE_LEFT"
        else: command = "NONE"
    
    return command
"""

"""
19
command = "NONE"
    rd = np.random.randint(0, 3)
    range_rd = np.random.randint(5, 11)
    if (speed_y > 0 and ball_y > 250):
        goal_x = pos_predict(ball_x, ball_y, speed_x , speed_y) 
        if (goal_x - plateform_x > range_rd): command = "MOVE_RIGHT"
        elif (goal_x - plateform_x < range_rd): command = "MOVE_LEFT"

        elif (ball_y >= 370):
            print("開搞")
            if (True):
                print("切球")
                if (speed_x > 0): command = "MOVE_RIGHT"
                else: command = "MOVE_LEFT"
            elif(rd == 1):
                command = "NONE"
            else:
                print("反向")
                if (speed_x > 0): command = "MOVE_LEFT"
                else: command = "MOVE_RIGHT"
        if (ball_y == 395):
            print(goal_x - plateform_x)
    
    elif (speed_y < 0 and ball_y > 380):
        if (ball_x + speed_x - plateform_x > 0 or ball_x - plateform_x > 0): command = "MOVE_RIGHT"
        elif(ball_x + speed_x - plateform_x < 0 or ball_x - plateform_x < 0): command = "MOVE_LEFT"
        else: command = "NONE"
        
    else:
        if (100 - plateform_x > 0): command = "MOVE_RIGHT"
        elif (100 - plateform_x < 0): command = "MOVE_LEFT"
        else: command = "NONE"
    
    return command
"""