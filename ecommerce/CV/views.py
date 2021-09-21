from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import FormView
from .forms import *



try:
    from PIL import Image
except:
    import Image
import pytesseract



# Create your views here.

class Image2Text(FormView):
    form_class = UploadForm
    template_name = 'image2text.html'
    success_url = '/'

    # def form_valid(self, form):
    #     upload = self.request.FILES['file']
    #     print(type(pytesseract.image_to_string(Image.open(upload)))) # =====> add line

    #     return super().form_valid(form)

@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        response_data = {}
        upload = request.FILES['file']
        content = pytesseract.image_to_string(Image.open(upload))
        response_data['content'] = content

        return JsonResponse(response_data)


