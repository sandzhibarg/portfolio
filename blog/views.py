from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-blog_date')[:5] # отображаем только 5 постов с сортировкой по дате (убывание)
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})