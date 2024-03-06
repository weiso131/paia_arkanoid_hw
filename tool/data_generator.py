import numpy as np
import sys

sys.path.append("C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml")


def get_graph(bricks:list, hard_bricks:list, ball_x : int, ball_y : int, last_ball_x : int, last_ball_y : int, plateform_x_left) -> np.array:
    #填出影像
    graph = np.zeros((2, 40, 100))

    #填出方塊
    for x, y in bricks:
        for dim0 in range(2):
            for i in range(3):
                    graph[dim0, min(39, int(x / 5) + i), int(y / 5)] = 25
    for x, y in hard_bricks:
        for dim0 in range(2):
            for i in range(5):
                for j in range(2):
                    graph[dim0, min(39, int(x / 5) + i), int(y / 5) + j] = 50
    
    #填出盤子
    for i in range(8):
        x = max(0, min(39, int(plateform_x_left / 5) + i))
        for dim0 in range(2):
            graph[dim0, x, int(395 / 5)] = 100

    #填出球
    graph[0, min(39, int(last_ball_x / 5)), int(last_ball_y / 5)] = 150
    graph[1, min(39, int(ball_x / 5)), int(ball_y / 5)] = 150

    return graph