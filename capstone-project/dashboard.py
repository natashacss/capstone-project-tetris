import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-v0_8")
st.set_page_config(
    page_title="Efek Pandemi COVID-19 pada Peningkatan Jumlah Pekerja di Bawah Umur",
    # layout="wide"
)

pp, name = st.columns([1, 10])
pp.image("databases/profile/pp.jpg", width=60)
name.markdown(
    """
        <style>
            .name {
                margin-top: -15px;
            }
            .sub {
                margin-top: -20px;
            }
            .date {
                margin-top: -20px;
                font-size: 12px;
            }
        </style>
    """,
    unsafe_allow_html=True,
)
name.markdown("<h6 class='name'>Natasha Catherine S</h6>", unsafe_allow_html=True)
name.markdown("<p class='name'>TETRIS-030</p>", unsafe_allow_html=True)
name.markdown("<p class='name'>katarinatashaa@gmail.com</p>", unsafe_allow_html=True)

"---"

st.title("Efek Pandemi COVID-19 pada Peningkatan Jumlah Pekerja di Bawah Umur")

st.write(
    """
    Anak-anak Indonesia adalah harapan masa depan negara ini, dan semua pihak bertanggung jawab untuk menjamin pemenuhan hak asasi manusia (HAM) mereka. Sayangnya, kenyataannya adalah angka pekerja anak di Indonesia masih mengkhawatirkan.
    
    Anak-anak berusia hingga 18 tahun memiliki hak untuk bersekolah dan memperoleh pendidikan. Namun, banyak dari mereka terpaksa harus bekerja untuk membantu orang tua atau memenuhi kebutuhan hidup sehari-hari.
    
    Menurut data dari Badan Pusat Statistik (BPS), pada tahun 2020, terdapat sekitar 1,17 juta anak usia 10-17 tahun yang bekerja di Indonesia, meningkat sebanyak 320 ribu anak dibandingkan dengan tahun sebelumnya (38% lebih tinggi dari 2019). Hal ini menunjukkan perlunya perhatian lebih terhadap perlindungan dan hak-hak anak dalam dunia ketenagakerjaan.   
    """
)


st.info(
    """
    Undang-Undang Nomor 13 Tahun 2003 mengenai Ketenagakerjaan menetapkan bahwa pengusaha dilarang mempekerjakan anak yang berusia kurang dari 18 tahun. Larangan mempekerjakan anak di bawah usia 18 tahun bertujuan untuk melindungi hak-hak mereka dan memastikan kesempatan pendidikan serta pertumbuhan yang sehat.
    
    Anak-anak harus berfokus pada pendidikan dan perkembangan mereka, bukan bekerja di bawah umur.
    
    UU No. 13 Tahun 2003 memberikan dasar hukum yang kuat untuk melindungi hak-hak pekerja, termasuk anak-anak, dalam dunia ketenagakerjaan di Indonesia.
    """
)

st.markdown(
    "<h3>Berikut adalah persentase jumlah pekerja berumur 10 hingga 17 tahun yang bekerja di Indonesia!</h3>", unsafe_allow_html=True
)
labor_area, labor_gender = st.tabs(["Berdasarkan provinsi di Indonesia...", "Berdasarkan jenis kelamin anak..."])

