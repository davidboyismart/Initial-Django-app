from django.http import HttpResponse
from django.urls import path


def home(request):
    return HttpResponse("""<html>
            <head><title>Document</title></head>
            <body>
                <h1><title>Azure Django Lab</title></h1> 
                <p>Hello from azure!</p>
                <p>This Django app is running on Azure app Service.</p>
                <p>Deployed automatically via github actions CI/CD pipeline.</p>
                <p><strong>pipeline is working!</strong></p>
                <h1>Hello World!</h1>
            </body>
            </html>
""")

urlpatterns = [
    path('', home),
]