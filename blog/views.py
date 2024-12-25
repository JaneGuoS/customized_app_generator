from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Channel, Post, Relation, Control

class BlogListView(ListView):
    model = Post

    template_name = 'blog_list.html'
    paginate_by = 10

class ChannelListView(ListView):
    model = Channel

    template_name = 'blog_list.html'
    paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     context = super(ChannelListView, self).get_context_data(**kwargs)
    #     context['posts'] = Post.objects.filter(title='test') //filter as per required
    #     return context

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'


def blog_list(request):
    controls = Control.objects.filter(business_id = 1).filter(control_type = 'User').filter(control_id = request.user.id).values("entity_id")
    relations = Relation.objects.all().filter(business_id = 1).filter(parent_id__in = controls).values("parent_id")
    relations_default = Relation.objects.filter(business_id = 1).filter(relation_type = 'Channel').filter(parent_id = 2).values("entity_id")
    posts = Post.objects.filter(id__in = relations_default).all()
    channels = Channel.objects.filter(id__in = relations).all()
    context = {
        'channels': channels,
        'posts': posts
    }
    return render(request, 'blog/blog_list.html', context) 
