# Xray/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadImageForm
from .predictions import predict
from .models import UploadedImage
from PIL import Image
from django.shortcuts import render
from .forms import UploadImageForm # Assuming you have a form for file upload

from django.shortcuts import render, redirect
from .forms import UploadImageForm
from .models import UploadedImage
from .predictions import predict  # Assuming predictions.py exists


def home(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            bone_type_result = predict(uploaded_image.image.path)
            prediction_result = predict(uploaded_image.image.path, bone_type_result)

            return render(
                request, 'Xray/result.html', {
                    'Bone_type': bone_type_result,
                    'prediction_result': prediction_result,
                    'uploaded_image': uploaded_image,
                }
            )
    else:
        form = UploadImageForm()
    return render(request, 'Xray/index.html', {'form': form})


def upload_view(request):
    # This view is no longer necessary as its functionality
    # is integrated into home
    return redirect('index')  # Redirect to the main page

def result(request):
    upload_view(request)

    return render(request, 'Xray/result.html')

def show_rules(request):
    return render(request, 'Xray/rules.html')

def about(request):
    return render(request, 'about.html')
