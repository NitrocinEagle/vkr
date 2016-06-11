from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from app.lessons.models import Lesson


class TestCase(models.Model):
    lesson = models.ForeignKey(Lesson)
    input = models.FileField(upload_to='tests/inputs/',
                             verbose_name=u'Файл с входными данными',
                             help_text=u'^CIPHER^_test_^N^_in.txt')
    output_etalon = models.FileField(upload_to='tests/etalon_outputs/',
                                     verbose_name=u'Файл с эталонными выходными данными',
                                     help_text=u'^CIPHER^_test_^N^_out_etal.txt')

    def __str__(self):
        return '%s. %s' % (self.id, self.lesson.title)


class TestCaseExample(models.Model):
    lesson = models.ForeignKey(Lesson)
    input = RichTextField(verbose_name=u'Пример входных данных')
    ouput = RichTextField(verbose_name=u'Пример выходных данных')

    def __str__(self):
        return '%s. %s' % (self.id, self.lesson.title)


class TestCasePass(models.Model):
    lesson = models.ForeignKey(Lesson)
    user = models.ForeignKey(User)
    test = models.ForeignKey(TestCase)
    passed = models.BooleanField()

    def __str__(self):
        pre = '[YES]' if self.passed else '[NO]'
        return pre + ' Тест %s. Лекция %s. Пользователь %s.' % (
            self.test.id, self.lesson.title, self.user.username)
