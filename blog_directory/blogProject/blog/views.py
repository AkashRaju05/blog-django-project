from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from django.http import Http404
# create yuor index for urls to index page response
# filtr uses | pipe symbol
posts=[
        # for each ids will have url diff  in every detail pags
        {'id':1,'title':'post 1','content': 'Content of Post 1'},
        {'id':2,'title':'post 2','content': 'Content of Post 2'},
        {'id':3,'title':'post 3','content': 'Content of Post 3'},
        {'id':4,'title':'post 4','content': 'Content of Post 4'} ,   ]
def index(request):
    #views.py: We create the variable name and send it to the template through the context dictionary.
    blog_title = 'Latest Posts'
    return render(request,'blog/index.html',{"blog_title": blog_title, 'posts':posts})
def detail(request, post_id):
    post = next(
        (item for item in posts if item['id'] == int(post_id)),
        None
    )
    if post is None:
        raise Http404("Post not found")
    return render(request, 'blog/detail.html', {'post': post})
    # logger = logging.getLogger('TESTING')
    # logger.debug(f'post variable is {post}')

def old_url_redirect(request):
    # why we using reverse beacause 
    # in future if we want to change it manually not possible but can acheive reverse for dynamic
    return redirect(reverse("blog:new_url"))
def new_url_view(request):
    return HttpResponse('this is the new url')