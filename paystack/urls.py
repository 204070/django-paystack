from django.conf.urls import url


from . import settings
from . import views

app_name = 'paystack'
urlpatterns = [
    url(r'^verify-payment/(?P<order>[\w.@+-]+)/$',
        views.verify_payment, name='verify_payment'),
    url(r'^failed-verification/(?P<order_id>[\w.@+-]+)/$',
        views.FailedView.as_view(), name='failed_verification'),
    url(r'^successful-verification/(?P<order_id>[\w.@+-]+)/$',
        views.SuccessView.as_view(),
        name='successful_verification'),
    url(r'^failed-page/$',
        views.TemplateView.as_view(template_name='paystack/failed-page.html'), name='failed_page'),
    url(r'^success-page/$',
        views.TemplateView.as_view(template_name='paystack/success-page.html'), name='success_page'),

]
