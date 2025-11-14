from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def my_info(request):
    html = """
    <html>
    <head><title>Моя таблиця</title></head>
    <body>
        <h1>Інформація про мене</h1>
        <table border="1" cellpadding="5">
            <tr><th>Ім'я</th><td>Fev1l</td></tr>
            <tr><th>Мова</th><td>Українська, Російська, Англійська</td></tr>
            <tr><th>Інтереси</th><td>Web development, SCADA, IIoT</td></tr>
            <tr><th>Games</th><td>CS2, Battlefild 6, StarCraft 2</td></tr>
            <img src="https://images.steamusercontent.com/ugc/2062124891277536945/27CD18CA6D166A67DBFF23092294E109880185FB/?imw=512&imh=512&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true"
                     alt="мем" width="200">
        </table>
    </body>
    </html>
    """
    return HttpResponse(html)
