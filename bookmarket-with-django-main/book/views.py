from django.http import JsonResponse
from .models import Book, Author, Category
import datetime



def book_view(request):
    objects = Book.objects.all()
    data = []
    
    for i in objects:
        data.append({
            "id": i.id,
            "name": i.name,
            "desc": i.desc,
            "author": i.author.full_name,
            "category": i.category.name,
            "created_at": i.created_at,
            "updated_at": i.updated_at
        })
    
    return JsonResponse(data, safe=False)


def book_view_by_id(request, id):
    i = Book.objects.get(id=id)
    
    data = {
        "id": i.id,
        "name": i.name,
        "desc": i.desc,
        "author": i.author.full_name,
        "category": i.category.name,
        "created_at": i.created_at,
        "updated_at": i.updated_at
    }
    
    return JsonResponse(data, safe=False)


def author_view(request):
    objects = Author.objects.all()
    data = []
    
    for i in objects:
        data.append({
            "id": i.id,
            "full_name": i.full_name,
            "desc": i.desc,
            "created_at": i.created_at,
            "updated_at": i.updated_at
        })
    
    return JsonResponse(data, safe=False)


def category_view(request):
    objects = Category.objects.all()
    data = []

    for i in objects:
        data.append({
            "id": i.id,
            "name": i.name,
            "created_at": i.created_at,
            "updated_at": i.updated_at
        })
    
    return JsonResponse(data, safe=False)
