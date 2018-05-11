import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator
from django.conf import settings


# Create your views here.
def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, settings.PAGINATOR_NUMBER)
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num)
    currentr_num = page_of_blogs.number
    page_list = list(range(max(currentr_num - settings.EACH_PAGE_SHOW, 1), currentr_num)) + list(range(currentr_num, min(currentr_num + settings.EACH_PAGE_SHOW, paginator.num_pages) + 1))
    if page_list[0] - 1 >= 2:
        page_list.insert(0, '...')
    if paginator.num_pages - page_list[-1] >= 2:
        page_list.append('...')
    if page_list[0] != 1:
        page_list.insert(0, 1)
    if page_list[-1] != paginator.num_pages:
        page_list.append(paginator.num_pages)
    recent_post = Post.objects.all()[:5]
    categories = Category.objects.all()
    return render(request, 'blog/index.html', context={'page_of_blogs': page_of_blogs, 'recent_post':recent_post, 'categories':categories, 'page_list':page_list})


def detail(request, blog_pk):
    post = get_object_or_404(Post, pk=blog_pk)
    post.body = markdown.markdown(post.body, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    recent_post = Post.objects.all()[:5]
    categories = Category.objects.all()
    return render(request, 'blog/detail.html', context={'post': post, 'recent_post':recent_post, 'categories':categories})


def category(request, category_pk):
    category_name = get_object_or_404(Category, pk=category_pk)
    category_post = Post.objects.filter(category=category_name)
    paginator = Paginator(category_post, settings.PAGINATOR_NUMBER)
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num)
    currentr_num = page_of_blogs.number
    page_list = list(range(max(currentr_num - settings.EACH_PAGE_SHOW, 1), currentr_num)) + list(
        range(currentr_num, min(currentr_num + settings.EACH_PAGE_SHOW, paginator.num_pages) + 1))
    if page_list[0] - 1 >= 2:
        page_list.insert(0, '...')
    if paginator.num_pages - page_list[-1] >= 2:
        page_list.append('...')
    if page_list[0] != 1:
        page_list.insert(0, 1)
    if page_list[-1] != paginator.num_pages:
        page_list.append(paginator.num_pages)
    recent_post = Post.objects.all()[:5]
    categories = Category.objects.all()
    return render(request, 'blog/category.html', context={'page_of_blogs': page_of_blogs, 'title': category_name, 'recent_post':recent_post, 'categories':categories, 'page_list':page_list})


def about(request):
    return render(request, 'blog/about.html')