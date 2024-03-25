from django.urls import path,include
from.import views
from apiproject2app.views import ActiveSampleList,ActiveSampleDetails


urlpatterns = [
     path('samples/',ActiveSampleList.as_view(),name='ActiveSampleList'),
    path('samples/<int:pk>/',ActiveSampleDetails.as_view(),name='ActiveSampleDetail')
    
]
