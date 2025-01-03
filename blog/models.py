from django.db import models
from django.utils.translation import gettext_lazy as _


class Control(models.Model):
    business_id = models.IntegerField(verbose_name=_('businessId'))
    control_type = models.CharField(max_length=255, verbose_name=_('controlType')) 
    control_id = models.IntegerField(verbose_name=_('controlId')) 
    entity_id = models.IntegerField(verbose_name=_('entityId')) 

    class Meta:
        verbose_name = _('control')
        verbose_name_plural = _('controls')

class Relation(models.Model):
    business_id = models.IntegerField(verbose_name=_('businessId'))
    relation_type = models.CharField(max_length=255, verbose_name=_('relationType')) 
    parent_id = models.IntegerField(verbose_name=_('parentId')) 
    entity_id = models.IntegerField(verbose_name=_('entityId')) 

    class Meta:
        verbose_name = _('relation')
        verbose_name_plural = _('relations')

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    body = models.TextField(verbose_name=_('body'))
    published = models.BooleanField(default=False, verbose_name=_('published'))
    published_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class Channel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    status = models.CharField(max_length=255, verbose_name=_('status')) 
    created_date = models.DateField(blank=True, null=True)
    count = models.IntegerField(verbose_name=_('count'))
    
      
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('channel')
        verbose_name_plural = _('channels')

class Comment(models.Model):
    post = models.ForeignKey(
        Post, verbose_name=_('post'), related_name="comments",
        on_delete=models.CASCADE)
    body = models.TextField(verbose_name=_('body'))

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


# Models needed for testing NestedObjects

class Count(models.Model):
    num = models.PositiveSmallIntegerField()
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.num)


class Event(models.Model):
    date = models.DateTimeField(auto_now_add=True)


class Location(models.Model):
    event = models.OneToOneField(
        Event, verbose_name='awesome event',
        on_delete=models.CASCADE
    )


class Guest(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "awesome guest"


class EventGuide(models.Model):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
