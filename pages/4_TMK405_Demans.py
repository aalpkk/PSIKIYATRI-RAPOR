import streamlit as st
from datetime import datetime

st.title("TMK 405 - Vesayet (Vasi Tespiti) Raporu")

def format_date(date_obj):
    return date_obj.strftime("%d/%m/%Y")

# Girişler
kurum = st.text_input("Üst Yazıyı Gönderen Kurum")
ust_yazi_tarihi = st.date_input("Üst Yazının Tarihi")
ust_yazi_sayisi = st.text_input("Üst Yazının Sayısı")
tc = st.text_input("Hasta TC Kimlik No")
ad_soyad = st.text_input("Adı ve Soyadı")
muayene_tarihi = st.date_input("Muayene Tarihi")

sikayet_suresi = st.text_input("Bilişsel Şikayetlerin Süresi (örn: yaklaşık 3 yıldır)")

tedavi_durumu = st.radio("İlaç Tedavi Bilgisi", ["Hiç kullanmamış", "Geçmişte kullanmış", "Hâlihazırda kullanıyor"])
if tedavi_durumu != "Hiç kullanmamış":
    tedavi_tanisi = st.text_input("Tedavi Tanısı")
    ilac_adi = st.text_input("İlaç Adı")
    ilac_dozu = st.text_input("İlaç Dozu")
    ilac_zamani = st.text_input("Kullanım Zamanı (örn: 2022-2023 arası)")

rapor_var = st.radio("Geçmişte düzenlenen resmi rapor var mı?", ["Hayır", "Evet"])
if rapor_var == "Evet":
    rapor_kurum = st.text_input("Raporu Düzenleyen Kurum")
    rapor_tarihi = st.date_input("Geçmiş Raporun Tarihi")
    rapor_no = st.text_input("Geçmiş Rapor Numarası")
    rapor_tani = st.text_input("Geçmiş Rapordaki Tanı")
    rapor_turu = st.selectbox("Raporun Türü", ["aslı", "aslı gibi örneği", "fotokopisi"])

mse = st.text_area("Ruhsal Durum Muayenesi", "İlgilinin ruhsal durum muayenesinde duygudurumunun ötimik, duygulanımının uygun olduğu, çağrışımlarının düzenli olduğu, düşünce içeriğinin fakir olduğu, sanrı ve algı bozukluğunun olmadığı, bellek ve yönelim bozukluğunun bulunduğu tespit edilmiştir.")

derece = st.selectbox("Modifiye Mini Mental Test Bozukluk Derecesi", ["hafif", "orta", "ağır"])
kurul_tarihi = st.date_input("Kurul Tarihi")
kurul_tanisi = st.text_input("Kurul Tanısı")

if st.button("Raporu Oluştur"):
    rapor = f"""
TMK 405 - Vesayet Raporu

{kurum}ün {format_date(ust_yazi_tarihi)} tarih ve {ust_yazi_sayisi} sayılı yazısı ile {yonlendirme_nedeni} için yönlendirilen {tc} T.C. kimlik nolu {ad_soyad}, {format_date(muayene_tarihi)} tarihinde Hitit Üniversitesi Erol Olçok Eğitim ve Araştırma Hastanesi Psikiyatri Polikliniğinde muayene edilmiştir.
İlgilinin kendisinden, kız kardeşinden, incelenen tıbbi ve adli evraklarından elde edilen bilgilere göre {ad_soyad}’nın {sikayet_suresi}dır bilişsel şikâyetlerinin olduğu, bu bilişsel gerileme nedeniyle gündelik yaşam aktivitelerini yerine getirmek için başkalarının yardımına ihtiyaç duyduğu öğrenilmiştir.
"""

    if tedavi_durumu == "Hiç kullanmamış":
        rapor += "İlgilinin incelenen tıbbi kayıtlarından geçmişte veya halihazırda bilişsel bozuklukla ilgili herhangi bir ilaç tedavisi kullanmadığı anlaşılmıştır.\n"
    else:
        rapor += f"İlgilinin {ilac_zamani} süresince {tedavi_tanisi} tanısı ile {ilac_adi} {ilac_dozu} kullandığı anlaşılmıştır.\n"

    if rapor_var == "Evet":
        rapor += f"İlgiliye {rapor_kurum} tarafından {format_date(rapor_tarihi)} tarih {rapor_no} rapor numarasıyla düzenlenen {rapor_tani} tanısı olduğunu bildirir sağlık kurulu raporunun {rapor_turu} görülmüştür.\n"

    rapor += f"""{mse}
İlgiliye uygulanan modifiye mini mental test sonucunda ilgilinin genel bilişsel performansında {derece} derecede bozulma olduğu belirlenmiştir.

Sonuç: Alınan öykü, incelenen evrak, yapılan muayene ve uygulanan modifiye mini mental test sonucunda {ad_soyad}’a {kurul_tanisi} tanısının konduğu, bu tanının ilgilinin TMK'nın 405. maddesi uyarınca vesayet altına alınmasını gerektirir nitelikte bir akıl zayıflığı olduğu, bu nedenle işlerini bizzat göremeyeceği, başkalarının bakım ve yardımına muhtaç olduğu, akıl sağlığının bağımsız ve sağlıklı karar vermeye yetkili olmadığı, hastalığının sürekli olduğu, hâlihazırdaki durumuyla başkalarına zarar vermemekte olup kapatılmasına gerek olmadığı ve mahkemece dinlenmesinde yarar olmadığı kanaatini bildirir sağlık kurulu raporudur.
"""

    st.text_area("Oluşturulan Rapor", rapor.strip(), height=600)
