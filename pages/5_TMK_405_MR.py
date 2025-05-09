import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="MenteLex - TMK 405 Zihinsel Yetersizlik (Mental Retardasyon) Nedeniyle",
    page_icon="🧠",  # Bu favicon olarak sekmede görünür
    layout="centered"
)


st.title("TMK 405 - Zihinsel Yetersizlik (Mental Retardasyon) Nedeniyle Vesayet Raporu")

def format_date(date_obj):
    return date_obj.strftime("%d/%m/%Y")

# Üst yazı ve hasta bilgileri
kurum = st.text_input("Üst Yazıyı Gönderen Kurum")
ust_yazi_tarihi = st.date_input("Üst Yazının Tarihi")
ust_yazi_sayisi = st.text_input("Üst Yazının Sayısı")
tc = st.text_input("Hasta TC Kimlik No")
ad_soyad = st.text_input("Adı ve Soyadı")
muayene_tarihi = st.date_input("Muayene Tarihi")

# Bilgi alınan kişi ve gelişimsel bilgiler (çoktan seçmeli)
bilgi_alinan = st.text_input("Bilgi Alınan Kişiler (örn: annesi, kardeşi)")

gelisim_opsiyonlari = [
    "zor doğumla dünyaya geldiği",
    "gelişim basamaklarının yaşıtlarına göre geç ilerlediği",
    "konuşamadığı",
    "gramer ve kelime dağarcığı yönünden sınırlı bir dil yetisiyle konuşabildiği",
    "sadece basit yönergeleri alabildiği",
    "okuma-yazma öğrenemediği",
    "heceleyerek okuyabildiği",
    "kendi adı ve birkaç basit kelimeyi güçlükle yazabildiği",
    "aritmetik işlemleri yapamadığı",
    "yabancılar tarafından kolaylıkla kandırılabildiği",
    "ev ihtiyaçlarını karşılama, sağlık ve ulaşım gibi alanlarda desteğe ihtiyaç duyduğu",
    "gündelik yaşam aktivitelerini yerine getirmek için başkalarının yardımına ihtiyaç duyduğu"
]
gelisim_secimleri = st.multiselect("Gelişimsel ve Eğitimsel Özellikler", options=gelisim_opsiyonlari)
gelisim_metin = ", ".join(gelisim_secimleri)

# Geçmiş rapor bilgisi
rapor_var = st.radio("Geçmişte düzenlenen resmi rapor var mı?", ["Hayır", "Evet"])
if rapor_var == "Evet":
    rapor_kurum = st.text_input("Raporu Düzenleyen Kurum")
    rapor_tarihi = st.date_input("Geçmiş Raporun Tarihi")
    rapor_no = st.text_input("Geçmiş Rapor Numarası")
    rapor_tani = st.text_input("Geçmiş Rapordaki Tanı")
    rapor_turu = st.selectbox("Raporun Türü", ["aslı", "aslı gibi örneği", "fotokopisi"])

# Ruhsal durum ve kurul
mse = st.text_area("Ruhsal Durum Muayenesi", 
    "İlgilinin ruhsal durum muayenesinde giyiminin sosyoekonomik düzeyi ile uyumlu olduğu, "
    "konuşma miktarının ve hızının normal olduğu, duygudurumunun ötimik, duygulanımının uygun olduğu, "
    "çağrışımlarının düzenli olduğu, düşünce içeriğinin fakir olduğu, sanrı ve algı bozukluğunun olmadığı tespit edilmiştir.")


kurul_tarihi = st.date_input("Kurul Tarihi")
kurul_tanisi = st.selectbox("Kurul Tanısı", [
    "Sınırda mental kapasite",
    "Hafif düzeyde mental retardasyon",
    "Orta düzeyde mental retardasyon",
    "Ağır düzeyde mental retardasyon",
    "Çok ağır düzeyde mental retardasyon",
    "Mental retardasyon"
])
zeka_testi = st.selectbox("Uygulanan Zeka Testi", ["Wechsler Yetişkinler İçin Zeka Testi", "Kent EGY Testi"])
iq_puani = st.text_input("IQ Puanı")


# Rapor çıktısı
if st.button("Raporu Oluştur"):
    rapor = f"""
TMK 405 - Vesayet Raporu (Mental Retardasyon)

{kurum}ün {format_date(ust_yazi_tarihi)} tarih ve {ust_yazi_sayisi} sayılı yazısı ile TMK'nın 405. maddesi uyarınca rapor düzenlenmesi için yönlendirilen {tc} T.C. kimlik nolu {ad_soyad}, {format_date(muayene_tarihi)} tarihinde Hitit Üniversitesi Erol Olçok Eğitim ve Araştırma Hastanesi Psikiyatri Heyetinde değerlendirilmiştir.
İlgilinin {bilgi_alinan}, incelenen tıbbi ve adli evraklarından elde edilen bilgilere göre {gelisim_metin}.
"""

    if rapor_var == "Evet":
        rapor += f"İlgiliye {rapor_kurum} tarafından {format_date(rapor_tarihi)} tarih {rapor_no} rapor numarasıyla düzenlenen {rapor_tani} tanısı olduğunu bildirir sağlık kurulu raporunun {rapor_turu} görülmüştür.\n"
        
    rapor += f"""{mse}
İlgiliye uygulanan {zeka_testi} sonucunda ilgilinin IQ puanı {iq_puani} olarak raporlanmıştır.
{format_date(kurul_tarihi)} tarihinde Hitit Üniversitesi Erol Olçok Eğitim ve Araştırma Hastanesi Psikiyatri Sağlık Kurulunda değerlendirilmiştir.

Sonuç: Alınan öykü, incelenen evrak, yapılan muayene ve uygulanan {zeka_testi} sonucunda {ad_soyad}’a {kurul_tanisi} tanısının konduğu, bu tanının ilgilinin TMK'nın 405. maddesi uyarınca vesayet altına alınmasını gerektirir nitelikte bir akıl zayıflığı olduğu, bu nedenle işlerini bizzat göremeyeceği, başkalarının bakım ve yardımına muhtaç olduğu, akıl sağlığının bağımsız ve sağlıklı karar vermeye yetkili olmadığı, hastalığının sürekli olduğu, hâlihazırdaki durumuyla başkalarına zarar vermemekte olup kapatılmasına gerek olmadığı ve mahkemece dinlenmesinde yarar olmadığı kanaatini bildirir sağlık kurulu raporudur.


  
"""

    st.text_area("Oluşturulan Rapor", rapor.strip(), height=600)
