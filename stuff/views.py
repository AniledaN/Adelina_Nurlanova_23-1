from django.shortcuts import render
from stuff.models import Stuff

# Create your views here.


def main_view(request):
    return render(request, 'layouts/index.html')


def stuff_view(request):
    if request.method == 'GET':
        stuff = Stuff.objects.all()

        return render(request, 'stuff/stuff.html', context={
            'stuff': stuff
        })


def stuff_detail_view(request, id):
    if request.method == 'GET':
        stuff = Stuff.objects.get(id=id)

        context = {
            'stuff': stuff,
            'comments': stuff.comments.all()
        }

        return render(request, 'stuff/detail.html', context=context)