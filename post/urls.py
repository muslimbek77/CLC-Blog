from django.urls import path, include
from post.views import PopularPostsView,ForYouPostsView,PostDetailView
urlpatterns = [
    path('popular/', PopularPostsView.as_view()),
    path('foryou/', ForYouPostsView.as_view()),
    path('detail/', PostDetailView.as_view()),

]
