from django.urls import path,include
from .import views

urlpatterns =[
    path("",views.index_3_home,name = "index_3_home"),
    path('user_login',views.user_login, name = 'user_login'),
    path('user_signup/',views.user_signup,name = "user_signup"),
    path('user_login',views.user_login, name = 'user_login'),
    path('user_logout/',views.user_logout,name="user_logout"),

    path('admin_login/',views.admin_login,name = 'admin_login'),
    path('admin_userlist/',views.admin_userlist,name = 'admin_userlist'),

   path('admin_addproducts/',views.admin_addproducts,name = 'admin_addproducts'),
   path('admin_productslist/',views.admin_productslist,name = 'admin_productslist'),
   path('shop_list_left_books/',views.shop_list_left_books,name = 'shop_list_left_books'),
   path('product_details',views.product_details,name = 'product_details'),
   
   path('admin_logout/',views.admin_logout,name = 'admin_logout'),
   path('admin_addcategory/',views.admin_addcategory,name = 'admin_addcategory'),
   path('admin_categorylist/',views.admin_categorylist,name = 'admin_categorylist'),
   path('userblock/',views.userblock,name = 'userblock'),
   path('admin_updateuser/',views.admin_updateuser,name = 'admin_updateuser'),
   path('admin_editproducts/',views.admin_editproducts,name = 'admin_editproducts'),
   path('admin_editcategory/',views.admin_editcategory,name = 'admin_editcategory'),
   path('admin_deletecategory/',views.admin_deletecategory,name = 'admin_deletecategory'),
    path('admin_deleteproduct/',views.admin_deleteproduct,name = 'admin_deleteproduct'),
   

   path('admin_dashboard/',views.admin_dashboard, name = 'admin_dashboard')





   
   
  
]