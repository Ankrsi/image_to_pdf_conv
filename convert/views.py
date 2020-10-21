from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from .models import *
from PIL import Image
import os

img_lists=[]
def first_page(request):
    pic_list=[]
    if request.method == 'POST':
        image=request.FILES.getlist("select_file")
        for f in image:
            img_lists.append(f)
            imageinfo=Pic(name="img",image=f)
            imageinfo.save()
        img = Pic.objects.all()
        #pic=Pic.objects.get()orfilter()
        for l in img_lists:
            lists=Image.open(l)
            rgb_img=lists.convert('RGB')
            pic_list.append(rgb_img)
        pic_list[0].save('./static/IMG/convert.pdf', save_all=True,append_images=pic_list[1:])
        return render(request,"font.html",{"img":img,'msg':'click here to download '})
    try:
        img = Pic.objects.all()
        img.delete()
        os.remove('./static/IMG/convert.pdf')
    except:
        pass
    return render(request,"font.html")
