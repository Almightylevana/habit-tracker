from rest_framework.routers import DefaultRouter
from .views import HabitViewSet, HabitEntryViewSet

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habit')
router.register(r'entries', HabitEntryViewSet, basename='entry')

urlpatterns = router.urls

