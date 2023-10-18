from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from WykazFarb.models import Paint, Paint_Sets, Collection
from django.shortcuts import render, redirect
# Create your views here.
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
        return redirect("/paintsets")