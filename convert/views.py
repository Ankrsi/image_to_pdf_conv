from django.shortcuts import render,get_object_or_404
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from .models import *
from PIL import Image
import os

# def page(request):
#     return HttpResponse('<h1>anish</h1>')
def first_page(request):
    if request.method == 'POST':
        image=request.FILES.getlist("select_file")
        for f in image:
            imageinfo=Pic(name="img",image=f)
            imageinfo.save()
        img = Pic.objects.all()
        #pic=Pic.objects.get()orfilter()
        return render(request, "font.html", {"img":img})
    return render(request,"font.html")


def download(request):
    img_list=[]
    pic_list=[]
    if request.method == 'POST':
        for root, dir, files in os.walk('media/image'):
            for name in files:
                f=str(os.path.join(str(root),str(name)))
                img_list.append(f)
        for im in img_list:
            pic=Image.open(im)
            pic=pic.convert('RGB')
            pic_list.append(pic)
        try:
            count=1
            path=os.path.expanduser('~')
            dir_path=path+'\\'+'Downloads'
            if 'convert.pdf' in os.listdir(dir_path):
                pic_list[0].save("str(dir_path)+'\\convert'+str(count)+'.pdf'", save_all=True, append_images=pic_list[1:])
                count+=1
            else:
                pic_list[0].save(str(dir_path)+'\\convert.pdf',save_all=True,append_images=pic_list[1:])
            img = Pic.objects.all()
            img.delete()
            return render(request, "font.html",{'msg':'Download Completed , Check Your '+path+' Folder'})
        except:
            pic_list[0].save('convert.pdf', save_all=True, append_images=pic_list[1:])
            img = Pic.objects.all()
            img.delete()

    else:
        return redirect('first_page')
    return render(request,"font.html")
