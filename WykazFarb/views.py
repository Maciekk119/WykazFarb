from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.template.response import TemplateResponse
from WykazFarb.models import Paint

# # class SchoolClassView(View):
#     def get(self, request, school_class):
#         klasa = str(int(school_class))
#
#         uczniowie = uczniowie.filter(school_class=klasa)
#         ctx = {'klasa': uczniowie}
#         return TemplateResponse(request, "school_view.html", ctx)
class Main(View):

    def get(self, request):
        return render(request, 'main.html')

class CatalogueBrands(View):
    def get(self, request, brand):

        paints = Paint.objects.filter(brand=brand)
        return render(request, 'catalogue.html', {'paints':paints})

class CatalogueTypes(View):
    def get(self, request, type):

        paints = Paint.objects.filter(type=type)
        return render(request, 'catalogue.html', {'paints':paints})

class Analog(View):
    def get(self, request, id):
        paint = Paint.objects.get(id=id)
        return render(request, 'analogs.html', {'paint':paint})