with labor_area:
    persentase_pekerja_anak = pd.read_csv("databases/labored-children-cleaned/persentase_pekerja_anak.csv")
    persentase_pekerja_anak["tahun"] = pd.to_datetime(persentase_pekerja_anak["tahun"].astype(str))
    persentase_pekerja_anak.set_index("tahun", inplace=True)
    area = st.selectbox(
        "Pilih provinsi",
        persentase_pekerja_anak.columns.unique(),
        index=len(persentase_pekerja_anak.columns.unique()) - 1,
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    persentase_pekerja_anak[area].plot(marker="o", ax=ax)
    # create a seperator before and after 2020
    plt.axvline(x="2020", color="red", linestyle="--")
    fill_thresholds_min, fill_thresholds_max = (
        np.min(ax.get_yticks()) - 0.2,
        np.max(ax.get_yticks()) + 0.2,
    )
    ax.fill_between(
        persentase_pekerja_anak.index[:3],
        fill_thresholds_min,
        fill_thresholds_max,
        color="green",
        alpha=0.2,
    )
    ax.fill_between(
        persentase_pekerja_anak.index[2:],
        fill_thresholds_min,
        fill_thresholds_max,
        color="red",
        alpha=0.2,
    )
    ax.text("2020", fill_thresholds_max - 0.15, "During Pandemic", style="italic")
    ax.text("2019", fill_thresholds_max - 0.15, "Pre-pandemic", style="italic")
    for i, value in enumerate(persentase_pekerja_anak[area]):
        ax.text(persentase_pekerja_anak.index[i], value + 0.05, value, style="italic")
    plt.ylabel("%")
    plt.annotate(
        "Sumber: Badan Pusat Statistik (BPS), 2024",
        (0, 0),
        (0, -35),
        fontsize=10,
        xycoords="axes fraction",
        textcoords="offset points",
        va="top",
    )
    st.pyplot(fig)

with labor_gender:
    persentase_anak_gender = pd.read_csv(
        "databases/labored-children-cleaned/persentase_anak_gender.csv"
    )
    persentase_anak_gender["tahun"] = pd.to_datetime(
        persentase_anak_gender["tahun"].astype(str)
    )
    persentase_anak_gender.set_index("tahun", inplace=True)
    fig, ax = plt.subplots(figsize=(10, 5))
    persentase_anak_gender["Laki-laki"].plot(marker="o", color="b", ax=ax)
    persentase_anak_gender["Perempuan"].plot(marker="o", color="r", ax=ax)
    # create a seperator before and after 2020
    plt.axvline(x="2020", color="red", linestyle="--")
    fill_thresholds_min, fill_thresholds_max = (
        np.min(ax.get_yticks()) - 0.2,
        np.max(ax.get_yticks()) + 0.2,
    )
    ax.fill_between(
        persentase_pekerja_anak.index[:3],
        fill_thresholds_min,
        fill_thresholds_max,
        color="green",
        alpha=0.2,
    )
    ax.fill_between(
        persentase_pekerja_anak.index[2:],
        fill_thresholds_min,
        fill_thresholds_max,
        color="red",
        alpha=0.2,
    )
    ax.legend(["Laki-laki", "Perempuan"])
    # create text top left
    ax.text("2020", 3.6, "During Pandemic", style="italic")
    ax.text("2019", 3.6, "Pre-pandemic", style="italic")
    for i, value in enumerate(persentase_anak_gender["Laki-laki"]):
        ax.text(
            persentase_pekerja_anak.index[i], value + 0.05, value, style="italic", color="blue"
        )
    for i, value in enumerate(persentase_anak_gender["Perempuan"]):
        ax.text(
            persentase_pekerja_anak.index[i], value - 0.15, value, style="italic", color="red"
        )
    plt.ylabel("%")
    plt.annotate(
        "Sumber: Badan Pusat Statistik (BPS), 2024",
        (0, 0),
        (0, -35),
        fontsize=10,
        xycoords="axes fraction",
        textcoords="offset points",
        va="top",
    )
    st.pyplot(fig)

st.write(
    """
    Pada tahun 2020, terjadi peningkatan yang signifikan ketika pandemi dimulai.
    
    Berbagai faktor mempengaruhi situasi ini, dan dalam hal ini, dugaan utamanya adalah pandemi itu sendiri.
    
    Pada tahun 2021, jumlah pekerja anak sedikit menurun dari tahun sebelumnya, yaitu dari 1,17 juta menjadi 940 ribu.
    
    Meskipun demikian, angka ini masih sedikit lebih tinggi daripada sebelum masa pandemi.
    
    Di Kalimantan Utara, data menunjukkan tren yang terus meningkat hingga tahun 2021.
    """
)

fig, ax = plt.subplots(figsize=(10, 3))
persentase_anak_provinsi = pd.read_csv("databases/labored-children-cleaned/persentase_anak_provinsi.csv")
sns.barplot(x="provinsi", y="persentase", data=persentase_anak_provinsi, palette="Blues_d")
plt.xticks(rotation=90)
plt.title("Peringkat Provinsi dengan Pekerja di Bawah Umur Terbanyak Tahun 2021")
plt.ylabel("%")
for i in ax.containers:
    ax.bar_label(i, fontsize=8)
plt.annotate(
    "Sumber: Badan Pusat Statistik (BPS), 2024",
    (0, 0),
    (0, -150),
    fontsize=10,
    xycoords="axes fraction",
    textcoords="offset points",
    va="top",
)
st.pyplot(fig)

col1, col2 = st.columns([3, 2])
fig, ax = plt.subplots(figsize=(7, 4))
pekerja_anak_2020 = pd.read_csv(
    "databases/labored-children-cleaned/pekerja_anak_2020.csv"
)
pekerja_anak_2020.set_index("tahun", inplace=True)
pekerja_anak_2020.plot(kind="bar", ax=ax)
plt.ylabel("%")
for i in ax.containers:
    ax.bar_label(
        i,
    )
plt.annotate(
    "Sumber: Badan Pusat Statistik (BPS), 2024",
    (0, 0),
    (0, -50),
    fontsize=10,
    xycoords="axes fraction",
    textcoords="offset points",
    va="top",
)
col1.pyplot(fig)
col1.markdown(
    "<h5>Menjadi Perhatian! Peningkatan Jumlah Pekerja di Bawah Umur Berdasarkan Rentang Kelompok Umur</h5>",
    unsafe_allow_html=True,
)
col2.write(
    """
    Peningkatan terbesar terjadi pada kelompok usia 10-12 tahun (naik 97% dari tahun 2019). Jumlah pekerja anak pada usia 13-14 juga mengalami kenaikan yang signifikan (naik 61% dari tahun 2019). Namun, angka pekerja anak pada usia 15-17 mengalami penurunan sedikit (turun 7,5% dari tahun 2019). Situasi ini memerlukan perhatian lebih terhadap perlindungan dan hak-hak anak dalam dunia ketenagakerjaan.
    """
)

st.markdown("<h3>Tingkat Kekerasan pada Anak di Balik Tren Pekerja di Bawah Umur</h3>", unsafe_allow_html=True)
st.write(
    """
    Anak-anak yang bekerja berisiko menghentikan pendidikan mereka dan terjerumus dalam situasi berbahaya yang mengancam perkembangan optimal mereka. Salah satu contohnya adalah terlibat dalam tindakan kekerasan. Kondisi ini memerlukan perhatian serius dari pemerintah, masyarakat, dan lembaga terkait untuk melindungi hak-hak anak dan memastikan masa depan mereka yang lebih baik.
    """
)

status_sekolah, kasus_kekerasan_anak = st.tabs(["Status Sekolah", "Kekerasan Anak"])
with status_sekolah:
    fig, ax = plt.subplots(figsize=(10, 5))
    pekerja_anak_sekolah = pd.read_csv(
        "databases/labored-children-cleaned/pekerja_anak_sekolah.csv"
    )
    pekerja_anak_sekolah.set_index("tahun", inplace=True)
    pekerja_anak_sekolah.plot(kind="bar", ax=ax)
    plt.title("Status Akademis Pekerja Anak")
    plt.ylabel("%")
    for i in ax.containers:
        ax.bar_label(
            i,
        )
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)
    plt.annotate(
        "Sumber: Badan Pusat Statistik (BPS), 2024",
        (0, 0),
        (0, -50),
        fontsize=10,
        xycoords="axes fraction",
        textcoords="offset points",
        va="top",
    )
    st.pyplot(fig)
    st.write(
        """
        Mayoritas pekerja anak memiliki status akademis yang menunjukkan bahwa mereka tidak lagi bersekolah. Pada tahun 2020, sekitar 15,83% dari mereka tidak bersekolah, dan pada tahun 2021, angka ini sedikit menurun menjadi 15,03%. Data ini mengindikasikan bahwa banyak pekerja anak mengalami situasi putus sekolah.
        """
    )

