from django.shortcuts import render
import os.path

from django.conf import settings
from django.http import HttpResponse, Http404

from .models import FilesAdmin
# Create your views here.



def index(request):
    context = {'file':FilesAdmin.objects.all()}
    return render(request, 'index.html', context)

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404


def music(request):
    return render(request, 'song/music.html')


def social(request):
    return render(request, 'song/social.html')


