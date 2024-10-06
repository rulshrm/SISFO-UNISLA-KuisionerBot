from playwright.sync_api import sync_playwright
import inquirer

# Menggunakan Inquirer untuk menampilkan pilihan jawaban kuisioner ke pengguna.
# Pengguna diminta untuk memilih salah satu dari lima opsi jawaban.
questions = [
    inquirer.List(
        'jawaban',
        message="Pilih jawaban untuk semua pertanyaan",
        choices=['Sangat Setuju', 'Setuju', 'Cukup Setuju', 'Tidak Setuju', 'Sangat Tidak Setuju']
    )
]

# URL halaman login SISFO UNISLA
link = "https://sisfo.unisla.ac.id/index.php"

# Meminta pengguna untuk memasukkan NIM dan Password
# Variabel 'user_name' untuk menyimpan NIM yang dimasukkan
user_name = input("Masukkan NIM Anda: ")

# Variabel 'password' untuk menyimpan password yang dimasukkan
password = input("Masukkan Password Anda: ")

# Mengambil jawaban yang dipilih oleh pengguna menggunakan Inquirer.
# Jawaban dipilih untuk semua pertanyaan kuisioner.
answers = inquirer.prompt(questions)
# Jawaban yang dipilih disimpan dalam variabel 'jawaban_dipilih'.
jawaban_dipilih = answers['jawaban']

# Fungsi untuk mengisi kuisioner secara otomatis
def isi_kuisioner(page, jawaban):
    """
    Mengisi kuisioner dari pertanyaan nomor 1 hingga 26 dengan jawaban yang telah dipilih pengguna.
    
    Args:
    - page: objek halaman dari Playwright untuk berinteraksi dengan halaman.
    - jawaban: jawaban yang telah dipilih pengguna (Sangat Setuju, Setuju, dll.).
    """
    # Mengisi setiap pertanyaan kuisioner (nomor 1 hingga 26) dengan jawaban yang dipilih.
    for i in range(1, 27):  # Mengiterasi pertanyaan dari 1 hingga 26
        # Selector input sesuai dengan nomor pertanyaan dan jawaban yang dipilih.
        selector = f'input[name="jawaban{i}"][value="{jawaban}"]'
        # Menandai jawaban pada pertanyaan yang sesuai.
        page.check(selector)
    print("Semua pertanyaan telah terisi.")

# Fungsi utama untuk menjalankan proses otomatisasi
def run(playwright):
    """
    Fungsi ini menjalankan keseluruhan proses otomatisasi, dari login ke halaman SISFO UNISLA,
    membuka halaman kuisioner, mengisi jawaban, menambahkan saran, dan menyimpan kuisioner.
    
    Args:
    - playwright: objek Playwright untuk mengontrol browser.
    """
    try:
        # Meluncurkan browser Chromium dalam mode headless (tanpa UI).
        # Jika ingin melihat prosesnya secara visual, ubah 'headless' menjadi False.
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        print("Memulai proses login...")
        # Mengakses halaman login SISFO UNISLA.
        page.goto(link)
        print(f"Halaman {link} dibuka.")

        # Mengisi form login dengan NIM, password, dan level.
        page.fill('input[name="username"]', user_name)  # Mengisi NIM pada input username.
        page.fill('input[name="password"]', password)  # Mengisi password pada input password.
        page.select_option('select[name="level"]', '7')  # Memilih level (7 = mahasiswa).
        page.click('button#sub')  # Klik tombol login untuk masuk ke sistem.
        print(f"Berhasil memasukkan username dan password.")

        # Mengklik link untuk membuka halaman "Kuesioner Wajib".
        page.click('a.menu:has-text("Kuesioner Wajib")')
        print(f"Masuk Page Kuesioner Wajib.")
        
        # Arahkan ke halaman kuisioner untuk mulai mengisi pertanyaan kuisioner.
        page.goto("https://sisfo.unisla.ac.id/users/index.php/survey")

        # Mengisi kuisioner secara otomatis dengan jawaban yang dipilih sebelumnya.
        isi_kuisioner(page, jawaban_dipilih)

        # Meminta pengguna untuk memasukkan saran di kolom isian saran.
        saran = input("Masukkan saran Anda: ")
        # Mengisi kolom saran pada kuisioner.
        page.fill('textarea[name="jawaban28"]', saran)

        # Klik tombol "Simpan" untuk mengirim form kuisioner setelah semua pertanyaan dan saran terisi.
        page.click('input[type="submit"]')
        print("Kuesioner berhasil disubmit.")

        # Menutup browser setelah semua proses selesai.
        browser.close()
        print("Proses selesai. Browser ditutup.")

    except Exception as e:
        # Jika terjadi kesalahan, tampilkan pesan error dan pastikan browser ditutup.
        print(f"Terjadi kesalahan selama proses: {e}")
        if 'browser' in locals():
            browser.close()
            print("Browser ditutup setelah terjadi kesalahan.")

# Memulai Playwright dan menjalankan fungsi utama
with sync_playwright() as playwright:
    run(playwright)
