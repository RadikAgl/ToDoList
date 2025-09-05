from rest_framework_simplejwt.authentication import JWTAuthentication

from tasks.models import TGUser


class MyJWTAuthentication(JWTAuthentication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_model = TGUser