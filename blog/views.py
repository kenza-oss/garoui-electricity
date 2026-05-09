from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def post_list(request):
    posts = Post.objects.filter(is_published=True)
    categories = Category.objects.all()
    
    # Filtrer par catégorie si demandé
    category_slug = request.GET.get('category')
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
        
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories,
        'current_category': category_slug
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    # Articles similaires (même catégorie)
    related_posts = Post.objects.filter(category=post.category, is_published=True).exclude(id=post.id)[:3]
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'related_posts': related_posts
    })
