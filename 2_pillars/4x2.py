"""
Make class Http404 callable so that below code works
"""


class Http404:
    def raise_exception(self, message: str = "Error HTTP 404") -> None:
        raise ValueError(message)


error_404 = Http404()
error_404(message="Terrible error HTTP 404")
