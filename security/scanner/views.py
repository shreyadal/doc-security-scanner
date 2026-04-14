import os
import subprocess
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def welcome(request):
    return render(request, 'welcome.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('scan')  # <-- sends you to the scan page
        else:
            return render(request, 'login.html', {"error": "Invalid username or password"})

    return render(request, 'login.html')


# @login_required
def scan_document(request):
    result = None

    if request.method == 'POST' and request.FILES.get('document'):
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        file_path = fs.save(uploaded_file.name, uploaded_file)
        file_full_path = os.path.join(settings.MEDIA_ROOT, file_path)

        # Run ClamAV scan
        try:
            scan_cmd = [
                r'C:\clamav-1.4.2.win.x64\clamscan.exe',
                file_full_path,
                '--database=C:\\clamav-1.4.2.win.x64\\database'
            ]
            process = subprocess.run(scan_cmd, capture_output=True, text=True)
            result = process.stdout
        except Exception as e:
            result = f"Error during scan: {e}"

    return render(request, 'upload.html', {'result': result})
