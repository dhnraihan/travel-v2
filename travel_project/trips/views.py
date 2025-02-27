from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Destination, Booking, Review, BlogPost, Comment
from .forms import BookingForm, ReviewForm, BlogPostForm, CommentForm



class HomeView(ListView):
    model = Destination
    template_name = 'trips/home.html'
    context_object_name = 'destinations'
    ordering = ['-created_at']
    paginate_by = 6



class DestinationDetailView(DetailView):
    model = Destination
    template_name = 'trips/destination_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(destination=self.object).order_by('-created_at')
        context['booking_form'] = BookingForm()
        context['review_form'] = ReviewForm()
        return context



@login_required
def book_destination(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.destination = destination
            booking.total_price = destination.price * booking.number_of_people
            booking.save()
            messages.success(request, 'Your booking has been confirmed!')
            return redirect('destination-detail', pk=pk)
    return redirect('destination-detail', pk=pk)



@login_required
def add_review(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.destination = destination
            review.save()
            messages.success(request, 'Your review has been added!')
    return redirect('destination-detail', pk=pk)



class UserBookingsView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'trips/user_bookings.html'
    context_object_name = 'bookings'
    paginate_by = 10

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-booking_date')



class BlogListView(ListView):
    model = BlogPost
    template_name = 'trips/blog_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        return BlogPost.objects.filter(status='published')


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'trips/blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context



class BlogCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'trips/blog_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'trips/blog_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author



class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'trips/blog_confirm_delete.html'
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


@login_required
def add_comment(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('blog-detail', slug=slug)
    return redirect('blog-detail', slug=slug)


class DestinationCreateView(LoginRequiredMixin, CreateView):
    model = Destination
    fields = ['name', 'description', 'location', 'image', 'price']
    template_name = 'trips/destination_form.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Destination has been created successfully!')
        return super().form_valid(form)
