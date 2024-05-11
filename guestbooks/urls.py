from django.urls import path
from guestbooks.views import *

urlpatterns = [
    path('', GuestBookListCreate.as_view()),
    path('<int:id>/', GuestBookRetrieveDestroy.as_view()),
]
