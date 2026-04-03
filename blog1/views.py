from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    )
 

# posts= [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27,2018'
#     },
#     {
#         'author': 'John Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'September 30,2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 3',
#         'content': 'Third post content',
#         'date_posted': 'October 1,2018'
#     }
# ]


# def home(request):
#     postList= Post.objects.all()
#     return render(request,'blog1/home.html',{'posts':posts})
class PostListView(ListView):
    model = Post
    # default view name is <app>/<model>_<viewtype>.html
    template_name = 'blog1/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
class UserPostListView(ListView):
    model=Post
    # default view name<app>/<model>_<viewtype>.html
    
    template_name='blog1/user_posts.html'
    context_object_name='posts'
    paginate_by=5    
    
    def get_queryset(self):
       user =get_object_or_404(User, username=self.kwargs.get('username'))
       return Post.objects.filter(author=user).order_by('-date_posted')
   
   
class postDetailView(DetailView):
    model=Post
    
class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DeleteView , LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    success_url = '/'  
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class  PostCreateView(LoginRequiredMixin, CreateView):   
    model = Post
    fields = ['title', 'content']   
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request,'blog1/about.html',{'title':'About'})
