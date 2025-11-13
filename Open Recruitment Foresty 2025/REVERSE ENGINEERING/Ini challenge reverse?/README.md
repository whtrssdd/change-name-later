# [Reverse Engineering] makeitsimple

| Info Challenge | Detail |
| :--- | :--- |
| **Nama CTF** | Foresty CTF 2024 (Contoh) |
| **Kategori** | Reverse Engineering |
| **Poin** | 190 |
| **Kesulitan** | Baby |
| **Author** | BbayuGt |

> Deskripsi Asli Challenge: "Ini challenge reverse? Harusnya sih challenge reverse, tapi kok..."

## 💡 Deskripsi Solusi

Challenge ini adalah sebuah biner (binary executable) yang terlihat seperti *Reverse Engineering*, tetapi solusinya jauh lebih sederhana dan cepat.

Kerentanan utama terletak pada **String tersembunyi** yang ada di dalam biner itu sendiri, yang ternyata adalah *flag* yang valid.

---

## 🛠️ Langkah-Langkah Solusi

### 1. Analisis Awal (Strings)
Awalnya, dilakukan analisis dasar pada biner `chall` untuk mencari string yang dapat dibaca.

```bash
strings chall 
# Output-nya sangat panjang, karena ini biner Rust/Go (berdasarkan snippet)
