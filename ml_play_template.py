"""
The template of the main script of the machine learning process
"""
import pygame
import sys
import numpy as np
import pickle
from os.path import exists
import os

sys.path.append("C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml")
from tool.pos_predict import movement_choice
from tool.data_generator import get_graph
   


class MLPlay:
    
    def __init__(self, ai_name, *args, **kwargs):
        """
        Constructor
        """
        i = 0
        graph_path = "C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml/graph"
        while (exists(graph_path + '/graph' + str(i) + '.pickle')): i += 1
        self.ball_served = False
        self.ball_x = 93
        self.ball_y = 395
        self.count = i
        self.datas = []
        self.last_brick = -1
        self.zero_point_pos = []



        self.origin_bricks = []
        self.origin_hard_bricks = []

        self.action_space = {"MOVE_RIGHT" : 0, "MOVE_LEFT" : 1, "NONE" : 2}

        

    def update(self, scene_info, keyboard=None, *args, **kwargs):
        """
        Generate the command according to the received `scene_info`.
        """
        #'frame', 'status', 'ball', 'platform', 'bricks', 'hard_bricks'
        
        last_ball_x = self.ball_x
        last_ball_y = self.ball_y
        self.ball_x = scene_info["ball"][0]
        self.ball_y = scene_info["ball"][1]
        
        speed_x = self.ball_x - last_ball_x
        speed_y = self.ball_y - last_ball_y #y速度大於0時是下降
        
        
        
        plateform_x = scene_info['platform'][0] + 20
        bricks = scene_info["bricks"]        #一般方塊的存在位置
        hard_bricks = scene_info["hard_bricks"]
        
        command = "NONE"
        
        
        
        if not self.ball_served:
            self.ball_served = True
            self.origin_bricks = scene_info["bricks"]
            self.origin_hard_bricks = scene_info["hard_bricks"]

            return "SERVE_TO_RIGHT"
            
        else:
            command = movement_choice(self.ball_x, self.ball_y, speed_x, speed_y, plateform_x)
        

        if (self.last_brick == -1):
            self.last_brick = len(bricks) + len(hard_bricks) * 2


        #填出影像
        new = (bricks, hard_bricks, self.ball_x, self.ball_y, last_ball_x, last_ball_y, scene_info['platform'][0], self.origin_bricks, self.origin_hard_bricks)

        self.datas.append([new, self.action_space[command]])
        

        


        #儲存的資料
        if ((self.ball_y == 395 and len(self.datas) > 1) or scene_info["status"] == "GAME_PASS"):
            dataName = str(int(self.count / 10)) + str(int(self.count % 10))

            return_data = self.datas #圖像資料們, 執行的動作
            with open('C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml/graph/' + dataName + '.pickle', 'wb') as f:
                pickle.dump(return_data, f)
            self.datas = []
            self.count += 1
                
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            self.last_brick = -1
            self.ball_x = 93
            self.ball_y = 395
            self.datas = []
            self.zero_point_pos = set([])
            
            return "RESET"

        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False


# cd C:\Users\weiso131\Desktop\paia2.4.5\resources\app.asar.unpacked\games\arkanoid
# python -m mlgame -i ./ml/ml_play_template.py . --difficulty NORMAL --level 20