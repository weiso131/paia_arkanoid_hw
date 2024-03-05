"""
The template of the main script of the machine learning process
"""
import pygame
import sys
import numpy as np
import pickle
from collections import deque


sys.path.append("C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml")
from tool.cnn_pos_predict_cls import ml_predict
from tool.data_generator import get_graph
   


class MLPlay:
    
    def __init__(self, ai_name, *args, **kwargs):
        """
        Constructor
        """
        self.ball_served = False
        self.ball_x = 93
        self.ball_y = 395
        self.count = 0
        self.datas = []
        self.last_data = deque([])
        
        

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
        speed_y = self.ball_y - last_ball_y#y速度大於0時是下降
        
        
        
        plateform_x = scene_info['platform'][0] + 20
        plateform_y = scene_info['platform'][1]
        bricks = scene_info["bricks"]        #一般方塊的存在位置
        hard_bricks = scene_info["hard_bricks"]
        
        command = "NONE"
        


        #填出影像
        new = get_graph(bricks, hard_bricks, self.ball_x, self.ball_y, last_ball_x, last_ball_y, scene_info['platform'][0])
        command = ml_predict(new)



        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            

            self.ball_x = 93
            self.ball_y = 395
            self.datas = []
            self.last_data = deque([])

            return "RESET"
        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_RIGHT"
            

            
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False


# cd C:\Users\weiso131\Desktop\paia2.4.5\resources\app.asar.unpacked\games\arkanoid
# python -m mlgame -f 120 --one-shot -i ./ml/ml_play.py . --difficulty NORMAL --level 1
