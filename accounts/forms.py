from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        models = get_user_model()
        fields = [
            "username",
            "nickname",
            "profile_image",
        ]
        labels = {
            "username": "아이디",
            "nickname": "닉네임",
            "profile_image": "프로필 이미지",
        }


class CustomUserChangeForm(UserChangeForm):
    password = None  # 프로필 변경과 비밀번호 변경을 따로 두기 위함

    class Meta:
        model = get_user_model()
        fields = [
            "nickname",
            "email",
            "profile_image",
        ]
        labels = {
            "nickname": "닉네임",
            "email": "이메일",
            "profile_image": "프로필 이미지",
        }
