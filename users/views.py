from django.shortcuts import render, redirect
from django.contrib import messages
from post.models import Posts
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.models import User

# class Profile(DetailView):
#     template_name = 'users/profile.html'
#     queryset = Posts.objects.all()
#     def get_object(self):
#         id_ = self.kwargs.get("username")
#         user = get_object_or_404(User, username=id_)
#         return user

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# @login_required
# def profile(request):
#     context = {
#         'posts':Posts.objects.all()
#     }
#     return render(request,'users/profile.html',context)

class PostListView(ListView):
    model = Posts
    template_name = 'users/profile.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    def get_object(self):
        id_ = self.kwargs.get("username")
        user = get_object_or_404(User, username=id_)
        return user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False