from django.urls import path
from .views import (
    HomeView,
    DestinationDetailView,
    DestinationCreateView,
    UserBookingsView,
    book_destination,
    add_review,
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    add_comment
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('destination/new/', DestinationCreateView.as_view(), name='destination-create'),
    path('destination/<int:pk>/', DestinationDetailView.as_view(), name='destination-detail'),
    path('destination/<int:pk>/book/', book_destination, name='book-destination'),
    path('destination/<int:pk>/review/', add_review, name='add-review'),
    path('my-bookings/', UserBookingsView.as_view(), name='user-bookings'),
    
    # Blog URLs
    path('blog/', BlogListView.as_view(), name='blog-list'),
    path('blog/new/', BlogCreateView.as_view(), name='blog-create'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/<slug:slug>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    path('blog/<slug:slug>/comment/', add_comment, name='add-comment'),
]
