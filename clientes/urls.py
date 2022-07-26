from django.urls import path, include
from .views import PersonCreateView, PersonDeleteView, PersonUpdateView, person_delete, person_update, persons_list, person_new, ListPerson, PersonDetail, ProductBulk


urlpatterns = [
    path('list/' , persons_list , name='person_list'),
    path('new/' , person_new , name='person_new'),
    path('update/<int:id>/' , person_update , name='person_update'),
    path('delete/<int:id>/' , person_delete , name='person_delete'),
    path('person_list' , ListPerson.as_view() , name= 'person_list_cbv'),
    path('person_detail/<int:pk>' , PersonDetail.as_view() , name= 'person_detail'),
    path('person_form' , PersonCreateView.as_view() , name= 'person_form_cbv'),
    path('person_form/<int:pk>' , PersonUpdateView.as_view() , name='person_form_update_cbv'),
    path('person_form/<int:pk>/delete' , PersonDeleteView.as_view() , name='person_form_delete_cbv'),
    path('product_bulk', ProductBulk.as_view(), name='product_bulk'),
    path('__debug__/', include('debug_toolbar.urls')),
    
]