from django.urls import path
from .views import AddEmail, AddTutor, Index
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', AddEmail.as_view(), name="cover"),
    path('careers/', AddTutor.as_view(), name="careers"),
    # path('favicon.ico', RedirectView.as_view(
    #     url=staticfiles_storage.url('res/favicon.ico')))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
