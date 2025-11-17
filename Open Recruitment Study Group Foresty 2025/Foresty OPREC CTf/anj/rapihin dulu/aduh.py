import dis
import importlib.util
import sys

# Menentukan nama modul dan path file .pyc
file_path = "script.cpython-313.pyc"
module_name = "script"

try:
    # 1. Buat "spesifikasi" modul dari file .pyc
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    
    # 2. Buat modul kosong dari spesifikasi itu
    module = importlib.util.module_from_spec(spec)
    
    # 3. Tambahkan modul ini ke sys.modules agar impor internal (jika ada) berfungsi
    sys.modules[module_name] = module
    
    # 4. "Jalankan" (impor) modul tersebut untuk mengisi datanya
    spec.loader.exec_module(module)

    # 5. Periksa apakah fungsi 'main' ada di dalam modul
    if hasattr(module, 'main'):
        print(f"--- Disassembly dari fungsi 'main' di {file_path} ---")
        # 6. Ini adalah intinya: Disassemble fungsi 'main'
        dis.dis(module.main)
        print("--- Akhir dari disassembly 'main' ---")

        # --- TAMBAHKAN BARIS DI BAWAH INI ---
        
        # 7. Disassemble fungsi 'enc'
        if hasattr(module, 'enc'):
            print(f"\n--- Disassembly dari fungsi 'enc' ---")
            dis.dis(module.enc)
            print("--- Akhir dari disassembly 'enc' ---")
        
        # 8. Cetak nilai variabel 'the_flag'
        if hasattr(module, 'the_flag'):
            print(f"\n--- Nilai variabel 'the_flag' ---")
            print(module.the_flag)
            print("--- Akhir dari nilai 'the_flag' ---")

    else:
        print(f"Error: Fungsi 'main' tidak ditemukan di dalam modul {module_name}.")
        print("Mungkin namanya berbeda? Coba periksa dengan 'print(dir(module))'")

except FileNotFoundError:
    print(f"Error: File '{file_path}' tidak ditemukan. Pastikan Anda berada di direktori yang benar.")
except Exception as e:
    print(f"Terjadi error: {e}")
    print("Pastikan Anda menjalankan ini dengan Python 3.")
