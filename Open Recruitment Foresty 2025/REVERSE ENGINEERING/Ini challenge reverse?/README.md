# 🔍 [Reverse Engineering] ini chal reverse

[![Status Solusi](https://img.shields.io/badge/Status-Solved-success)]()
[![Poin Challenge](https://img.shields.io/badge/Poin-190-orange)]()
[![Kategori](https://img.shields.io/badge/Kategori-Reverse_Engineering-red)]()

> **Path Solusi:** `oprecforesty2025/reverse engineering/ini chal reverse/`

## 💡 Informasi Challenge

| Detail | Nilai |
| :--- | :--- |
| **Event CTF** | Oprec Foresty 2025 |
| **Poin** | 190 |
| **Kesulitan** | Baby (Mudah) |
| **Author** | BbayuGt |
| **Deskripsi** | Ini challenge reverse? Harusnya sih challenge reverse, tapi kok... |

## 🧩 File yang Diberikan
-   `chall`: File biner (executable) berarsitektur x86-64.

---

## 🧠 Teknik dan Kerentanan

Challenge ini awalnya terlihat seperti membutuhkan *decompiler* atau *debugger* canggih, namun ternyata **flag dapat diekstrak secara langsung** menggunakan utilitas dasar Linux (`strings`).

**Kerentanan:** *Flag* hardcoded dan tidak terenkripsi, disimpan sebagai *string* biasa di dalam segmen data biner.

---

## 🛠️ Langkah-Langkah Solusi (Writeup)

### 1. Analisis Awal File

Periksa jenis file dan arsitektur biner.

```bash
# Periksa jenis file
$ file chall
chall: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, ...
