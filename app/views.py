from django.shortcuts import render
from .models import Vehicle, LaneDetection
from django.core.files.storage import FileSystemStorage
from .number_plate_detection import detect_number_plate
import os

def index(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        plate_number = detect_number_plate(os.path.join('media', filename))
        vehicle = Vehicle.objects.create(plate_number=plate_number, image_path=uploaded_file_url)
        vehicle.save()

        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file_url,
            'plate_number': plate_number
        })

    return render(request, 'index.html')
