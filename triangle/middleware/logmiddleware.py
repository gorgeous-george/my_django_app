from django.utils.deprecation import MiddlewareMixin

from triangle.models import HistoryLog


class LogMiddleware(MiddlewareMixin):

    def _init_(self, get_response):
        self.get_response = get_response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if "/admin" not in request.path:
            HistoryLog.objects.create(path=request.path, method=request.method)
