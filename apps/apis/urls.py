from django.urls import path

from . import views

urlpatterns = [
    path('objects', views.ObjectsView.as_view(), name='objects_view'),

    path('wallets/dash/property/<pid>', views.WalletViewDash.as_view(), name='wallet_view_dash'),
    path('wallets/bitcoin/property/<pid>', views.WalletViewBitcoin.as_view(), name='wallet_view_bitcoin'),
    path('repositories/property/<pid>', views.RepositoryView.as_view(), name='repository_view'),

    path('wallets/dash/<oid>/actions/<aid>', views.WalletActionsDash.as_view(), name='wallet_actions_dash_view'),
    path('wallets/bitcoin/<oid>/actions/<aid>', views.WalletActionsBitcoin.as_view(), name='wallet_actions_bitcoin_view'),
    path('repositories/<oid>/actions/<aid>', views.RepositoryActions.as_view(), name='repository_actions_view'),

    path('objects/<iid>/publishers/<oid>/events/<eid>', views.WalletEvents.as_view(), name='wallet_events_view'),
]