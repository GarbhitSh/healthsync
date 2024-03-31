# views.py

import os
import torch
from PIL import Image
from torchvision import transforms
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .forms import ImageUploadForm
from .models import YourModel
import os
import torch
import torch.nn as nn
import numpy as np
from PIL import Image
from torchvision import transforms, models

resnet_model = torch.load('models\\bt_resnet50_model.pt', map_location=torch.device('cpu'))


device_name = "cuda:0:" if torch.cuda.is_available() else "cpu"
device = torch.device(device_name)

resnet_model = models.resnet50(pretrained=True)

for param in resnet_model.parameters():
    param.requires_grad = True

n_inputs = resnet_model.fc.in_features

resnet_model.fc = nn.Sequential(nn.Linear(n_inputs, 2048),
                                nn.SELU(),
                                nn.Dropout(p=0.4),
                                nn.Linear(2048, 2048),
                                nn.SELU(),
                                nn.Dropout(p=0.4),
                                nn.Linear(2048, 4),
                                nn.LogSigmoid())

for name, child in resnet_model.named_children():
    for name2, params in child.named_parameters():
        params.requires_grad = True

resnet_model.to(device)

resnet_model.load_state_dict(torch.load('models\\bt_resnet50_model.pt',map_location=torch.device('cpu')))

resnet_model.eval()

transform = transforms.Compose([transforms.Resize((512, 512)), transforms.ToTensor()])

LABELS = ['None', 'Meningioma', 'Glioma', 'Pitutary']


def predict_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']

            # Validate image format
            if not image_file.content_type.startswith('image/'):
                return HttpResponseBadRequest('Uploaded file is not an image.')

            try:
                img = Image.open(image_file)

                img = transform(img)

                img = img[None, ...]

                with torch.no_grad():       
                  y_hat = resnet_model.forward(img.to(device))

                  predicted = torch.argmax(y_hat.data, dim=1)

                  print(LABELS[predicted.data],'\n')
                  prediction=LABELS[predicted.data]


                return render(request, 'btiapp/result.html', {
                              'prediction': prediction,
                              'uploaded_image':image_file, })
            except Exception as e:
                print(f"Error processing image: {e}")
                return HttpResponseBadRequest('Error processing image.')
        else:
            return HttpResponseBadRequest('Form data is invalid.')
    else:
        form = ImageUploadForm()
    return render(request, 'btiapp/index.html', {'form': form})

def index(request):
    context = {}  # You can add context data here for the template
    return render(request, 'btiapp/index.html', context)
