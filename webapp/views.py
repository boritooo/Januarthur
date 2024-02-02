from django.shortcuts import render, redirect

from webapp.painter_forms import PainterForm
from . models import *




def home_page(request):
    return render(request, 'pages/home.html')

def sculpture_page(request):
    return render(request,  'pages/sculptures.html')

def painting_page(request):
    return render(request,  'pages/paintings.html')

def painter_page(request):
    painters = Painter.objects.all()
    return render(request,  'pages/painter.html',{'painters':painters})

def painter_info(request):
    painters = Painter.objects.all()
    context ={
        'painters':painters,
        
    }
    return render(request, 'pages/painter_info.html', context)

def createpainter_form(request):
    form = PainterForm()
    if request.method == 'POST':
        form = PainterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('painterPage')


    context ={
        'form':form 
    } 


    return render (request, 'pages/painter_form.html', context)

def updatePainter(request, pk):
    painter = Painter.objects.get(id=pk)
    form = PainterForm(instance=painter)

    if request.method == 'POST':
        form = PainterForm(request.POST, instance=painter)
        if form.is_valid():
            form.save()
            return redirect('painterPage')


    context ={'form':form}    
    return render(request, 'pages/painter_form.html', context)


def deletePainter(request, pk):
    painter = Painter.objects.get(id=pk)
    if request.method == 'POST':
        painter.delete()
        return redirect('painterPage')
    
    context = {'painter':painter}

    return render(request, 'pages/delete_painter.html', context)