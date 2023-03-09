from django.shortcuts import render

# Create your views here.
def starting_page(request):
    return render(request, 'blog/index.htm')


def posts(request):
    return render(request, 'blog/all-post.htm')


def post_detail(request, slug):
    return render(request, 'blog/post-detail.htm', {slug: slug})