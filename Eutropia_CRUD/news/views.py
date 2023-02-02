from django.shortcuts import render
from news.models import dailyNews
from news.forms import Newsform
from django.shortcuts import redirect


def nws(request):
    if request.method== "POST":
        form=Newsform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show') 
            except:
                pass
    else: 
        form = Newsform()
    return render(request, 'index.html', {'form':form})

def show(request):
    news= dailyNews.objects.all()
    return render(request, 'show.html', {'news':news })

def edit(request,id):
    news= dailyNews.objects.get(id=id)
    return render(request, 'edit.html',{'news':news})

def update(request,id):
    news= dailyNews.objects.get(id = id)
    form=Newsform(request.POST,instance=news)
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'news': news}) 

def delete(request, id):  
    news = dailyNews.objects.get(id=id)  
    news.delete()  
    return redirect("/show")