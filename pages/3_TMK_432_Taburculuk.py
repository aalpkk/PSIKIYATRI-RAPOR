import streamlit as st
from datetime import date

st.set_page_config(
    page_title="MenteLex - TMK 432 Taburcu Raporu",
    page_icon="🧠",  # Bu favicon olarak sekmede görünür
    layout="centered"
)


st.title("TMK 432 - Taburcu Raporu")

# Girdiler
kurum = st.text_input("Üst Yazıyı Gönderen Kurum")
karar_tarihi = st.date_input("Mahkeme Yatış Kararının Tarihi")
karar_sayisi = st.text_input("Mahkeme Yatış Kararının Sayısı")

yatış_tarihi = st.date_input("Yatış Tarihi")
taburcu_tarihi = st.date_input("Taburcu Tarihi")

tc = st.text_input("Hasta TC Kimlik No")
ad_soyad = st.text_input("Adı Soyadı")
tani = st.text_input("Tanı")
tedavi = st.text_area("Uygulanan Tedavi", placeholder="örn: risperidon 2 mg/gün ve valproik asit 1000 mg/gün")

# Rapor metni oluştur
if st.button("Raporu Oluştur"):
    rapor = f"""{kurum}nin {karar_tarihi.strftime('%d/%m/%Y')} tarih ve {karar_sayisi} sayılı kararı ile TMK’nın 432. maddesine istinaden {yatış_tarihi.strftime('%d/%m/%Y')} - {taburcu_tarihi.strftime('%d/%m/%Y')} tarihleri arasında Hitit Üniversitesi Erol Olçok Eğitim ve Araştırma Hastanesi Psikiyatri Servisinde yatırılarak izlenen {tc} T.C. Kimlik Numaralı {ad_soyad}’e {tani} tanısı konmuş olup tedavisi {tedavi} şeklinde düzenlenmiştir.

İlgilinin uygulanan tedaviden fayda gördüğünü, halihazırda söz konusu ruhsal hastalığının düzelme halinde olduğunu, bu durumuyla hastanemizden çıkarılmasının ve ikametgahına en yakın psikiyatri kliniğinde ayaktan tedavisinin uygun olduğunu bildirir sağlık kurulu raporudur.
"""
    st.text_area("Oluşturulan Rapor", rapor, height=400)
