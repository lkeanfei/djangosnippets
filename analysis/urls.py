from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sessionlogout/' ,views.SessionLogoutView.as_view()),
    url(r'^sessionverify/' ,views.SessionVerifyView.as_view()),
    url(r'^sessionlogin/' ,views.SessionLoginView.as_view()),
    url(r'^hello-view/' ,views.HelloApiView.as_view()),
    url(r'^sharesview/' ,views.ShareHoldingsView.as_view()),
    url(r'^intraday/' ,views.IntraDayView.as_view()),
    url(r'^price/', views.PriceView.as_view()),
    url(r'^bursapricevol/', views.BursaPriceVolumeView.as_view()),
    url(r'^counters/', views.CountersView.as_view()),
    url(r'^counterdetail/', views.CounterDetailView.as_view()),
    url(r'^security/', views.SecurityView.as_view()),
    url(r'^forecastanalysis/', views.ForecastAnalysisView.as_view()),
    url(r'^securityholdings/', views.SecurityShareholdingsView.as_view()),
    url(r'^frontpage/', views.FrontPageView.as_view()),
    url(r'^frontpagenewhighlow/', views.FrontPageNewHighLowView.as_view()),
    url(r'^frontpagetopgainers/', views.FrontPageTopGainersView.as_view()),
    url(r'^frontpagetoplosers/', views.FrontPageTopLosersView.as_view()),
    url(r'^frontpagevolume/', views.FrontPageVolumeView.as_view()),
    url(r'^frontpagebreakout/', views.FrontPageBreakoutView.as_view()),
    url(r'^company/' ,views.ShareHoldingsView.as_view()),
    url(r'^staticbox/', views.StaticBoxView.as_view()),
    url(r'^staticboxbreakout/', views.StaticBoxBreakoutView.as_view()),
    url(r'^dynamicbox/', views.DynamicBoxView.as_view()),
    url(r'^dynamicboxbreakout/', views.DynamicBoxBreakoutView.as_view()),
    url(r'^marketoverview/', views.MarketOverviewView.as_view()),
    url(r'^tradingdays/', views.TradingDaysView.as_view()),
    url(r'^screener/', views.ScreenerView.as_view()),
    url(r'^ownershareholdings/', views.OwnerShareholdingsView.as_view()),
    url(r'^companyshares/', views.CompanySharesView.as_view()),
    url(r'^activecounters/', views.ActiveCountersView.as_view()),




]