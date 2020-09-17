from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('signin', signin, name='login'),
    path('view', picture_view, name='picture_view'),
    path('logout', signout, name="logout")

    # path('', include('home.urls'))
]
