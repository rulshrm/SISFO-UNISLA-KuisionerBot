# SISFO UNISLA AutoKuisioner

Sebuah script otomatisasi untuk mengisi kuesioner di **SISFO UNISLA** menggunakan **Playwright** dan **Inquirer**.

## Fitur
- Login otomatis ke halaman SISFO UNISLA.
- Mengisi kuesioner secara otomatis dengan jawaban yang dipilih oleh pengguna.
- Menambahkan saran pengguna sebelum menyimpan kuisioner.
- Berjalan dalam mode headless (tanpa menampilkan browser).

## Prasyarat

Sebelum menjalankan script ini, pastikan beberapa hal berikut:

1. **Python** sudah terinstall di sistem Anda. Anda bisa mengunduh dan menginstallnya dari [sini](https://www.python.org/downloads/).
2. Install paket **playwright** dan **inquirer**. Anda bisa menginstalnya dengan menjalankan perintah berikut di terminal:

    ```bash
    pip install playwright inquirer
    ```

3. Install Playwright browser dependencies:

    ```bash
    playwright install
    ```

## Cara Penggunaan

1. Clone repository ini atau unduh file script ke komputer Anda:

    ```bash
    git clone https://github.com/rulshrm/SISFO-UNISLA-KuisionerBot.git
    ```

2. Masuk ke direktori project:

    ```bash
    cd SISFO-UNISLA-AutoKuisioner
    ```

3. Jalankan script:

    ```bash
    python sisfo-unisla-autokuisioner.py
    ```

4. Setelah menjalankan script, Anda akan diminta untuk memasukkan NIM, Password, dan Saran:

    - **NIM**: Masukkan NIM Anda untuk login ke SISFO.
    - **Password**: Masukkan password untuk login.
    - **Pilihan jawaban kuisioner**: Pilih jawaban untuk semua pertanyaan (misalnya, "Sangat Setuju").
    - **Saran**: Masukkan saran Anda untuk kuisioner.

5. Script secara otomatis akan mengisi semua pertanyaan dalam kuisioner dan menyimpan hasilnya.

## Struktur Kode

- **`questions`**: Menggunakan **inquirer** untuk menampilkan opsi jawaban kuisioner.
- **`isi_kuisioner`**: Fungsi untuk mengisi kuisioner secara otomatis dari pertanyaan 1 hingga 26.
- **`run`**: Fungsi utama yang menangani proses login, mengisi kuisioner, menambahkan saran, dan menyimpan hasil.
- **Error Handling**: Jika terjadi kesalahan selama proses, browser akan otomatis ditutup untuk menghindari masalah lebih lanjut.

## Teknologi yang Digunakan
- [Playwright](https://playwright.dev/python/docs/intro) – Framework untuk otomatisasi browser.
- [Inquirer](https://pypi.org/project/inquirer/) – Library untuk menangani input interaktif dari pengguna.

## Catatan Penting

- Pastikan kredensial (NIM dan Password) yang digunakan valid untuk menghindari kegagalan login.
- Script ini bekerja pada browser **headless**, sehingga tidak ada jendela browser yang ditampilkan saat proses berjalan.
- Periksa koneksi internet Anda sebelum menjalankan script.

## Lisensi

Proyek ini dilisensikan di bawah lisensi MIT - lihat [LICENSE](LICENSE) file untuk detail lebih lanjut.
