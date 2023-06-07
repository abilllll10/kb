# Mendefinisikan daftar penyakit beserta kode, nama, dan gejalanya
daftar_penyakit = [
    {"kode": "P01", "nama": "A", "gejala": ["G01", "G03"]},  # Penyakit A dengan gejala G01 dan G03
    {"kode": "P02", "nama": "B", "gejala": ["G02", "G03", "G06"]},  # Penyakit B dengan gejala G02, G03, dan G06
    {"kode": "P03", "nama": "C", "gejala": ["G02", "G04", "G01", "G05"]},  # Penyakit C dengan gejala G02, G04, G01, dan G05
    {"kode": "P04", "nama": "D", "gejala": ["G06", "G05"]}  # Penyakit D dengan gejala G06 dan G05
]

# Mendefinisikan daftar gejala beserta kode, nama, dan nilai keahliannya
daftar_gejala = [
    {"kode": "G01", "nama": "Pusing", "nilai": 0.8},  # Gejala Pusing dengan nilai keahlian 0.8
    {"kode": "G02", "nama": "Keringat Dingin", "nilai": 0.6},  # Gejala Keringat Dingin dengan nilai keahlian 0.6
    {"kode": "G03", "nama": "Menggigil", "nilai": 0.5},  # Gejala Menggigil dengan nilai keahlian 0.5
    {"kode": "G04", "nama": "Dehidrasi", "nilai": 0.2},  # Gejala Dehidrasi dengan nilai keahlian 0.2
    {"kode": "G05", "nama": "Batuk", "nilai": 0.5},  # Gejala Batuk dengan nilai keahlian 0.5
    {"kode": "G06", "nama": "Nyeri Tenggorokan", "nilai": 0.5}  # Gejala Nyeri Tenggorokan dengan nilai keahlian 0.5
]

# Mendefinisikan gejala pasien beserta kode gejala dan nilai-nilainya
gejala_pasien = [
    {"kode": "G01", "nilai": 0.5},  # Pasien memiliki gejala Pusing dengan nilai 0.5
    {"kode": "G05", "nilai": 0.8},  # Pasien memiliki gejala Batuk dengan nilai 0.8
    {"kode": "G04", "nilai": 0.4},  # Pasien memiliki gejala Dehidrasi dengan nilai 0.4
    {"kode": "G02", "nilai": 0.3},  # Pasien memiliki gejala Keringat Dingin dengan nilai 0.3
    {"kode": "G03", "nilai": 0.2}  # Pasien memiliki gejala Menggigil dengan nilai 0.2
]

# Mendefinisikan fungsi untuk menghitung faktor kepastian suatu penyakit berdasarkan gejala pasien
def hitung_faktor_kepastian(penyakit, gejala_pasien):
    faktor_kepastian = 0  # Inisialisasi faktor kepastian
    for gejala_penyakit in penyakit["gejala"]:  # Meloop gejala penyakit pada daftar penyakit
        for gejala in gejala_pasien:  # Meloop gejala pasien pada gejala pasien
            if gejala["kode"] == gejala_penyakit:  # Jika kode gejala pasien sama dengan kode gejala penyakit
                for gejala_ahli in daftar_gejala:  # Meloop gejala ahli pada daftar gejala
                    if gejala_ahli["kode"] == gejala["kode"]:  # Jika kode gejala ahli sama dengan kode gejala pasien
                        produk = gejala["nilai"] * gejala_ahli["nilai"]  # Mengalikan nilai gejala pasien dengan nilai gejala ahli
                        faktor_kepastian = faktor_kepastian + produk * (1 - abs(faktor_kepastian))  # Menghitung faktor kepastian
                        break
    return faktor_kepastian

# Melakukan perulangan melalui daftar penyakit dan mencetak nama penyakit beserta faktor kepastiannya
for penyakit in daftar_penyakit:
    faktor_kepastian = hitung_faktor_kepastian(penyakit, gejala_pasien)
    print(penyakit["nama"], str(faktor_kepastian * 100) + '%')  # Mencetak nama penyakit beserta faktor kepastiannya dalam bentuk persentase
