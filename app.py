import streamlit as st
import pandas as pd
import datetime

from database import gejala
from rules import forward_chaining

# ==========================
# KONFIGURASI HALAMAN
# ==========================

st.set_page_config(
    page_title="Sistem Pakar Diagnosis Diabetes",
    page_icon="🩺",
    layout="wide"
)


# ==========================
# SESSION STATE
# ==========================

if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

with st.sidebar:

    st.image("assets/logo.png", width=170)

    st.markdown(
        "<h2 style='text-align:center;color:#1565C0;'>🩺 Sistem Pakar</h2>",
        unsafe_allow_html=True
    )

    st.write("Diagnosis Diabetes Mellitus")

    st.markdown("---")

    menu = st.selectbox(
        "📂 Pilih Menu",
        [
            "🏠 Dashboard",
            "🩺 Diagnosa",
            "📄 Riwayat",
            "📊 Grafik",
            "ℹ️ Tentang"
        ]
    )

    st.markdown("---")

    st.info("Metode : Forward Chaining")

    st.success("Status : Online")

    st.caption("Versi 1.0")

# ==========================
# DASHBOARD
# ==========================

# ==========================
# DASHBOARD
# ==========================

if menu == "🏠 Dashboard":

    st.title("🩺 Sistem Pakar Diagnosis Diabetes Mellitus")

    st.image("assets/logo.png", width=180)

    st.write("📅", datetime.datetime.now().strftime("%d %B %Y"))
    st.write("🕒", datetime.datetime.now().strftime("%H:%M:%S"))

    st.success("Selamat Datang 👋")

    st.write("""
Aplikasi ini merupakan sistem pakar berbasis web yang digunakan untuk membantu
melakukan diagnosis awal penyakit Diabetes Mellitus berdasarkan gejala yang
dialami oleh pengguna.

Sistem menggunakan metode **Forward Chaining** dan **Scoring System**
untuk menghasilkan diagnosis awal berdasarkan gejala yang dipilih.

⚠️ Hasil diagnosis hanya sebagai informasi awal dan tidak menggantikan
pemeriksaan dokter.
""")

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    total = len(st.session_state.riwayat)

    tinggi = sum(
        1 for x in st.session_state.riwayat
        if "Risiko Tinggi" in x["Hasil"] or "Risiko Sangat Tinggi" in x["Hasil"]
    )

    sedang = sum(
        1 for x in st.session_state.riwayat
        if "Kemungkinan" in x["Hasil"]
    )

    normal = sum(
        1 for x in st.session_state.riwayat
        if "Tidak Terindikasi" in x["Hasil"]
    )

    col1.metric("👥 Total Pasien", total)
    col2.metric("⚠️ Risiko Tinggi", tinggi)
    col3.metric("📈 Kemungkinan", sedang)
    col4.metric("✅ Normal", normal)

    st.markdown("---")

    st.subheader("📌 Informasi Singkat")

    st.info("""
Diabetes Mellitus merupakan penyakit kronis yang dapat dicegah dengan:

• Menjaga pola makan sehat
• Berolahraga minimal 30 menit setiap hari
• Menjaga berat badan ideal
• Mengurangi konsumsi gula
• Melakukan pemeriksaan gula darah secara berkala
""")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🧠 Metode")
        st.write("Forward Chaining")

    with col2:
        st.info("💻 Platform")
        st.write("Python + Streamlit")

    with col3:
        st.info("📋 Fitur")
        st.write("Diagnosa Diabetes")

    st.markdown("---")

    st.subheader("📖 Apa itu Diabetes Mellitus?")

    st.write("""
Diabetes Mellitus merupakan penyakit kronis yang ditandai dengan tingginya kadar
gula darah akibat tubuh tidak mampu memproduksi insulin yang cukup atau tidak
dapat menggunakan insulin secara efektif.

Gejala yang umum meliputi:

• Sering haus
• Sering buang air kecil
• Mudah lapar
• Berat badan turun
• Mudah lelah
• Penglihatan kabur
• Luka sulit sembuh
• Kesemutan
""")

    st.write("""
Diabetes Mellitus merupakan penyakit kronis yang terjadi ketika kadar gula darah
(glukosa) meningkat akibat tubuh tidak mampu memproduksi insulin yang cukup atau
tidak dapat menggunakan insulin secara efektif.

Gejala yang umum dialami antara lain:

- Sering haus
- Sering buang air kecil
- Mudah lapar
- Berat badan turun
- Mudah lelah
- Penglihatan kabur
- Luka sulit sembuh
- Kesemutan pada tangan atau kaki

Deteksi dini sangat penting untuk mencegah komplikasi seperti penyakit jantung,
kerusakan ginjal, gangguan saraf, dan gangguan penglihatan.
""")
# ==========================
# DIAGNOSA
# ==========================

