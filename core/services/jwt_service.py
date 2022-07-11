from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

from rest_framework_simplejwt.tokens import BlacklistMixin, Token

from core.enums.action_enum import ActionEnum
from core.exceptions.jwt_exception import JwtException

UserModel = get_user_model()


class ActivateToken(BlacklistMixin, Token):
    lifetime = ActionEnum.ACTIVATE.exp_time
    token_type = ActionEnum.ACTIVATE.token_type


class RecoveryPassword(BlacklistMixin, Token):
    lifetime = ActionEnum.RECOVERY_PASSWORD.exp_time
    token_type = ActionEnum.RECOVERY_PASSWORD.token_type


class JwtService:
    @staticmethod
    def create_activate_token(user):
        return ActivateToken.for_user(user)

    @staticmethod
    def create_recovery_password_token(user):
        return RecoveryPassword.for_user(user)

    @staticmethod
    def validate_activate_token(token):
        try:
            action_token = ActivateToken(token)
            action_token.check_blacklist()
        except Exception:
            raise JwtException
        action_token.blacklist()
        user_id = action_token.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)

    @staticmethod
    def validate_recovery_password_token(token):
        try:
            action_token = RecoveryPassword(token)
            action_token.check_blacklist()
        except Exception:
            raise JwtException
        action_token.blacklist()
        user_id = action_token.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)
