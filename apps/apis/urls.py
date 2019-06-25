from django.urls import path

from . import views

urlpatterns = [
    path('objects', views.ObjectsView.as_view(), name='objects_view'),
    path('status', views.StatusView.as_view(), name='status_view'),
    path('objects/<oid>/actions/<aid>', views.StatusView.as_view(), name='status_view'),
    path('wallets/property/<pid>', views.WalletView.as_view(), name='wallet_view'),
    path('wallets/<oid>/actions/<aid>', views.WalletActions.as_view(), name='wallet_actions_view'),
    path('objects/<iid>/publishers/<oid>/events/<eid>', views.WalletEvents.as_view(), name='wallet_events_view'),
    path('handle_tasks', views.TaskView.as_view(), name='tasks_view'),
]