from django.urls import path
from .views import Home_view,ProfileList,ProfileCreate,Watch,ShowMovieDetail,ShowMovie
app_name = 'core'

urlpatterns = [
    path('',Home_view.as_view(),name='home'),
    path('profile/',ProfileList.as_view(),name='profile-list'),
    path('profile/create/',ProfileCreate.as_view(),name='profile-create'),
    path('watch/<str:profile_id>/',Watch.as_view(),name='profile-watch'),
    path('movie/detail/<str:movie_id>/',ShowMovieDetail.as_view(),name='movie-detail'),
    path('movie/play/<str:movie_id>/',ShowMovie.as_view(),name='movie-watch'),

]