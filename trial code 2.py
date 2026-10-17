# 1. Fungsi untuk menerima atau mengolah data input
def input_data_belanja():
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = float(input("Masukkan harga: "))
    jumlah_barang = int(input("Masukkan jumlah: "))
    return nama_barang,harga_barang, jumlah_barang

# 2. Fungsi untuk menghitung hasil utama (total belanja & diskon)
def hitung_total(harga, jumlah):
    return harga * jumlah

def hitung_diskon(total_belanja):
    if total_belanja >= 100000:
        return total_belanja * 0.10
    return 0

# 3. Fungsi untuk menampilkan hasil
def tampilkan_hasil(nama_barang, total_belanja, diskon, total_bayar):
    print("\nHASIL PERHITUNGAN ")
    print("Nama Barang =", nama_barang)
    print("Total =", total_belanja)
    print("Diskon =", diskon)
    print("Bayar =", total_bayar)

#Program Utama
# Memanggil fungsi input data
nama_barang, harga_input, jumlah_input = input_data_belanja()

# Proses perhitungan menggunakan fungsi
total_belanja = hitung_total(harga_input, jumlah_input)
diskon = hitung_diskon(total_belanja)
total_bayar = total_belanja - diskon

# Memanggil fungsi untuk menampilkan hasil ke layar
tampilkan_hasil(nama_barang,total_belanja, diskon, total_bayar)