import streamlit as st
from datetime import date

st.title("Hukuki Ehliyet (Akli Meleke) Raporu")

# Ortak alanlar
tc = st.text_input("Hasta TC Kimlik No")
ad_soyad = st.text_input("Ad Soyad")
muayene_tarihi = st.date_input("Muayene Tarihi")
belge_turu = st.text_input("Noterde Düzenlenecek Belge Türü (örn: vekaletname, satış sözleşmesi)")

# Başvuru türü
basvuru = st.radio("Başvuru Yolu", ["Noterden yönlendirme", "Kendi dilekçesiyle başvuru"])

if basvuru == "Noterden yönlendirme":
    noter_no = st.text_input("Hangi Noter (örn: 2.)")
    ust_yazi_tarihi = st.date_input("Üst Yazının Tarihi")
    ust_yazi_sayisi = st.text_input("Üst Yazının Sayısı")
    giris_paragraf = f"""T.C. Çorum {noter_no} Noterliğinin {ust_yazi_tarihi.strftime('%d/%m/%Y')} tarih ve {ust_yazi_sayisi} sayılı yazısı ile {belge_turu} tanzim etmek için hukuki ehliyetinin bulunup bulunmadığı hususunda rapor düzenlenmesi için yönlendirilen {tc} T.C. kimlik nolu {ad_soyad}, {muayene_tarihi.strftime('%d/%m/%Y')} tarihinde Hitit Üniversitesi Erol Olçok Eğitim ve Araştırma Hastanesi Psikiyatri Polikliniğinde muayene edilmiştir.\n"""
else:
    dilekce_tarihi = st.date_input("Dilekçe Evrak Tarihi")
    dilekce_sayisi = st.text_input("Dilekçe Evrak Sayısı")
    giris_paragraf = f"""T.C. Sağlık Bakanlığı Erol Olçok Eğitim ve Araştırma Hastanesi Başhekimliğine {dilekce_tarihi.strftime('%d/%m/%Y')} tarihli ve {dilekce_sayisi} sayılı evrak ile kendisine akli meleke raporu verilmesi amacıyla başvuran {tc} T.C. kimlik nolu {ad_soyad}, {muayene_tarihi.strftime('%d/%m/%Y')} tarihinde Hitit Üniversitesi Erol Olçok Eğitim ve Araştırma Hastanesi Psikiyatri Polikliniğinde muayene edilmiştir.\n"""

# Z skoru ve tanı
z_skoru = st.text_input("3MS Z Skoru")
ehliyet_durumu = st.radio("Hukuki Ehliyeti", ["Var", "Yok"])

if ehliyet_durumu == "Var":
    sonuc_paragraf = f"""İlgilinin kendisi ve yakınından alınan anamnez, incelenen tıbbi kayıtları ve yapılan modifiye mini mental test sonucuna göre (3MS z skoru: {z_skoru}) {ad_soyad}'nın hâlihazırda ayırt etme gücünü ve hukuki ehliyetini etkileyecek nitelikte herhangi bir akıl hastalığı veya zayıflığı saptanmadığı, dolayısıyla kişinin rapor talebine esas {belge_turu} tanzim etme işlemini gerçekleştirmek için fiili ehliyetinin bulunduğu kanaati edinilmiştir."""
else:
    tanı = st.selectbox("Tanı", ["demans", "hafif bilişsel bozukluk"])
    sonuc_paragraf = f"""İlgilinin kendisi ve yakınından alınan anamnez, incelenen tıbbi kayıtları ve yapılan modifiye mini mental test sonucuna göre (3MS z skoru: {z_skoru}) {ad_soyad}’ya hâlihazırda ayırt etme gücünü etkileyecek nitelikte {tanı} tanısının konulduğu, bu nedenle ilgilinin {belge_turu} tanzim etme işlemini gerçekleştirmek için fiili ehliyetinin bulunmadığı kanaati edinilmiştir."""

# Sonuç gösterimi
rapor = giris_paragraf + "\n" + sonuc_paragraf
st.text_area("Oluşturulan Rapor", rapor, height=500)