with kasus_kekerasan_anak:
    fig, ax = plt.subplots(figsize=(10, 5))
    kekerasan_per_tahun = pd.read_csv(
        "databases/labored-children-cleaned/kekerasan_per_tahun.csv"
    )
    kekerasan_per_tahun["tahun"] = pd.to_datetime(
        kekerasan_per_tahun["tahun"].astype(str)
    )
    kekerasan_per_tahun.set_index("tahun", inplace=True)
    kekerasan_per_tahun.plot(marker="o", ax=ax)
    plt.title("Kekerasan Anak di Indonesia")
    plt.ylabel("Jumlah Kasus Kekerasan Anak")
    for i, value in enumerate(kekerasan_per_tahun["total"]):
        ax.text(kekerasan_per_tahun.index[i], value + 100, value, style="italic")
    plt.annotate(
        "Komisi Perlindungan Anak Indonesia (KPAI)",
        (0, 0),
        (0, -33),
        fontsize=10,
        xycoords="axes fraction",
        textcoords="offset points",
        va="top",
    )
    st.pyplot(fig)
    kekerasan_desc_col, kekerasan_corr_col = st.columns([4, 1])
    kekerasan_corr = persentase_pekerja_anak["INDONESIA"].corr(
        kekerasan_per_tahun["total"]
    )

    with kekerasan_desc_col:
        st.write(
            """
            Seperti peningkatan jumlah pekerja anak, terjadi lonjakan yang signifikan dalam kasus kekerasan anak di Indonesia pada tahun 2020 ketika pandemi dimulai. Data menunjukkan bahwa jumlah kasus kekerasan anak berkorelasi tinggi dengan persentase pekerja anak. Situasi ini memerlukan perhatian serius dari pemerintah, masyarakat, dan lembaga terkait untuk melindungi hak-hak anak dan memastikan masa depan mereka yang lebih baik.
            """
        )
    with kekerasan_corr_col:
        st.metric(
            "Korelasi:",
            f"{kekerasan_corr*100:.2f}%",
        )
