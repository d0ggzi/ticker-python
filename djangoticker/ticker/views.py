from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from moviepy.editor import *
import os
import matplotlib.colors as mc

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
screensize=(100, 100)

def ticker(message, duration=3, bg_color="black", text_color="white"):
    try:
        txtClip = TextClip(message, color=text_color, font="PT Mono",
                        kerning = -5, fontsize=80, bg_color=bg_color)
        speed = (len(message)-3)/duration * 33
        txtClip = txtClip.set_position(lambda t: (-speed*t, 0))
        bg_color = [el*255 for el in mc.to_rgb(bg_color)]
        cvc = CompositeVideoClip( [txtClip], size=screensize, bg_color=bg_color).set_duration(duration)

        filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
        cvc.write_videofile(os.path.join(BASE_DIR+"/video",filename) + '.avi',fps=25,codec='mpeg4')

        return filename
    except Exception as e:
        print(e)


def index(request):
    if request.method == 'POST':
        form = CreateVideoForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            filename = ticker(data['message'], data['duration'], data['bg_color'], data['text_color'])

            with open(os.path.join(BASE_DIR+"/video",filename+'.avi'), 'rb') as f:
                video = f.read()

            response = HttpResponse(video, content_type='video/x-msvideo')
            response['Content-Disposition'] = 'attachment; filename="video.avi"'
            return response
    else:
        form = CreateVideoForm()

    return render(request, 'ticker/index.html', {'form': form, 'title': "Главная"})


def create(request):
    message = request.GET.get("message")
    duration = int(request.GET.get("duration", 3))
    bg_color = request.GET.get("bg_color", "black")
    text_color = request.GET.get("text_color", "white")
    if message:
        Ticker.objects.create(message=message, duration=duration, bg_color=bg_color, text_color=text_color)
        filename = ticker(message, duration, bg_color, text_color)

        with open(os.path.join(BASE_DIR+"/video",filename+'.avi'), 'rb') as f:
            video = f.read()

        response = HttpResponse(video, content_type='video/x-msvideo')
        response['Content-Disposition'] = 'attachment; filename="video.avi"'
        return response
    else:
        return HttpResponse("<h2>Введите сообщение</h2>")