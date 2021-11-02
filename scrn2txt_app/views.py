from django.shortcuts import render
from .utils import recognise, save_screen
import subprocess

def send_file(request):
    if request.method == 'POST':
        save_screen(request)
        # recognise(request)
        subprocess.run(['scrn2txt_app/start_recognise.sh'])
        return render(request, 'form_upload2.html')
    else:
        return render(request, 'form_upload.html')

# def recognise_file(request):
#     recognise(request)
#     return render(request, 'form_upload.html')

