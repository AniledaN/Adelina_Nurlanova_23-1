from django.shortcuts import render
from stuff.models import Stuff, Category

# Create your views here.


def main_view(request):
    return render(request, 'layouts/index.html')


def stuff_view(request):
    if request.method == 'GET':
        category_id = int(request.GET.get('category_id', 0))

        if category_id:
            stuff = Stuff.objects.filter(categories__in=[category_id])
        else:
            stuff = Stuff.objects.all()

        return render(request, 'stuff/stuff.html', context={
            'stuff': stuff
        })


def stuff_detail_view(request, id):
    if request.method == 'GET':
        stuff = Stuff.objects.get(id=id)

        context = {
            'stuff': stuff,
            'comments': stuff.comments.all(),
            'categories': stuff.categories.all()
        }

        return render(request, 'stuff/detail.html', context=context)


def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context = {
            'categories': categories
        }

        return render(request, 'categories/index.html', context=context)