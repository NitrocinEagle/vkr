from django.contrib import auth


class UsernameMixin(object):
    def get_context_data(self, *args, **kwargs):
        kwargs['username'] = auth.get_user(self.request).username
        return super(UsernameMixin, self).get_context_data(*args, **kwargs)