elif menu == "🩺 Diagnosa":

    st.title("🩺 Form Diagnosa Diabetes Mellitus")

    st.subheader("👤 Data Pasien")

    col1, col2 = st.columns(2)

    with col1:
        nama = st.text_input("Nama Pasien")
        umur = st.number_input("Umur", min_value=1, max_value=120)
        jenis_kelamin = st.selectbox(
            "Jenis Kelamin",
            ["Laki-laki", "Perempuan"]
        )

    with col2:
        berat = st.number_input(
            "Berat Badan (kg)",
            min_value=20,
            max_value=200
        )

        tinggi = st.number_input(
            "Tinggi Badan (cm)",
            min_value=100,
            max_value=220
        )

    if tinggi > 0:

        bmi = berat / ((tinggi / 100) ** 2)

        st.info(f"📏 BMI : {bmi:.2f}")

        if bmi < 18.5:
            st.warning("Kategori BMI : Berat badan kurang")

        elif bmi < 25:
            st.success("Kategori BMI : Normal")

        elif bmi < 30:
            st.warning("Kategori BMI : Kelebihan berat badan")

        else:
            st.error("Kategori BMI : Obesitas")

    st.markdown("---")

    riwayat = st.selectbox(
        "🧬 Riwayat Keluarga Diabetes",
        ["Tidak Ada", "Ada"]
    )

    st.markdown("---")

    st.subheader("🩺 Pilih Gejala")
    col1, col2 = st.columns(2)

    skor = 0

    with col1:

        if st.checkbox("Sering haus"):
            skor += 2

        if st.checkbox("Sering buang air kecil"):
            skor += 2

        if st.checkbox("Mudah lapar"):
            skor += 1

        if st.checkbox("Berat badan turun"):
            skor += 2

        if st.checkbox("Mudah lelah"):
            skor += 1

        if st.checkbox("Penglihatan kabur"):
            skor += 2

        if st.checkbox("Luka sulit sembuh"):
            skor += 2

    with col2:

        if st.checkbox("Kesemutan"):
            skor += 2

        if st.checkbox("Mulut kering"):
            skor += 1

        if st.checkbox("Kulit terasa gatal"):
            skor += 1

        if st.checkbox("Sering infeksi"):
            skor += 2

        if st.checkbox("Sering mengantuk"):
            skor += 1

        if st.checkbox("Obesitas"):
            skor += 2

        if st.checkbox("Kurang olahraga"):
            skor += 1

    st.markdown("---")
    if st.button("🔍 Diagnosa Sekarang", use_container_width=True):

        if nama.strip() == "":
            st.error("Nama pasien harus diisi.")
            st.stop()

        hasil = forward_chaining(skor)

        data = {
            "Tanggal": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
            "Nama": nama,
            "Umur": umur,
            "Jenis Kelamin": jenis_kelamin,
            "Berat": berat,
            "Tinggi": tinggi,
            "BMI": round(bmi, 2),
            "Riwayat Keluarga": riwayat,
            "Skor": skor,
            "Hasil": hasil
        }

        st.session_state.riwayat.append(data)

        st.success("✅ Hasil Diagnosa")

        c1, c2 = st.columns(2)

        with c1:
            st.metric("Total Skor", skor)

        with c2:
            st.metric("Hasil Diagnosa", hasil)

        st.progress(min(skor / 20, 1.0))

        st.markdown("---")

        st.subheader("📋 Rekomendasi")

        if skor >= 18:
            st.error("""
Segera lakukan pemeriksaan gula darah (GDP/HbA1c),
konsultasikan dengan dokter, dan mulai menerapkan pola hidup sehat.
""")

        elif skor >= 12:
            st.warning("""
Risiko tinggi diabetes.
Disarankan melakukan pemeriksaan di fasilitas kesehatan.
""")

        elif skor >= 7:
            st.info("""
Terdapat kemungkinan diabetes.
Lakukan pemeriksaan gula darah untuk memastikan kondisi.
""")

        else:
            st.success("""
Risiko rendah.
Tetap jaga pola makan sehat, olahraga rutin,
dan lakukan pemeriksaan kesehatan secara berkala.
""")
# ==========================
# RIWAYAT
# ==========================

elif menu == "📄 Riwayat":

    st.title("📄 Riwayat Diagnosa Diabetes")

    if len(st.session_state.riwayat) == 0:

        st.warning("Belum ada riwayat diagnosa.")

    else:

        df = pd.DataFrame(st.session_state.riwayat)

        st.subheader("📋 Data Riwayat")

        st.dataframe(df, use_container_width=True)

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Jumlah Diagnosa", len(df))

        with col2:
            st.metric("Rata-rata Skor", round(df["Skor"].mean(),2))

        st.markdown("---")

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇ Download Riwayat (CSV)",
            data=csv,
            file_name="riwayat_diabetes.csv",
            mime="text/csv"
        )

        if st.button("🗑 Hapus Semua Riwayat"):

            st.session_state.riwayat = []

            st.success("Riwayat berhasil dihapus.")

            st.rerun()
            # ==========================
