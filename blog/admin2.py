
from django.utils.translation import gettext_lazy

from djadmin2 import renderers
from djadmin2.actions import DeleteSelectedAction

# Import your custom models
from djadmin2.site import djadmin2_site
from djadmin2.types import Admin2TabularInline, ModelAdmin2
from .actions import (CustomPublishAction, PublishAllItemsAction,
                      unpublish_items, unpublish_all_items)
from .models import Channel, Post, Comment, Relation, Control


class CommentInline(Admin2TabularInline):
    model = Comment

class ChannelAdmin(ModelAdmin2):
    list_actions = [
        DeleteSelectedAction, CustomPublishAction,
        PublishAllItemsAction, unpublish_items,
        unpublish_all_items,
    ]
    search_fields = ('title')
    list_display = ('title', 'count', 'created')
    field_renderers = {
        'title': renderers.title_renderer,
    }
    save_on_top = True
    date_hierarchy = "created_date"
    ordering = ["-created_date", "title", ]

class PostAdmin(ModelAdmin2):
    list_actions = [
        DeleteSelectedAction, CustomPublishAction,
        PublishAllItemsAction, unpublish_items,
        unpublish_all_items,
    ]
    inlines = [CommentInline]
    search_fields = ('title', '^body')
    list_display = ('title', 'body', 'published', "published_date",)
    field_renderers = {
        'title': renderers.title_renderer,
    }
    save_on_top = True
    date_hierarchy = "published_date"
    ordering = ["-published_date", "title", ]


class CommentAdmin(ModelAdmin2):
    search_fields = ('body', '=post__title')
    list_filter = ['post', ]
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = False

class RelationAdmin(ModelAdmin2):
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = False

class ControlAdmin(ModelAdmin2):
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = False

# Register the blog app with a verbose name
djadmin2_site.register_app_verbose_name(
    'blog',
    gettext_lazy('My Blog')
)

#  Register each model with the admin
djadmin2_site.register(Channel, ChannelAdmin)
djadmin2_site.register(Post, PostAdmin)
djadmin2_site.register(Comment, CommentAdmin)
djadmin2_site.register(Relation, RelationAdmin)
djadmin2_site.register(Control, ControlAdmin)
