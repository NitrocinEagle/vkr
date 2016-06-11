from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)

    error_css_class = 'class-error'
    required_css_class = 'class-required'

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # adding css classes to widgets without define the fields:
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['label'] = 'Пароль'

    def as_div(self):
        return self._html_output(
            normal_row=u'<div%(html_class_attr)s>%(label)s %(field)s %(help_text)s %(errors)s</div>',
            error_row=u'<div class="error">%s</div>',
            row_ender='</div>',
            help_text_html=u'<div class="help-text">%s</div>',
            errors_on_separate_row=False)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'last_name', 'first_name', 'study_group',)

    error_css_class = 'class-error'
    required_css_class = 'class-required'

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # adding css classes to widgets without define the fields:
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def as_div(self):
        return self._html_output(
            normal_row=u'<div%(html_class_attr)s>%(label)s %(field)s %(help_text)s %(errors)s</div>',
            error_row=u'<div class="error">%s</div>',
            row_ender='</div>',
            help_text_html=u'<div class="help-text">%s</div>',
            errors_on_separate_row=False)
