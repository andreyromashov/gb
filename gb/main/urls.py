from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='main'),
    path('administration', views.administration, name='administration'),
    path('berezhlivaya_poliklinika', views.berezhlivaya_poliklinika, name='berezhlivaya_poliklinika'),
    path('callback', views.callback, name='callback'),
    path('clinicheskie_issledovaniya', views.clinicheskie_issledovaniya, name='clinicheskie_issledovaniya'),
    path('contacts', views.contacts, name='contacts'),
    path('license', views.license, name='license'),
    path('order', views.order, name='order'),
    path('otdel_klin_far', views.otdel_klin_far, name='liotdel_klin_farcense'),
    path('pravila_vnutrennego_rasporyadka_dly_potrebitelei', views.pravila_vnutrennego_rasporyadka_dly_potrebitelei, name='pravila_vnutrennego_rasporyadka_dly_potrebitelei'),
    path('regular_gallery', views.regular_gallery, name='regular_gallery'),
    path('history', views.history, name='history'),
    path('rezhim_raboti', views.rezhim_raboti, name='rezhim_raboti'),
    path('ocenit_rab', views.ocenit_rab, name='ocenit_rab'),
    path('inf_o_zacup', views.inf_o_zacup, name='inf_o_zacup'),
    path('o_nas', views.o_nas, name='o_nas'),
    path('svedenia_rezistracii', views.svedenia_rezistracii, name='svedenia_rezistracii'),
    path('otchet_ucher', views.otchet_ucher, name='otchet_ucher'),
    path('otchet_o_povedenii', views.otchet_o_povedenii, name='otchet_o_povedenii'),
    path('otchet_o_rezultatah', views.otchet_o_rezultatah, name='otchet_o_rezultatah'),
    path('zapis_na_priem', views.zapis_na_priem, name='zapis_na_priem'),
    path('info_o_disponserizacii', views.info_o_disponserizacii, name='info_o_disponserizacii'),
    path('school_health', views.school_health, name='school_health'),
    path('inf_o_oms', views.inf_o_oms, name='inf_o_oms'),
    path('uslovia_okazania_mp', views.uslovia_okazania_mp, name='uslovia_okazania_mp'),
    path('contacts', views.contacts, name='contacts'),
    path('lecarstvenoe_obespechenie', views.lecarstvenoe_obespechenie, name='lecarstvenoe_obespechenie'),
    path('kategorii_gragdan', views.kategorii_gragdan, name='kategorii_gragdan'),
    path('poraydok_lekarstv', views.poraydok_lekarstv, name='poraydok_lekarstv'),
    path('spisok_aptek', views.spisok_aptek, name='spisok_aptek'),
    path('med_ekspertiza', views.med_ekspertiza, name='med_ekspertiza'),
    path('pocazatel_kachestva', views.pocazatel_kachestva, name='pocazatel_kachestva'),
    path('tellefon_links', views.tellefon_links, name='tellefon_links'),
    path('pamitka_o_teroristah', views.pamitka_o_teroristah, name='pamitka_o_teroristah'),
    path('uchastok', views.uchastok, name='uchastok'),

]
