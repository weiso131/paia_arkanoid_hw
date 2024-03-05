import sys
import numpy as np
sys.path.append("C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml")

from torch import nn
import torch

import torch.nn.functional as F

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()

        self.conv = nn.Sequential(nn.Conv2d(1, 16, kernel_size=3, padding=1, stride=2),
                                  nn.ReLU(),
                                  nn.Conv2d(16, 64, kernel_size=3, padding=1, stride=2),
                                  nn.ReLU())

        fc_sample = torch.zeros((1, 40, 100))
        self.fc_input = len(torch.flatten(self.conv(fc_sample)))

        self.fc = nn.Sequential(nn.Linear(self.fc_input, 1024),
                                nn.ReLU(),
                                nn.Linear(1024, 3))
        
        
    def forward(self, x):
        x = self.conv(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)
        return x
    




check_point = torch.load("C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml/checkpoint_cls.pth")
model = SimpleCNN()#要跟讀取的模型同個結構
model.load_state_dict(check_point)

model = model.to(dtype=torch.float32)


action_space = ["MOVE_RIGHT", "MOVE_LEFT", "NONE"]

def ml_predict(graph) -> str:
    tensor_graph = torch.tensor([graph])
    
    model.eval()
    with torch.no_grad():
        tensor_graph = tensor_graph.unsqueeze(dim=0)

        tensor_graph = tensor_graph.to(dtype=torch.float32)
        out = model(tensor_graph)[0]
        predict = action_space[int(torch.argmax(out))]
    
    return predict

#python -m mlgame -f 120 --one-shot -i .\ml\ml_play.py . --difficulty NORMAL --level 1

