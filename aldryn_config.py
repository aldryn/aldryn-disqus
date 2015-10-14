# -*- coding: utf-8 -*-
from aldryn_client import forms


class Form(forms.BaseForm):

    disqus_shortname = forms.CharField('Site shortname')

    def to_settings(self, data, settings):
        settings['DISQUS_SHORTNAME'] = data['disqus_shortname']
        return settings
