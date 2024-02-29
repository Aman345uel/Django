from django.contrib import admin
from django.urls import path
from commerce.views import home, about, contacts, product, toys, clothes, electronics, accessories,submit_form, form_success
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', home, name= 'home'),
    path('about/', about, name= 'about'),
    path('contacts/', contacts, name= 'contact'),
    path('product/', product, name= 'All'),
    path('toys/', toys, name= 'toys'),
    path('clothes/', clothes, name= 'cloth'),
    path('electornics/', electronics, name= 'electro'),
    path('accessories/', accessories, name= 'access'),
    path('submit/', submit_form, name='submit_form'),
    path('success/', form_success, name='form_success'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
