from django.urls import path
from . import views


#from baseapp.views import user_views as views




urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', views.getUserProfile, name="users-profile"),
]

