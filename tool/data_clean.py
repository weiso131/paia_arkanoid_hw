import sys
import pickle
import os
from os import listdir
sys.path.append("C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml/tool")

#from data_generator import get_graph

"""
資料格式
[[[(磚塊x, 磚塊y),], [(硬磚塊x, 硬磚塊y),], 盤子的位置, (球位置x, 球位置y), (球速度x, 球速度y), action], 
[[(磚塊x, 磚塊y),], [(硬磚塊x, 硬磚塊y),], 盤子的位置, (球位置x, 球位置y), (球速度x, 球速度y), action], 
[[(磚塊x, 磚塊y),], [(硬磚塊x, 硬磚塊y),], 盤子的位置, (球位置x, 球位置y), (球速度x, 球速度y), action], 
....]

"""

def brick_compare(bricks_a : list, bricks_b : list) -> bool:
    i = 0
    while (i < len(bricks_a) and i < len(bricks_b)):
        if (bricks_a[i] != bricks_b[i]): return False
        i += 1
    return True

def data_compare(old_data_path : str, new_data_path : str):
    
    with open(old_data_path, "rb") as f:
        old_data = pickle.load(f)
    with open(new_data_path, "rb") as f:
        new_data = pickle.load(f)
    #確定要存的資料
    new_data_correct = []
    
    for j in range(len(new_data)):
        save_data = True
        
        for i in range(len(old_data)):
            bool_check = brick_compare(old_data[i][0], new_data[j][0]) and \
                brick_compare(old_data[i][1], new_data[j][1]) and \
                old_data[i][2] == new_data[j][2] and \
                old_data[i][3] == new_data[j][3] and \
                old_data[i][4] == new_data[j][4]
                
            if (bool_check): 
                    save_data = False
                    break
        if (save_data):
             new_data_correct.append(new_data[j])

    with open(new_data_path, 'wb') as f:
        pickle.dump(new_data_correct, f)

def train_data_clean(train_data_path : str, origin_data_path : str):
    """
    origin_data_path
        graphX
            data1.pickle
            data2.pickle
            data3.pickle
    train_path_path

    """
    origin_data_dirs = listdir(origin_data_path)
    for dir_name in origin_data_dirs:
        data_list = listdir(origin_data_path + '/' + dir_name)
        for data_name in data_list:
            #print(origin_data_path + '/' + dir_name + '/' + data_name)

            train_data = listdir(train_data_path)
            for td in train_data:
                data_compare(train_data_path + '/' + td, origin_data_path + '/' + dir_name + '/' + data_name)
            os.rename(src=origin_data_path + '/' + dir_name + '/' + data_name, 
                        dst=train_data_path + '/' + dir_name + '_' + data_name)
    


    