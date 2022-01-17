
# from .views import book_list, book_details
#from .views import BookList, BookDetails


from django.urls import path, include
from .views import BookViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', BookViewSet, basename = 'books')
router.register('users', UserViewSet)

urlpatterns = [

    path('api/', include(router.urls)),


    # path('books/', BookList.as_view()),
    # path('books/<int:id>/', BookDetails.as_view()),

    # path('books/', book_list),
    # path('books/<int:pk>/', book_details),
    
]
