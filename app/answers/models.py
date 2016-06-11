# -*- coding: utf8 -*-
from django.db import models
from app.lessons.models import Lesson
from django.contrib.auth.models import User


class Answer(models.Model):
    lesson = models.ForeignKey(Lesson)
    user = models.ForeignKey(User)
    cpp_file = models.FileField(upload_to='tasks/test_answers/',
                                verbose_name=u'cpp-программа')
    test_pass = models.BooleanField(verbose_name=u'Тестирование пройдено',
                                    blank=True)

    def __str__(self):
        return u'Ответ от пользователя %s к лекции %s' % (
            self.user.username, self.lesson.title)
