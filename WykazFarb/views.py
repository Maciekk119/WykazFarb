from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.template.response import TemplateResponse
from WykazFarb.models import Paint, Paint_Sets, Collection
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from math import floor


class Main(View):
    """This view shows main page"""

    def get(self, request):
        return render(request, 'main.html')


class CatalogueBrands(View):
    """This view in this class shows paints divided by brands"""

    def get(self, request, brand):
        paints = Paint.objects.filter(brand=brand).order_by('id')
        paints_col_number = floor(paints.count()/12)
        paints_rest = paints.count()%12
        print(paints.count())
        print(paints_rest)
        columns = {'paints_1': None, 'paints_2': None, 'paints_3': None,'paints_4': None,
                   'paints_5': None, 'paints_6': None, 'paints_7': None,'paints_8': None,
                   'paints_9': None, 'paints_10': None, 'paints_11': None,'paints_12': None,}
        paints_1 = 'x'
        for i in range(1, 12):
            i = i+1
            print(i)
        return render(request, 'catalogue.html', {'paints': paints, 'paints_1': paints_1})


class CatalogueTypes(View):
    """This view in this class shows paints divided by types"""

    def get(self, request, type):
        paints = Paint.objects.filter(type=type)
        return render(request, 'catalogue.html', {'paints': paints})


class Analog(View):
    """This view shows you equivalent of chosen paint"""

    def get(self, request, id):
        paint = Paint.objects.get(id=id)
        user = request.user
        paintsets = ''
        if user.is_authenticated:
            paintsets = Paint_Sets.objects.filter(user=user)
        return render(request, 'analogs.html', {'paint': paint, 'paintsets': paintsets})

    """This view lets you add paint to your set or your collection"""

    def post(self, request, id):
        user = request.user
        paint = Paint.objects.get(id=id)
        paintset_in = request.POST["paint_set"]
        collection = Collection.objects.get(owner=user)
        collection_contains = collection.contains
        collection_contains.add(paint)
        if paintset_in != 'kolekcja':
            paintset_out = Paint_Sets.objects.get(id=paintset_in)
            paintset_out.paints.add(paint)

        return redirect('/')


class Logging(View):
    """This class creates view that can be used to log in"""

    def get(self, request):
        return render(request, 'logging.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('/')


class Registering(View):
    """This view lets you create new user"""

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            User.objects.create_user(username=username, password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            Collection.objects.create(owner=user)
            return redirect('/')
        else:
            return render(request, 'registration.html', {'form': form, 'message': 'Nieprawidłowy login lub hasło'} )


@login_required
def PaintSets(request):
    """This function shows your paintsets and lets you create new paintset"""
    if request.method == "GET":
        user_id = request.user.id
        farby = []
        paintsets = Paint_Sets.objects.filter(user=user_id)
        kolekcja_id = Collection.objects.get(owner_id=user_id)
        kolekcja = Paint.objects.filter(collection=kolekcja_id)
        for paintset in paintsets:
            id_zestawu = paintset.id
            paints = Paint.objects.filter(paint_sets=id_zestawu)
            zestaw = [paintset, paints]
            farby.append(zestaw)
        return render(request, 'paintsets.html', {'farby': farby, 'kolekcja': kolekcja})

    if request.method == "POST":
        set_name = request.POST['text_input']
        user = request.user
        Paint_Sets.objects.create(name=set_name, user=user)
        link = '/paintsets/?name=1'
        return redirect(link)


class Paints(View):

    def get(self, request):
        user_id = request.user.id
        kolekcja_id = Collection.objects.get(owner_id=user_id)
        kolekcja = Paint.objects.filter(collection=kolekcja_id)
        return render(request, 'paints.html', {'kolekcja': kolekcja})



def Logout(request):
    logout(request)
    return redirect('/')

def xyz():
    pass