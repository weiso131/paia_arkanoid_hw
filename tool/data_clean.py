import sys
import pickle
import os
from os import listdir
sys.path.append("C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml/tool")

#from data_generator import get_graph

"""
資料格式
bricks, hard_bricks, ball_x, ball_y, last_ball_x, last_ball_y, plateform_x_left, origin_bricks

"""

def brick_compare(bricks_a : list, bricks_b : list) -> bool:
    i = 0
    while (i < len(bricks_a) and i < len(bricks_b)):
        if (bricks_a[i] != bricks_b[i]): return False
        i += 1
    return True

def data_compare(old_data_path : str, new_data_path : str):
    """
    1. 打開已經認證過的資料
    2. 打開未認證過的資料
    3. 修改未認證的資料的內容
    
    """
    with open(old_data_path, "rb") as f:
        old_data = pickle.load(f)
    with open(new_data_path, "rb") as f:
        new_data = pickle.load(f)
    #確定要存的資料
    new_data_correct = []
    
    for j in range(len(new_data)):
        save_data = True
        
        for i in range(len(old_data)):
            old_bricks, old_hard_bricks, old_ball_x, old_ball_y, old_last_ball_x, old_last_ball_y, old_plateform_x_left, _ = old_data[i][0]
            new_bricks, new_hard_bricks, new_ball_x, new_ball_y, new_last_ball_x, new_last_ball_y, new_plateform_x_left, _ = new_data[j][0]
            bool_check = brick_compare(old_bricks, new_bricks) and \
                brick_compare(old_hard_bricks, new_hard_bricks) and \
                old_ball_x == new_ball_x and \
                old_ball_y == new_ball_y and \
                old_last_ball_x == new_last_ball_x and \
                old_last_ball_y == new_last_ball_y and \
                old_plateform_x_left == new_plateform_x_left
                
            if (bool_check): 
                    print(f"new_ball_x:{new_ball_x}, old_ball_x:{old_ball_x}, new_plateform_x_left:{new_plateform_x_left}, old_plateform_x_left:{old_plateform_x_left}")
                    save_data = False
                    break
        if (save_data):
             new_data_correct.append(new_data[j])

    with open(new_data_path, 'wb') as f:
        pickle.dump(new_data_correct, f)


    


    