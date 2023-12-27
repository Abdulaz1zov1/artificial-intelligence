from django.http import JsonResponse
from .models import News, Category
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.views import View
from rest_framework import views
from rest_framework import views, response
from .serializers import CategorySerializer

from rest_framework import generics


class Category2List(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CategoryAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        data_obj = Category.objects.all()
        
        data = CategorySerializer(data_obj, many=True)
        return response.Response(data.data)



class CategoryList(View):
    def get(self, request, *args, **kwargs):
        data_obj = Category.objects.all()
        
        data = [
            {
                "id": i.id,
                "name": i.name,
                "created_at": i.created_at,
            } for i in data_obj
        ]

        return JsonResponse(data, safe=False)
    
    def post(self, request, *args, **kwargs):

        data = request.POST
        new_category_obj = Category(name=data['name'])
        new_category_obj.save()
        
        return JsonResponse({
            "status": "201",
            "obj_id": new_category_obj.id
        }, status=201)


class CategoryView(View):
    
    def get_object(self, id):
        return Category.objects.filter(id=int(id))

    def get(self, request, id, *args, **kwargs):
        data_obj = self.get_object(id)
        
        if len(data_obj)==0:
            return JsonResponse({"status": "object does not exist"}, status=404)
        
        data = [
            {
                "id": i.id,
                "name": i.name,
                "created_at": i.created_at,
            } for i in data_obj
        ]

        return JsonResponse(data[0], safe=False)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id)[0]
        obj.delete()
        
        return JsonResponse({}, status=204)
    
    def post(self, request, id, *args, **kwargs):
        
        data = request.POST
        obj = self.get_object(id)[0]
        obj.name = data['name']
        obj.save()

        return JsonResponse({
            "status": 200,
            "obj_id": obj.id
        }, status=200)


class Category_2post(View):
    def post(self, request, *args, **kwargs):
        return HttpResponse('get22 requests')
    

def NewsListView(request):
    object_list = News.objects.all()
    data = []

    for i in object_list:
        data.append(
            {
                "name": i.name,
                "text": i.matn,
                "category": i.bolim.name,
            }
        )

    return JsonResponse(data, safe=False)


@require_http_methods(["POST"])
def add_news(request):
    data = request.POST
    
    object_data = News(name=data['name'], matn=data['text'], bolim=Category.objects.get(id=int(data['bolim'])))
    object_data.save()

    return JsonResponse({
        "status": "Your news has beed added successfully", 
        "object_id": object_data.id
        }, status=201)