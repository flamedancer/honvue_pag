#-*- coding: utf8 -*-

import re
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

RBLANK = re.compile(r'\s+')




# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
# 
# 
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


@python_2_unicode_compatible  # only if you need to support Python 2
class Game(models.Model):
    index = models.IntegerField()
    name = models.CharField(max_length=200)
    bigpicture = models.CharField(max_length=200)
    smpicture = models.CharField(max_length=200)
    showpictures = models.CharField(max_length=200)
    small_desc = models.CharField(max_length=1000)
    main_desc = models.TextField(max_length=20000)
    feature_desc = models.TextField(max_length=20000)
    type_tags = models.CharField(max_length=200)
    IOS_link = models.CharField(max_length=100, default=None, blank=True, null=True)
    ANDROID_link = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_showpictures(self):
        return RBLANK.split(self.showpictures)
    
    def get_type_tags(self):
        return RBLANK.split(self.type_tags)


@python_2_unicode_compatible  # only if you need to support Python 2
class New(models.Model):
    title = models.CharField(max_length=200)
    bigpicture = models.CharField(max_length=200)
    smpicture = models.CharField(max_length=200)
    content = models.TextField(max_length=20000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title


@python_2_unicode_compatible  # only if you need to support Python 2
class JobCategory(models.Model):
    index = models.IntegerField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


@python_2_unicode_compatible  # only if you need to support Python 2
class Job(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=20000)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
