from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from simplemathcaptcha.fields import MathCaptchaField


class SignupForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if settings.CAPTCHA_TYPE == 'simple_math':
            question_template = _('What is %(num1)i %(operator)s %(num2)i? ')
            are_you_a_robot = MathCaptchaField(label=_('Answer this question: '))
        elif settings.CAPTCHA_TYPE == 'recaptcha':
            are_you_a_robot = ReCaptchaField(widget=ReCaptchaWidget())
        else:
            are_you_a_robot = forms.CharField(widget=forms.HiddenInput(), required=False)
        self.fields["are_you_a_robot"] = are_you_a_robot
