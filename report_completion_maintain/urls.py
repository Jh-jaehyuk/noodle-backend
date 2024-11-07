from django.urls import path, include
from rest_framework.routers import DefaultRouter

from report_completion_maintain.controller.views import ResultReportCompletionMaintainView

router = DefaultRouter()
router.register(r"report_completion_maintain", ResultReportCompletionMaintainView, basename="report_completion_maintain")

urlpatterns = [
    path("", include(router.urls)),
    path("create", ResultReportCompletionMaintainView.as_view({"post": "create"}), name="create-result-report-completion-maintain"),
]
