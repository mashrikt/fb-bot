from rest_framework import generics, status
from django.http import HttpResponse

from .permissions import IsFbAuthenticated


class WebHookView(generics.ListAPIView):
    permission_classes = [IsFbAuthenticated]

    def get_serializer_class(self):
        pass

    def get_queryset(self):
        pass

    def list(self, request, *args, **kwargs):

        print(self.request.GET)
        return HttpResponse(self.request.GET["hub.challenge"], content_type="text/plain",
                            status=status.HTTP_200_OK)