# GRAFIK
# ==========================

elif menu == "📊 Grafik":

    st.title("📊 Grafik Hasil Diagnosa")

    if len(st.session_state.riwayat) == 0:

        st.warning("Belum ada data diagnosa.")

    else:

        df = pd.DataFrame(st.session_state.riwayat)

        st.subheader("📈 Statistik Diagnosa")

        total = len(df)
        tinggi = len(df[df["Hasil"]=="⚠️ Risiko Tinggi Diabetes Mellitus"])
        sangat_tinggi = len(df[df["Hasil"]=="⚠️ Risiko Sangat Tinggi Diabetes Mellitus"])
        kemungkinan = len(df[df["Hasil"]=="⚠️ Kemungkinan Diabetes Mellitus"])
        normal = len(df[df["Hasil"]=="✅ Tidak Terindikasi Diabetes Mellitus"])

        c1,c2,c3,c4 = st.columns(4)

        c1.metric("Total Pasien", total)
        c2.metric("Risiko Tinggi", tinggi+sangat_tinggi)
        c3.metric("Kemungkinan", kemungkinan)
        c4.metric("Normal", normal)

        st.markdown("---")

        st.subheader("📊 Grafik Batang")

        st.bar_chart(df["Hasil"].value_counts())

        st.markdown("---")

        st.subheader("🥧 Diagram Lingkaran")

        pie = df["Hasil"].value_counts()

        st.pyplot(
            pie.plot.pie(
                autopct="%1.1f%%",
                figsize=(6,6)
            ).figure
        )

        st.markdown("---")

        st.subheader("📋 Ringkasan")

        st.write(f"Jumlah pasien : **{total}**")
        st.write(f"Risiko sangat tinggi : **{sangat_tinggi}**")
        st.write(f"Risiko tinggi : **{tinggi}**")
        st.write(f"Kemungkinan diabetes : **{kemungkinan}**")
        st.write(f"Tidak terindikasi : **{normal}**")
        # ==========================
        
# TENTANG
# ==========================

elif menu == "ℹ️ Tentang":

    st.title("ℹ️ Tentang Aplikasi")

    st.image("assets/logo.png", width=180)

    st.markdown("---")

    st.header("🩺 Sistem Pakar Diagnosis Diabetes Mellitus")

    st.write("""
Aplikasi ini merupakan sistem pakar berbasis web yang dirancang untuk membantu
pengguna melakukan diagnosis awal penyakit Diabetes Mellitus berdasarkan gejala
yang dialami.

Metode yang digunakan adalah **Forward Chaining** yang dipadukan dengan
**Scoring System** sehingga mampu memberikan hasil diagnosis awal beserta
rekomendasi tindakan.
""")

    st.markdown("---")

    st.subheader("🎯 Tujuan")

    st.write("""
- Membantu deteksi dini Diabetes Mellitus.
- Memberikan informasi awal kepada masyarakat.
- Sebagai media edukasi mengenai penyakit diabetes.
""")

    st.markdown("---")

    st.subheader("⚙️ Teknologi")

    st.write("""
- Python 3
- Streamlit
- Pandas
- Matplotlib
""")

    st.markdown("---")

    st.subheader("✨ Fitur Aplikasi")

    st.write("""
✅ Dashboard

✅ Diagnosa Diabetes

✅ Riwayat Diagnosa

✅ Grafik Hasil Diagnosa

✅ Download Riwayat CSV

✅ Tampilan Responsif
""")

    st.markdown("---")

    st.subheader("👨‍💻 Pengembang")

    st.write("""
Nama : **Arya Fatih Choiry**

Program Studi : **Teknik Biomedis**

Universitas : **Universitas Dian Nuswantoro**

Versi Aplikasi : **1.0**
""")

    st.success("Terima kasih telah menggunakan aplikasi ini.")
st.markdown("---")

st.caption(
    "© 2026 Sistem Pakar Diagnosis Diabetes Mellitus | "
    "Teknik Biomedis | Universitas Dian Nuswantoro"
)
st.markdown("---")

st.markdown(
"""
<div style="text-align:center;">
<b>Sistem Pakar Diagnosis Diabetes Mellitus</b><br>
Menggunakan Metode Forward Chaining<br><br>

© 2026 Teknik Biomedis<br>
Universitas Dian Nuswantoro
</div>
""",
unsafe_allow_html=True
)