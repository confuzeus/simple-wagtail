from allcaptcha.mixins import CaptchaFormMixin
from wagtail.admin.forms.auth import LoginForm as WagtailLoginForm


class LoginForm(CaptchaFormMixin, WagtailLoginForm):
    pass
