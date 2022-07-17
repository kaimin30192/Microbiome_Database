from django.urls import path
from django.urls import path, re_path
from django.views.static import serve
from Database import settings
from .views import (
    analysis_view,
    home_view,
    data_view,
    phenotype_01_select_view,
    phenotype_02_select_view,
    gender_01_select_view,
    gender_02_select_view,
    submit_1_view,
    submit_2_view,
    start_analysis_view
)
re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOTS})
app_name = 'filter'

urlpatterns = [
    path('home/', home_view, name='home_page'),
    path('analysis/', analysis_view, name='analysis_page'),
    path('data/', data_view, name='data_page'),
    path('data_1/', phenotype_01_select_view, name='data_1_page'),
    path('data_2/', phenotype_02_select_view, name='data_2_page'),
    path('gender_1/', gender_01_select_view, name='gender_1_page'),
    path('gender_2/', gender_02_select_view, name='gender_2_page'),
    path('submit_1/', submit_1_view, name='submit_1_page'),
    path('submit_2/', submit_2_view, name='submit_2_page'),
    path('start_analysis/', start_analysis_view, name='start_analysis_page')
]
