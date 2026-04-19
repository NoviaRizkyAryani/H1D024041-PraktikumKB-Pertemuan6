import tkinter as tk
from tkinter import messagebox

database_tht = {
    "Tonsilitis": {"gejala": ["G37", "G12", "G5", "G27", "G6", "G21"]},
    "Sinusitis Maksilaris": {"gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"]},
    "Sinusitis Frontalis": {"gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"]},
    "Sinusitis Edmoidalis": {"gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"]},
    "Sinusitis Sfenoidalis": {"gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"]},
    "Abses Peritonsiler": {"gejala": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"]},
    "Faringitis": {"gejala": ["G37", "G5", "G6", "G7", "G15"]},
    "Kanker laring": {"gejala": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"]},
    "Deviasi Septum": {"gejala": ["G37", "G17", "G20", "G8", "G18", "G25"]},
    "Laringitis": {"gejala": ["G37", "G5", "G15", "G16", "G32"]},
    "Kanker Leher dan Kepala": {"gejala": ["G5", "G22", "G8", "G28", "G3", "G11"]},
    "Otitis Media Akut": {"gejala": ["G37", "G20", "G35", "G31"]},
    "Contact Ulcers": {"gejala": ["G5", "G2"]},
    "Abses Parafaringeal": {"gejala": ["G5", "G16"]},
    "Barotitis Media": {"gejala": ["G12", "G20"]},
    "Kanker Nasofaring": {"gejala": ["G17", "G8"]},
    "Kanker Tonsil": {"gejala": ["G6", "G29"]},
    "Neuronitis Vestibularis": {"gejala": ["G35", "G24"]},
    "Meniere": {"gejala": ["G20", "G35", "G14", "G4"]},
    "Tumor Syaraf Pendengaran": {"gejala": ["G12", "G34", "G23"]},
    "Kanker Leher Metastatik": {"gejala": ["G29"]},
    "Osteosklerosis": {"gejala": ["G34", "G9"]},
    "Vertigo Postular": {"gejala": ["G24"]}
}

daftar_gejala = [
    ("G1", "Apakah pernafasan Anda serasa tidak normal/sesak?"),
    ("G2", "Apakah suara Anda menjadi serak atau parau?"),
    ("G3", "Apakah terdapat perubahan kondisi pada tekstur kulit Anda?"),
    ("G4", "Apakah telinga Anda terasa tersumbat atau penuh?"),
    ("G5", "Apakah Anda merasa sakit saat sedang berbicara atau menelan?"),
    ("G6", "Apakah tenggorokan Anda terasa nyeri?"),
    ("G7", "Apakah Anda merasakan sakit pada area leher?"),
    ("G8", "Apakah terjadi pendarahan (mimisan) pada hidung?"),
    ("G9", "Apakah Anda mendengar suara berdenging di telinga"),
    ("G10", "Apakah produksi air liur Anda keluar secara terus-menerus?"),
    ("G11", "Apakah terdapat perubahan nada atau kualitas suara pada suara Anda?"),
    ("G12", "Apakah Anda sedang menderita sakit kepala?"),
    ("G13", "Apakah Anda merasa nyeri di bagian pinggir hidung?"),
    ("G14", "Apakah Anda mengalami serangan pusing berputar (vertigo)?"),
    ("G15", "Apakah ada pembengkakan kelenjar getah bening?"),
    ("G16", "Apakah area Leher Anda nampak membengkak?"),
    ("G17", "Apakah saluran hidung Anda terasa tersumbat?"),
    ("G18", "Apakah Anda memiliki riwayat infeksi sinus?"),
    ("G19", "Apakah terjadi penurunan berat badan secara signifikan?"),
    ("G20", "Apakah Anda merasakan nyeri di bagian telinga?"),
    ("G21", "Apakah selaput lendir Anda terlihat kemerahan?"),
    ("G22", "Apakah Anda merasa ada benjolan di area leher?"),
    ("G23", "Apakah tubuh Anda merasa goyah atau tidak seimbang saat berdiri?"),
    ("G24", "Apakah bola mata Anda bergerak secara tidak sengaja?"),
    ("G25", "Apakah Anda merasakan nyeri di area wajah?"),
    ("G26", "Apakah dahi Anda terasa sakit atau tertekan?"),
    ("G27", "Apakah Anda mengalami gangguan batuk?"),
    ("G28", "Apakah ada pertumbuhan jaringan asing di dalam mulut Anda?"),
    ("G29", "Apakah terdapat benjolan yang muncul di leher Anda?"),
    ("G30", "Apakah ada rasa sakit di antara kedua mata Anda?"),
    ("G31", "Apakah terjadi peradangan pada bagian gendang telinga Anda?"),
    ("G32", "Apakah tenggorokan Anda terasa gatal atau tidak nyaman?"),
    ("G33", "Apakah hidung Anda terus mengeluarkan lendir (meler)?"),
    ("G34", "Apakah fungsi pendengaran Anda menurun (tuli)?"),
    ("G35", "Apakah Anda merasakan mual atau keinginan untuk muntah?"),
    ("G36", "Apakah tubuh Anda terasa sangat letih dan tidak bertenaga?"),
    ("G37", "Apakah suhu tubuh Anda meningkat (demam)?")
]

class AplikasiPakarTHT:
    def __init__(self, root):
        self.root = root
        self.root.title = ("Sistem Pakar Diagnosa Penyakit THT")
        self.gejala_user = []
        self.index_tanya = 0
        
        self.label_tanya = tk.Label(root, 
        text="Jawablah beberapa pertanyaan berikut untuk diagnosa.\nKlik tombol 'Mulai Diagnosa' untuk memulai diagnosa", 
        font=("Times New Roman", 12), wraplength=350, height=6)
        self.label_tanya.pack(pady=20)
        
        self.btn_mulai = tk.Button(root, text="MULAI DIAGNOSA", width=20, bg="yellow", font=("Times New Roman", 10, "bold"), command=self.start)
        self.btn_mulai.pack(pady=10)
        
        self.frame_tombol = tk.Frame(root)
        self.btn_ya = tk.Button(self.frame_tombol, text="YA", width=12, bg="green", fg="white", font=("Times New Roman", 10, "bold"), command=lambda: self.next('y'))
        self.btn_tidak = tk.Button(self.frame_tombol, text="TIDAK", width=12, bg="red", fg="white", font=("Times New Roman", 10, "bold"), command=lambda: self.next('t'))
        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)

    def start(self):
        self.gejala_user = []
        self.index_tanya = 0
        self.btn_mulai.pack_forget()
        self.frame_tombol.pack(pady=20)
        self.update_pertanyaan()

    def update_pertanyaan(self):
        if self.index_tanya < len(daftar_gejala):
            _, teks = daftar_gejala[self.index_tanya]
            self.label_tanya.config(text=teks)
        else:
            self.show_result()

    def next(self, resp):
        if resp == 'y':
            kode_gejala = daftar_gejala[self.index_tanya][0]
            self.gejala_user.append(kode_gejala)
        
        self.index_tanya += 1
        self.update_pertanyaan()

    def show_result(self):
        hasil_diagnosa = []
        
        for penyakit, data in database_tht.items():
            if all(g in self.gejala_user for g in data["gejala"]):
                hasil_diagnosa.append(penyakit)
        
        if hasil_diagnosa:
            pesan = "Hasil Analisis Sistem:\n\nAnda kemungkinan menderita:\n• " + "\n• ".join(hasil_diagnosa)
        else:
            pesan = "Sistem tidak menemukan penyakit yang sesuai dengan kombinasi gejala Anda."
            
        messagebox.showinfo("Hasil Diagnosa Akhir", pesan)
        
        self.frame_tombol.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa selesai. Tekan tombol untuk memulai ulang.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x350")
    app = AplikasiPakarTHT(root)
    root.mainloop()