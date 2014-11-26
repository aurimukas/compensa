# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import StrictButton, InlineField

from taggit.forms import TagWidget, TagField

from .models import Request

class RequestForm(forms.ModelForm):

    class Meta:
        model = Request
        exclude = ('user',)
        widgets = {
            'requested_reg_numbers': TagWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'request-form'
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('com_local:new_request')
        self.helper.html5_required = True

        self.helper.layout = Layout(
            InlineField('code'),
            'requested_reg_numbers',
            StrictButton(_('Create request'), css_class='btn-default', type='submit'),
        )

        super(RequestForm, self).__init__(*args, **kwargs)
