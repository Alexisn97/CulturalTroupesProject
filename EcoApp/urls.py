from django.urls import path

from .views import *

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
  path('fff/',index),
  path('studentform/', StudentForm),
  path('select_student/',select_student),
  path('code/',code),
  path('DeleteStudent/<int:id>/', DeleteStudent),
  path('Updatestudent/<int:id>/',UpdateStudent),






  path('', CulturalTroupes),
  path('search_troupes/',search_troupes),
  path('CulturalSelect/', CulturalSelect),
  path('booking/',booking)

  # path('about/',about),
  # path('Contact/',Contact),
  # path('login/',login),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
