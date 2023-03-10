from datetime import date

from django.shortcuts import render


all_posts = [
    {
        "slug":"hike-in-mountains",
        "image": "FB.jpg",
        "author":"Wamah",
        "date": date(2021, 12, 21),
        "title": "Mountain Hiking",
        "exerpt": "There's nothing like the views you get fro hiking in the mountains",
        "content": """
            In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. 
            Lorem ipsum may be used as a placeholder before final copy is available
            
            In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. 
            Lorem ipsum may be used as a placeholder before final copy is available
            
            In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. 
            Lorem ipsum may be used as a placeholder before final copy is available
        """
    },
    
    {
        "slug":"hike-the-mountains",
        "image": "FB.jpg",
        "author":"Wamah",
        "date": date(2021, 10, 21),
        "title": "Mountain in The Hiking",
        "exerpt": "There's nothing like the views you get fro hiking in the mountains",
        "content": """
            In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. 
            Lorem ipsum may be used as a placeholder before final copy is available
            
            In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. 
            Lorem ipsum may be used as a placeholder before final copy is available
            
            In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. 
            Lorem ipsum may be used as a placeholder before final copy is available
        """
    },
    
    {
        "slug":"hike-in-the-mountain",
        "image": "FB.jpg",
        "author":"Wamah",
        "date": date(2022, 9, 21),
        "title": "Mountain The Hike",
        "exerpt": "There's nothing like the views you get fro hiking in the mountains",
        "content": """
            In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. 
            Lorem ipsum may be used as a placeholder before final copy is available
            
            In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. 
            Lorem ipsum may be used as a placeholder before final copy is available
            
            In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. 
            Lorem ipsum may be used as a placeholder before final copy is available
        """
    }
]

def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.htm', {"Posts": latest_posts})


def posts(request):
    return render(request, 'blog/all-post.htm', {"all_posts": all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.htm', {"post": identified_post})