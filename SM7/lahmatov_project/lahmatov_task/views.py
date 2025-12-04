from django.http import HttpResponse
from django.shortcuts import render
from .models import CarsBrand, CarsInfo

def install(request):
    CarsInfo.objects.all().delete()
    CarsBrand.objects.all().delete()

    brands = [
        {"BRAND_NAME": "Tesla", "BRAND_COUNTRY": "USA", "BRAND_RATING": 10},
        {"BRAND_NAME": "Audi", "BRAND_COUNTRY": "Germany", "BRAND_RATING": 9},
        {"BRAND_NAME": "Honda", "BRAND_COUNTRY": "Japan", "BRAND_RATING": 8},
        {"BRAND_NAME": "Toyota", "BRAND_COUNTRY": "Japan", "BRAND_RATING": 9},
        {"BRAND_NAME": "Ford", "BRAND_COUNTRY": "USA", "BRAND_RATING": 8},
        {"BRAND_NAME": "BMW", "BRAND_COUNTRY": "Germany", "BRAND_RATING": 9},
        {"BRAND_NAME": "Mercedes", "BRAND_COUNTRY": "Germany", "BRAND_RATING": 9},
    ]

    cars = [
        {"CAR_NAME": "Model S", "CAR_MODEL": "2024", "CAR_PRICE": 90000, "CAR_BRAND": "Tesla"},
        {"CAR_NAME": "A6", "CAR_MODEL": "2023", "CAR_PRICE": 55000, "CAR_BRAND": "Audi"},
        {"CAR_NAME": "Civic", "CAR_MODEL": "2022", "CAR_PRICE": 25000, "CAR_BRAND": "Honda"},
        {"CAR_NAME": "Corolla", "CAR_MODEL": "2023", "CAR_PRICE": 20000, "CAR_BRAND": "Toyota"},
        {"CAR_NAME": "Mustang", "CAR_MODEL": "2022", "CAR_PRICE": 35000, "CAR_BRAND": "Ford"},
        {"CAR_NAME": "X5", "CAR_MODEL": "2023", "CAR_PRICE": 60000, "CAR_BRAND": "BMW"},
        {"CAR_NAME": "E-Class", "CAR_MODEL": "2023", "CAR_PRICE": 65000, "CAR_BRAND": "Mercedes"},
        {"CAR_NAME": "Camry", "CAR_MODEL": "2024", "CAR_PRICE": 28000, "CAR_BRAND": "Toyota"},
        {"CAR_NAME": "Accord", "CAR_MODEL": "2023", "CAR_PRICE": 27000, "CAR_BRAND": "Honda"},
        {"CAR_NAME": "F-150", "CAR_MODEL": "2024", "CAR_PRICE": 40000, "CAR_BRAND": "Ford"},
    ]

    messages = ["🧹 Старі записи видалено."]

    for b in brands:
        obj = CarsBrand.objects.create(
            BRAND_NAME=b["BRAND_NAME"],
            BRAND_COUNTRY=b["BRAND_COUNTRY"],
            BRAND_RATING=b["BRAND_RATING"]
        )
        messages.append(f"✅ Створено бренд: {obj.BRAND_NAME}")

    for c in cars:
        brand = CarsBrand.objects.get(BRAND_NAME=c["CAR_BRAND"])
        obj = CarsInfo.objects.create(
            CAR_NAME=c["CAR_NAME"],
            CAR_MODEL=c["CAR_MODEL"],
            CAR_PRICE=c["CAR_PRICE"],
            CAR_BRAND=brand
        )
        messages.append(f"🚗 Створено авто: {obj}")

    return HttpResponse("<br>".join(messages))


def duikt_page_lahmatov(request):
    cars = CarsInfo.objects.select_related('CAR_BRAND').all()
    return render(request, 'duikt_page_lahmatov.html', {'cars': cars})
