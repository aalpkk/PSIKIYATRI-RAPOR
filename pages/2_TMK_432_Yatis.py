import streamlit as st
from datetime import date

st.title("TMK 432 - Akıl Hastalığı Nedeniyle Zorunlu Yatış Kararı")

# Üst yazı bilgileri
kurum = st.text_input("Üst Yazıyı Gönderen Kurum")
ust_yazi_tarihi = st.date_input("Üst Yazının Tarihi")
ust_yazi_sayisi = st.text_input("Üst Yazının Sayısı")
tc = st.text_input("Hasta TC Kimlik No")
ad_soyad = st.text_input("Adı ve Soyadı")
rapor_tarihi = st.date_input("Rapor Tarihi")
anamnez = st.text_area("Anamnez")

# Tanı ve karar seçenekleri
tani = st.text_input("Tanı (varsa)")
karar = st.radio("Rapor Sonucu", [
    "Yatış gerekli (kendisi ve toplum için tehlike)", 
    "Herhangi bir bozukluk yok", 
    "Mental retardasyon var, yatış gerekmez", 
    "Diğer ruhsal bozukluk, yatış gerekmez"
])

# ↓ Ruhsal durum muayenesi bileşenleri
st.markdown("### Ruhsal Durum Muayenesi")
duygudurum = st.selectbox("Duygudurum", ["çökkün", "disforik", "anksiyöz", "öforik", "coşkulu", "taşkın", "ötimik"])
duygulanim = st.selectbox("Duygulanım", [
    "uygun", "uygunsuz", "düzleşmiş", "küntleşmiş", "sığ", 
    "çökkünlük yönünde artmış", "taşkınlık yönünde artmış"
])
cagrisimlar = st.multiselect("Çağrışım Özellikleri", [
    "çağrışımlarının düzenli", "çağrışımlarında hızlanma", "çağrışımlarında yavaşlama",
    "çağrışımlarında gevşeme", "çağrışımlarında teğetsellik", "çağrışımlarında çevresellik",
    "düşünce sürecinde enkoherans", "basınçlı konuşmasının", "fikir uçuşmalarının",
    "clang çağrışımlarının", "düşünce sürecinde perseverasyonların", "düşünce sürecinde blokların"
])
sanrilar = st.multiselect("Sanrılar", [
    "büyüklük", "kötülük görme", "alınma", "düşünce sokulması", "düşünce okunması",
    "düşünce çalınması", "düşünce yayınlanması", "somatik edilginlik", "duygudulanımın edilginliği",
    "dürtünün edilginliği", "iradenin edilginliği", "erotomanik", "küçüklük", "nihilistik",
    "sadakatsizlik", "somatik", "hipokondriak", "enfestasyon"
])
varsanilar = st.multiselect("Varsanılar", ["işitme", "görme", "taktil"])
zeka = st.selectbox("Zeka (Soyutlama)", ["soyutlamasının bozuk olduğu", "soyutlamasının olağan olduğu"])

# ↓ Ruhsal durum metni oluştur
# ↓ Ruhsal durum metni oluştur (maksimum 2 seçim + gramer uyumlu)
mse = f"İlgilinin {rapor_tarihi.strftime('%d/%m/%Y')} tarihindeki ruhsal durum muayenesinde duygudurumunun {duygudurum}, duygulanımının {duygulanim} olduğu"

# En fazla 2 seçenekle sınırlama
cagrisimlar_kisa = cagrisimlar[:2]
sanrilar_kisa = sanrilar[:2]
varsanilar_kisa = varsanilar[:2]

# Düşünce süreci
if cagrisimlar_kisa:
    cagrisim_metin = ", ".join(cagrisimlar_kisa)
    mse += f", düşünce sürecinde {cagrisim_metin} olduğu"
else:
    mse += ", çağrışımlarının düzenli olduğu"

# Sanrılar
if sanrilar_kisa:
    sanri_metin = ", ".join(sanrilar_kisa)
    mse += f", {sanri_metin} sanrıları bulunduğu"
else:
    mse += ", sanrı boyutunda düşünce içeriği bulunmadığı"

# Varsanılar
if varsanilar_kisa:
    varsanilar_metin = ", ".join(varsanilar_kisa)
    mse += f", {varsanilar_metin} varsanısı bulunduğu"
else:
    mse += ", algı bozukluğu olmadığı"

# Zeka (soyutlama)
mse += f", {zeka} tespit edilmiştir."


# ↓ Sonuç metni seçimi
if karar == "Yatış gerekli (kendisi ve toplum için tehlike)":
    sonuc = f"İlgiliye {tani} tanısı koyulmuş olup, kişinin söz konusu akıl hastalığı nedeniyle kendisi ve toplum açısından tehlikelilik oluşacağından TMK'nin 432. maddesi uyarınca tıbbi durumu elverir vermez çıkarılmak üzere kapalı psikiyatri servisi bulunan bir sağlık kurumunda yatarak tedavi görmesinin uygun olduğunu bildirir sağlık kurulu raporudur."

elif karar == "Herhangi bir bozukluk yok":
    sonuc = "Alınan öykü, incelenen evrak ve yapılan muayene sonucunda ilgilinin TMK'nın 432. maddesi uyarınca hastanede yatmasını gerektirecek nitelikte herhangi bir akıl hastalığı, akıl zayıflığı, alkol ya da madde bağımlılığı saptanmadığını bildirir rapordur."

elif karar == "Mental retardasyon var, yatış gerekmez":
    sonuc = "Alınan öykü, incelenen evrak ve yapılan muayene sonucunda ilgiliye mental retardasyon tanısı konulmuş olup bu tanının bir akıl zayıflığı olmakla birlikte ilgilinin halihazırdaki durumuyla toplum için tehlike oluşturmadığı, tedavi, eğitim veya ıslahının mümkün olmadığı, haliyle bir kuruma yerleştirilmesine veya alıkonulmasına gerek olmadığı kanaatini bildirir sağlık kurulu raporudur."

else:
    sonuc = f"Alınan öykü, incelenen evrak ve yapılan muayene sonucunda ilgiliye {tani} tanısı konulmuş olup bu tanının bir akıl hastalığı olmakla birlikte ilgilinin halihazırdaki durumuyla toplum için tehlike oluşturmadığı, tedavi, eğitim veya ıslahı için bir kuruma yerleştirilmesine veya alıkonulmasına gerek olmadığı kanaatini bildirir sağlık kurulu raporudur."

# Tüm metni birleştir
tam_rapor = f"""{kurum}un {ust_yazi_tarihi.strftime('%d/%m/%Y')} tarih ve {ust_yazi_sayisi} sayılı yazısı ile TMK’nın 432. maddesi uyarınca hakkında rapor düzenlenmesi için yönlendirilen {tc} T.C. kimlik nolu {ad_soyad}, {rapor_tarihi.strftime('%d/%m/%Y')} tarihinde Hitit Üniversitesi Erol Olçok Eğitim ve Araştırma Hastanesi Psikiyatri Heyetinde değerlendirilmiştir.
İlgilinin kendisinden ve ilgili tıbbi/adli evraktan edinilen bilgilere göre {anamnez} anlaşılmıştır.
{mse}

{sonuc}"""

# Sonuç gösterimi
st.text_area("Oluşturulan Rapor", tam_rapor, height=600)
