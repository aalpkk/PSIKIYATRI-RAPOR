import streamlit as st

st.set_page_config(
    page_title="MenteLex: Psikiyatristler İçin Rapor Otomasyonu",
    page_icon="🧠",  # Bu favicon olarak sekmede görünür
    layout="centered"
)


st.title("🧠 MenteLex: Psikiyatristler İçin Adli Rapor Düzenleme Uygulaması")

st.markdown("""
MenteLex, psikiyatristler tarafından düzenlenen resmi raporların 
hızlı, hatasız ve yasal dile uygun şekilde oluşturmasına yardımcı olan 
bir destek aracıdır.
""")

st.markdown("## 📋 Rapor Türünü Seçin:")

raporlar = {
    "1_TCK_32": "🧾 TCK 32 – Cezai Ehliyet Raporu",
    "2_TMK_432_Yatis": "🏥 TMK 432 – Mahkemeden Sorulan Zorunlu Yatış Kararı",
    "3_TMK_432_Taburculuk": "🏠 TMK 432 – Taburcu Raporu",
    "4_TMK405_Demans": "👵 TMK 405 – Vasi Raporu (Demans)",
    "5_TMK_405_MR": "🧒 TMK 405 – Vasi Raporu (Mental Retardasyon)",
    "6_Fiili_Ehliyet": "📑 Noter – Hukuki Ehliyet Raporu",
    "7_TMK_432_Riza_Disi_Yatis": "📤 TMK 432 – Rızası Olmadan Yatış Ardından Bildirim"
}


for sayfa, baslik in raporlar.items():
    st.page_link(f"pages/{sayfa}.py", label=baslik, icon="➡️")

st.markdown("---")
st.info("Yukarıdaki başlıklardan birini seçerek ilgili rapor sayfasına geçebilirsiniz.")

