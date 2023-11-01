from django.urls import path, include
from .views import RedirectToLongURLView, URLShorteningView, URLShortenedSuccessView, URListView

urlpatterns = [
    path("<str:s_url>/", RedirectToLongURLView.as_view(), name='redirect-view'),
    path("", URLShorteningView.as_view(), name="url-shortener"),
    path("url/shortened/", URLShortenedSuccessView.as_view(), name="url-shortened"),
    path("url/all/", URListView.as_view(), name="url-all"),
    

]