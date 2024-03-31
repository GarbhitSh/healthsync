# models.py

import torch
import torch.nn as nn
import torchvision.models as models

class YourModel(nn.Module):
    def __init__(self):
        super(YourModel, self).__init__()
        # Load a pretrained ResNet-50 model
        self.resnet50 = models.resnet50(pretrained=True)
        # Replace the final fully connected layer with a new one for your specific task
        num_ftrs = self.resnet50.fc.in_features
        self.resnet50.fc = nn.Linear(num_ftrs, 4)  # Assuming 4 output classes for brain tumor types

    def forward(self, x):
        return self.resnet50(x)
