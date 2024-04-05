from django.urls import path
from . import views

urlpatterns = [
    #add paths for api functions
    path('ProductItems/', views.getProductItems),
    path('ProductItem/<int:pk>', views.getProductItem.as_view()),
    path('RegisteredVendos/',views.getRegisteredVendo),
    path('addProductItems/', views.addProductItems.as_view()),
    path('registerVendos/', views.RegisterVendos),
    #path('',''),
]

#Note:
# add '.as_view()' if view has generic API class~