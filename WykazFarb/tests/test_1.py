from WykazFarb.views import Main, Paint_Sets, CatalogueBrands, Logging, Analog, Paint, User, Collection
import pytest
from django.test import Client
from WykazFarb.models import Paint_Sets

@pytest.fixture
def client():
    client = Client()
    return client

def test_main(client):

    response = client.get('/')
    assert response.status_code == 200

def test_registering(client):

    response = client.get('/registering/')
    assert response.status_code == 200


@pytest.fixture
def paint():
    paint = Paint.objects.create(name="Ochre", brand=1, type=1)
    return paint

@pytest.mark.django_db
def test_paint_model1(paint):
    assert Paint.objects.get(name="Ochre") == paint

@pytest.mark.django_db
def test_paint_model2(paint):
    assert len(Paint.objects.all()) == 1

@pytest.fixture
def paintset():
    user = User.objects.create(username='Zdzisław')
    paintset = Paint_Sets.objects.create(name="Nietoperz", user=user)
    return paintset

@pytest.mark.django_db
def test_paintset_model1(paintset):
    assert Paint_Sets.objects.get(name="Nietoperz") == paintset


@pytest.mark.django_db
def test_paintset_model2(paintset):
    assert len(Paint_Sets.objects.all()) == 1



@pytest.mark.django_db
def test_login(client):
    response = client.get('/accounts/login/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_katalog1(client):
    response = client.get('/katalog/brand/1')
    assert response.status_code == 200

@pytest.mark.django_db
def test_katalog2(client):
    response = client.get('/katalog/brand/2')
    assert response.status_code == 200

@pytest.mark.django_db
def test_katalog3(client):
    response = client.get('/katalog/brand/3')
    assert response.status_code == 200

@pytest.mark.django_db
def test_katalog_type1(client):
    response = client.get('/katalog/type/1')
    assert response.status_code == 200

@pytest.mark.django_db
def test_katalog_type2(client):
    response = client.get('/katalog/type/2')
    assert response.status_code == 200

@pytest.mark.django_db
def test_katalog_type3(client):
    response = client.get('/katalog/type/3')
    assert response.status_code == 200

@pytest.mark.django_db
def test_katalog_type4(client):
    response = client.get('/katalog/type/4')
    assert response.status_code == 200

@pytest.mark.django_db
def test_katalog_type5(client):
    response = client.get('/katalog/type/5')
    assert response.status_code == 200

@pytest.mark.django_db
def test_katalog_type6(client):
    response = client.get('/katalog/type/6')
    assert response.status_code == 200
