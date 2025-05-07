import streamlit as st

st.set_page_config(page_title="Adli Psikiyatri Raporları", 
layout="centered")

st.title("🧠 Adli ve Hukuki Psikiyatri Raporları")

st.markdown("""
Bu uygulama, Hitit Üniversitesi Erol Olçok Eğitim ve Araştırma 
Hastanesi’nde düzenlenmesi gereken çeşitli adli ve idari raporların 
otomatik oluşturulmasına yardımcı olmak amacıyla hazırlanmıştır.
""")

st.markdown("## 📋 Rapor Türünü Seçin:")

raporlar = {
    "1_TCK_32": "🧾 TCK 32 – Cezai Ehliyet Raporu",
    "2_TMK_432_Yatis": "🏥 TMK 432 – Zorunlu Yatış Kararı",
    "3_TMK_432_Taburculuk": "🏠 TMK 432 – Taburcu Raporu",
    "4_TMK_405_Demans": "👵 TMK 405 – Vasi Raporu (Demans)",
    "5_TMK_405_Mental_Retardasyon": "🧒 TMK 405 – Vasi Raporu (Mental 
Retardasyon)",
    "6_Noter_Ehliyet": "📑 Noter – Hukuki Ehliyet Raporu"
}

for sayfa, baslik in raporlar.items():
    st.page_link(f"pages/{sayfa}.py", label=baslik, icon="➡️")

st.markdown("---")
st.info("Yukarıdaki başlıklardan birini seçerek ilgili rapor sayfasına 
geçebilirsiniz.")

