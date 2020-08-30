from django.urls import path
from .views import AddEmail, AddTutor, Index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', AddEmail.as_view(), name="cover"),
    path('careers/', AddTutor.as_view(), name="careers"),
    # path('cover/', Index.as_view(), name="cover"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
