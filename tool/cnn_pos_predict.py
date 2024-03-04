import sys
import numpy as np
sys.path.append("C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml")

from torch import nn
import torch

from tool.pos_predict import pos_predict

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv_layer = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(in_channels=32, out_channels=128, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        with torch.no_grad():
            self._to_linear = self.conv_layer(torch.zeros(1, 1, 40, 100))
            self._to_linear = torch.flatten(self._to_linear)
        self.fc_layer = nn.Sequential(
            nn.Linear(len(self._to_linear), 1024),
            nn.Dropout(0.7),
            nn.ReLU(),
            nn.Linear(1024, 1)
        )

    def forward(self, x):
        x = self.conv_layer(x)
        x = torch.flatten(x, 1)
        x = self.fc_layer(x)
        return x
    




check_point = torch.load("C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml/checkpoint2.pth")
model = CNN()#要跟讀取的模型同個結構
model.load_state_dict(check_point)

use_gpu = False
if (use_gpu):
    model = model.to(device="cuda", dtype=torch.float32)
else:
    model = model.to(dtype=torch.float32)

def ml_predict(graph, use_pos_predict, ball_x, ball_y, speed_x, speed_y):
    tensor_graph = torch.tensor([graph])
    
    model.eval()
    with torch.no_grad():
        tensor_graph = tensor_graph.unsqueeze(dim=0)

        if (use_gpu): tensor_graph = tensor_graph.to(device="cuda", dtype=torch.float32)
        else: tensor_graph = tensor_graph.to(dtype=torch.float32)
        predict = float(model(tensor_graph)[0]) * 5
    if (use_pos_predict and speed_y > 0):
        predict = pos_predict(ball_x, ball_y, speed_x, speed_y)
    return predict

#python -m mlgame -f 120 --one-shot -i .\ml\ml_play.py . --difficulty NORMAL --level 1

