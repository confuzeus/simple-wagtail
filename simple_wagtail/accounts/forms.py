from wagtail.admin.forms.auth import LoginForm as WagtailLoginForm
from allcaptcha.mixins import CaptchaFormMixin

class LoginForm(CaptchaFormMixin, WagtailLoginForm):
    pass
