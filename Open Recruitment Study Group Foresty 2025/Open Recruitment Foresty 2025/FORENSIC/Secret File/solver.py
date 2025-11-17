import zipfile
import os

# Ganti ini dengan nama file zip awal Anda
file_zip_awal = "secret_file.zip" 

# Ganti ini jika zip memiliki password
PASSWORD = None  # atau ganti dengan b"password_nya"

print(f"Memulai ekstraksi dari: {file_zip_awal}")

# Loop selama file yang kita proses adalah file zip
while file_zip_awal.endswith(".zip"):
    print(f"Membuka: {file_zip_awal}")
    
    try:
        # Buka file zip
        with zipfile.ZipFile(file_zip_awal, 'r') as zf:
            
            # Siapkan untuk mencari zip berikutnya di dalam zip ini
            zip_berikutnya = None
            
            # Cek semua file di dalam zip
            for nama_file in zf.namelist():
                if nama_file.endswith(".zip"):
                    zip_berikutnya = nama_file
                
                # Ekstrak file (dengan atau tanpa password)
                if PASSWORD:
                    zf.extract(nama_file, pwd=PASSWORD)
                else:
                    zf.extract(nama_file)
            
            # Hapus file zip yang lama
            os.remove(file_zip_awal)
            
            if zip_berikutnya:
                # Kita menemukan zip baru, set sebagai target loop berikutnya
                file_zip_awal = zip_berikutnya
            else:
                # Tidak ada zip lagi, hentikan loop
                print("====================")
                print("Ekstraksi selesai, tidak ada zip di dalamnya.")
                break
                
    except zipfile.BadZipFile:
        print(f"Error: File {file_zip_awal} bukan file zip yang valid atau rusak.")
        break
    except FileNotFoundError:
        print(f"Error: File {file_zip_awal} tidak ditemukan.")
        break

print("Proses selesai. Cek direktori untuk file flag.")

# Coba baca file flag.txt jika ada
if os.path.exists("flag.txt"):
    print("Flag ditemukan:")
    with open("flag.txt", "r") as f:
        print(f.read())