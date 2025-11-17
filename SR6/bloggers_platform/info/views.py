from django.http import HttpResponse, HttpResponseNotFound
from .data import BloggersData

data = BloggersData()  # ОБОВ’ЯЗКОВО: створюємо екземпляр

def home(request):
    return HttpResponse("""
        <h1>Головна сторінка</h1>
        <p>Актуальні новини світу блогерів</p>
        <a href='/profiles/'>Переглянути блогерів</a> |
        <a href='/news/'>Новини</a>
    """)

def profiles(request):
    bloggers = data.get_all()
    html = "<h2>Наші блогери</h2><table border='1'>"
    html += "<tr><th>№</th><th>Категорія</th><th>Ім'я</th><th>Опис</th></tr>"
    for i, b in enumerate(bloggers, start=1):
        html += f"<tr><td><a href='/profiles/{i}/'>{i}</a></td><td>{b['category']}</td><td>{b['name']}</td><td>{b['description']}</td></tr>"
    html += "</table>"
    return HttpResponse(html)

def profile_detail(request, blogger_id):
    try:
        blogger = data.get_by_id(int(blogger_id))
        if blogger:
            return HttpResponse(f"""
                <h1>{blogger['name']}</h1>
                <p>Категорія: {blogger['category']}</p>
                <p>{blogger['description']}</p>
                <p><a href='{blogger['social']}'>Соцмережа</a></p>
                <a href='/profiles/'>Назад до списку</a>
            """)
        else:
            return HttpResponseNotFound("<h1>404: Блогер не знайдений</h1>")
    except ValueError:
        return HttpResponseNotFound("<h1>404: Невірний ID</h1>")


def news(request):
    news_list = [
        {"title": "ТехноЇжак запустив новий проект по ПК", "date": "2025-11-15", "source": "YouTube"},
        {"title": "Марія Волжанка відвідала Францію — новий влог уже онлайн", "date": "2025-11-14", "source": "Instagram"},
        {"title": "zWORMz Gaming запустив 5090 на BLACK OPS 7 в 4к", "date": "2025-11-14", "source": "YouTube"},
        {"title": "Petrenko запустив стрим на твичі", "date": "2025-11-14", "source": "Twitch"},
        {"title": "Після обновлення КС2 все пішло коту під хвіст", "date": "2025-11-10", "source": "Global"},
    ]
    html = "<h1>Останні новини</h1><table border='1'>"
    html += "<tr><th>Заголовок</th><th>Дата</th><th>Джерело</th></tr>"
    for item in news_list:
        html += f"<tr><td>{item['title']}</td><td>{item['date']}</td><td>{item['source']}</td></tr>"
    html += "</table><br><a href='/'>Назад на головну</a>"
    return HttpResponse(html)