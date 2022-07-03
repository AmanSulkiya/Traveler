from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm


urlpatterns = [
  
    path('',views.TourView.as_view(),name="home"),
    path('booking-detail/<int:pk>',views.BookingDetailView.as_view(), name='booking-detail'),
    path('book/', views.book_now, name='book-now'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart, name='showcart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='payment_done'),
    path('accounts/login/', auth_views.LoginView.as_view
    (template_name='app/login.html',
    authentication_form=LoginForm), name='login'),
    path('registration/', views.CustomerRegistrationView.
    as_view(), name="customerregistration"),
    
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('mybookings/', views.mybookings, name='mybookings' ),
    
    path('address/', views.address, name='address'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),
    name='logout'),
    path('passwordchange/',auth_views.PasswordChangeView.
    as_view(template_name='app/passwordchange.html',
    form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
   
    path('passwordchangedone/', auth_views.PasswordChangeView.
    as_view(template_name='app/passwordchangedone.html'),
    name='passwordchangedone'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', 
    form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),

    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact , name='contact'),
    path('flight/', views.flight , name='flight'),
    path('train/', views.train , name='train'),
    path('buses/', views.buses , name='buses'),
    path('strain/',views.TrainView.as_view, name='strain'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
