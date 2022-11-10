from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "nickname",
            "profile_image",
        )
        labels = {
            "username": "아이디",
            "nickname": "닉네임",
            "profile_image": "프로필 이미지",
        }


class CustomUserChangeForm(UserChangeForm):
    password = None  ## profile_update에서 password를 없애기 위함. exclude로는 안됨.

    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "nickname",
            "profile_image",
        ]
        labels = {
            "email": "이메일",
            "nickname": "닉네임",
            "profile_image": "프로필 이미지",
        }
