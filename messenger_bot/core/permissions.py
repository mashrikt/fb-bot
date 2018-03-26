from rest_framework import permissions

from messenger_bot.settings import VERIFY_TOKEN


class IsFbAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == "GET":
            mode = request.GET.get('hub.mode', '')
            token = request.GET.get('hub.verify_token', '')

            if mode == 'subscribe' and token == VERIFY_TOKEN:
                return True
        return False
