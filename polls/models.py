# coding=utf-8
import datetime
from django.db import models
from django.utils import timezone


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text

#
# class Users(models.Model):
#     name = models.CharField(u'Имя', max_length=255)
#     paycheck = models.IntegerField(u'Зарплата', default=0)
#     date_joined = models.DateTimeField(u'Дата поступления на работу')
#
#     def __unicode__(self):
#         return self.name
#
#
# class Rooms(models.Model):
#     department = models.CharField(u'Отдел', max_length=255)
#     spots = models.IntegerField(u'Вместимость', default=1)
#
#     def __unicode__(self):
#         return self.department