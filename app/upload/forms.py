# -*- coding: utf8 -*-
import subprocess
from django import forms


class UploadAnswerForm(forms.Form):
    answer_file = forms.FileField(label=u'cpp-файл с программой')

    def handle_uploaded_file(self, file, prefix, dir):
        file_path = dir + '/media/answers/' + prefix + '_' + str(file)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return file_path

    def make_test(self, script, cpp, input, etalon, base_dir):
        result = subprocess.call(
            "cd / && ./%s %s %s %s %s" % (script, cpp, input, etalon, base_dir),
            shell=True)
        return result
