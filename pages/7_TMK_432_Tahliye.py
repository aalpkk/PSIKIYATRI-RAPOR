import streamlit as st
from datetime import date

st.title("TMK 432 - Rıza Dışı Yatış Bildirimi Raporu")

def format_date(dt):
    return dt.strftime("%d/%m/%Y")

# Giriş alanları
tc = st.text_input("T.C. Kimlik Numarası")
ad_soyad = st.text_input("Adı ve Soyadı")
muayene_yeri = st.selectbox("Muayene Yeri", ["Psikiyatri Polikliniği", 
"Psikiyatri Acil", "Servis", "Konsültasyon"])
muayene_tarihi = st.date_input("Muayene Tarihi", value=date.today())
tani = st.text_input("Koyulan Tanı")
yatirildigi_tarih = st.date_input("Yatış Tarihi", value=date.today())

# Rapor oluştur
if st.button("Raporu Oluştur"):
    rapor = f"""
{tc} T.C. Kimlik numaralı {ad_soyad} isimli hasta 
{format_date(muayene_tarihi)} tarihinde Hitit Üniversitesi Erol Olçok 
Eğitim ve Araştırma Hastanesi {muayene_yeri}nde muayene edilmiştir. 
İlgiliye {tani} tanısı koyulmuş olup ruhsal hastalığı nedeniyle kendisine 
veya çevresine zarar verme riski bulunmaktadır. Bu gerekçeyle, Türk Medeni 
Kanunu’nun 432. maddesi uyarınca toplum için tehlike oluşturabileceği ve 
kişisel korunmasının başka yollarla sağlanamayacağı anlaşılmış olup 
{format_date(yatirildigi_tarih)} tarihinde hastanın kendi rızası 
olmaksızın psikiyatri servisine yatışı gerçekleştirilmiştir.

İlgilinin durumu elverir elvermez taburcu edilmek üzere, TMK 432. madde 
kapsamında yatarak tedavisine devam edilmesi için ilgili sulh hukuk 
mahkemesinden izin ve karar alınmasının uygun olduğu kanaatini bildirir 
sağlık kurulu raporudur.
    """

    st.text_area("Oluşturulan Rapor", rapor.strip(), height=500)

