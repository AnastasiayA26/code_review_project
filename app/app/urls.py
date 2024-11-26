from django.contrib import admin
from django.urls import path
from app.auth.views import login_view
from app.code_review.views import review_code

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('review/', review_code),
]

