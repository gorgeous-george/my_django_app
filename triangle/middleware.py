from triangle.models import HistoryLog


class LogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if "/admin" not in request.path:
            HistoryLog.objects.create(path=request.path, method=request.method)
