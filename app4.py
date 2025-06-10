import streamlit as st

def next_step(): #Function ketika tombol 'Next" ditekan
    if st.session_state.p_index < len(data) - 1:
        st.session_state.p_index += 1 #Index untuk pertanyaan + 1 sehingga lanjut ke pertanyaan selanjutnya

def back_step(): #Function ketika tombol 'Back' ditekan
    if st.session_state.p_index > 0: #Ketika di pertanyaan index ke 0 atau pertanyaan pertama, ketika click tombol 'Back' pun tidak akan pindah kemana mana
        st.session_state.p_index -= 1 #Index untuk pertanyaan - 1 sehingga kembali ke pertanyaan sebelumnya

st.title("🧐WHAT IS YOUR PASSION🧐") #Judul

st.header("Mini quizzz") #Pengantar
data = [ #Mendeclare data yang isinya kumpulan pertanyaan dan pilihan
   {
       "pertanyaan" : "Saat nongkrong, lu lebih suka...",
       "pilihan": [
                "Duduk sambil ngerjain side project (iya, bawa laptop😎)",
                "Nge-review desain cafe: 'Ini kok norak bgt desainnya😐'",
                "Ngobrolin tren crypto, data Tiktok"
            ]
   },
   {
       "pertanyaan" : "Kalo disuruh ikut lomba, lu paling semangat kalau...",
       "pilihan": [
                "Hackathon bikin web/aplikasi",
                "Bikin desain buat aplikasi",
                "Suruh ngolah data buanyak banget biar rapih"
            ]
   },
   {
       "pertanyaan" : "Waktu kerja kelompok, lu biasanya...",
       "pilihan": [
                "Paling gercep ngambil coding-an pokoknya biar cepet kelar",
                "Maunya yang gambar gambar mulu",
                "Selalu nanya, 'INI DATA DAPET DARIMANA'"
            ]
   }
]

if "p_index" not in st.session_state: #Menggunakan st.session_state karena jika hanya variabel biasa maka akan ter reset (Setiap ada interaksi user, streamlit membaca ulang dari atas)
    st.session_state.p_index = 0
if "jawaban_user" not in st.session_state:
    st.session_state.jawaban_user = [None] * len(data) #Membuat list untuk menyimpan jawaban dari radio yang telah dijawab oleh user

if "submitted" not in st.session_state:
    st.session_state.submitted = False

index_sekarang = st.session_state.p_index
pertanyaan_sekarang = data[index_sekarang] #Mengakses pertanyaan dari list data dengan index_sekarang

st.subheader(f"Pertanyaan ke-{index_sekarang+1} dari {len(data)}")
jawaban = st.radio( #Pilihan
    pertanyaan_sekarang["pertanyaan"], #Judul dari pertanyaan
    pertanyaan_sekarang["pilihan"], #Pilihan-pilihan yang tersedia, mengambil value dari key "pilihan"
    index = pertanyaan_sekarang["pilihan"].index(st.session_state.jawaban_user[index_sekarang]) #Menyimpan jawaban user ketika next atau back pertanyaan
    if st.session_state.jawaban_user[index_sekarang] in pertanyaan_sekarang["pilihan"] else 0,
    key = f"radio_{index_sekarang}"
)

st.session_state.jawaban_user[index_sekarang] = jawaban #Meng assign setiap value dari radio ke list jawaban_user

col1, col2  = st.columns([1,1]) #Membuat column sehingga bisa kanan kiri
with col1: #Isi dari kolom 1
    st.button("Back", on_click=back_step) #Tombol back untuk ke pertanyaan sebelumnya

with col2: #Isi dari kolom 2
    if index_sekarang == len(data) - 1: #Ketika index sudah mencapai len(data) - 1 atau pertanyaan terakhir
        if st.button("Submit"): #Mengganti tombol 'Next' dengan tombol 'Submit'
            st.session_state.submitted = True
    else: #Selain dari indeks terakhir, tombol tetap menjadi 'Next'
        st.button("Next", on_click=next_step)

if st.session_state.submitted: #Conditional ketika user sudah menekan tombol submit
    jawaban_user = st.session_state.jawaban_user
    #Assign poin untuk setiap category
    programmer = 0
    uiux = 0
    data_scientist = 0

    for i in range (len(jawaban_user)): #Looping setiap index
        for pilihan in data[i]["pilihan"]: #NEsted loop untuk semua 'pilihan' di data dengan indeks i
            if jawaban_user[i] == pilihan and data[i]["pilihan"].index(pilihan) == 0:
                programmer += 1
            elif jawaban_user[i] == pilihan and data[i]["pilihan"].index(pilihan) == 1:
                uiux += 1
            elif jawaban_user[i] == pilihan and data[i]["pilihan"].index(pilihan) == 2:
                data_scientist += 1

    #Print output sesuai nilai poin tertinggi
    if programmer > uiux and programmer > data_scientist:
        st.subheader("SELAMAT KAMU OTW TIDUR 1 JAM PER HARI SEBAGAI PROGRAMMER")
    elif uiux > programmer and uiux > data_scientist:
        st.subheader("SELAMAT KAMU BISA BEDAIN WARNA #FFFFFF SAMA #FEFEFE. COCOK JADI UIUX DESIGNER")
    elif data_scientist > programmer and data_scientist > uiux:
        st.subheader("SELAMAT KAMU BISA NGELIHAT 1000 LINE EXCEL SEKALIGUS. SEPUH DATSCI")
    else:
        st.subheader("SELAMAT KAMU ALL ROLE, COCOK JADI PROGRAMMER, UIUX, SAMA DATSCI")

    st.session_state.submitted = False