import datetime

data_treatment = []
data_pelanggan = []
data_reservasi = []

jadwal_kode = {
    "dawn": "08:00 - 12:00",
    "noon": "13:00 - 16:00",
    "dusk": "17:00 - 20:00"
}

# Fungsi Admin ================================================
def admin_menu():
    while True:
        print("\n=== Calestia Facial Treatment [Admin] ===")
        print("1. Data Treatment")
        print("2. Data Pelanggan")
        print("3. Data Reservasi")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_treatment()
        elif pilihan == "2":
            menu_pelanggan()
        elif pilihan == "3":
            menu_reservasi()
        elif pilihan == "0":
            main()
        else:
            print("Pilihan tidak valid!")

def menu_treatment():
    while True:
        print("\n=== Menu Data Treatment ===")
        print("1. Tambah Data")
        print("2. Cari Data")
        print("3. Edit Data")
        print("4. Hapus Data")
        print("0. Kembali")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_treatment()
        elif pilihan == "2":
            cari_treatment()
        elif pilihan == "3":
            edit_treatment()
        elif pilihan == "4":
            hapus_treatment()
        elif pilihan == "0":
            admin_menu()
        else:
            print("Pilihan tidak valid!")

def tambah_treatment():
    print("\n=== Tambah Data Treatment ===")
    while True:
        jenis = input("Masukkan jenis treatment: ")
        if not jenis:
            print("Jenis treatment tidak boleh kosong!")
            return
        
        harga_input = input("Masukkan harga treatment: ")
        if not harga_input.isdigit():
            print("Harga treatment harus berupa angka!")
            return 
        
        harga = int(harga_input)
        id_treatment = f"TR{len(data_treatment) + 1:03}"
        data_treatment.append({
            "id": id_treatment,
            "jenis": jenis,
            "harga": harga
        })
        print(f"Treatment berhasil ditambahkan dengan ID {id_treatment}!")

        print("\n===== Daftar Treatment =====")
        for treatment in data_treatment:
            print(f"ID Treatment   : {treatment['id']}")
            print(f"Jenis          : {treatment['jenis']}")
            print(f"Harga          : {treatment['harga']}")
            print("============================")
        
        next = input("Apakah Anda ingin menambahkan data lainnya? (y/n): ")
        if next.lower() != 'y':
            break
    return menu_treatment()

def cari_treatment():
    print("\n======= Cari Data Treatment =======")
    while True:
        cari = input("Masukkan ID atau jenis treatment yang dicari: ").lower()
        
        found = False
        for treatment in data_treatment: 
            if treatment['id'].lower() == cari or cari in treatment['jenis'].lower():
                print(f"ID Treatment   : {treatment['id']}")
                print(f"Jenis          : {treatment['jenis']}")
                print(f"Harga          : {treatment['harga']}")
                print("================================")
                found = True
        
        if not found:
            print("Treatment tidak ditemukan!")
        
        next = input("Apakah Anda ingin mencari data lainnya? (y/n): ")
        if next.lower() != 'y':
            break
    return menu_treatment()

def edit_treatment():
    print("\n=== Edit Data Treatment ===")
    while True:
        id_treatment = input("Masukkan ID Treatment: ")
        for t in data_treatment:
            if t["id"] == id_treatment:
                jenis_baru = input(f"Jenis Treatment baru (kosongkan untuk tidak mengubah: {t['jenis']}): ")
                if jenis_baru:
                    t["jenis"] = jenis_baru

                harga_baru = input(f"Harga baru (kosongkan untuk tidak mengubah: {t['harga']}): ")
                if harga_baru:
                    t["harga"] = int(harga_baru)

                print("Data berhasil diperbarui!")
                return
        print("Data tidak ditemukan!")

        next = input("Apakah Anda ingin mengubah data lainnya? (y/n): ")
        if next.lower() != 'y':
            break
    return menu_treatment()

def hapus_treatment():
    print("\n=== Hapus Data Treatment ===")
    while True:
        id_treatment = input("Masukkan ID Treatment: ")
        for t in data_treatment:
            if t["id"] == id_treatment:
                data_treatment.remove(t)
                print("Data berhasil dihapus!")
                return
        print("Data tidak ditemukan!")
        next = input("Apakah Anda ingin menghapus data lainnya? (y/n): ")
        if next.lower() != 'y':
            break
    return menu_treatment()

def menu_pelanggan(): #admin
    while True:
        print("\n=== Menu Data Pelanggan ===")
        print("1. Tampilkan Data")
        print("2. Cari Data")
        print("3. Hapus Data")
        print("0. Kembali")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_pelanggan()
        elif pilihan == "2":
            cari_pelanggan()
        elif pilihan == "3":
            hapus_pelanggan()
        elif pilihan == "0":
            admin_menu()
        else:
            print("Pilihan tidak valid!")

def tampilkan_pelanggan():
    print("\n=== Daftar Semua Pelanggan ===")
    if not data_pelanggan:
            print("Tidak ada data pelanggan.")
            return
    
    for pelanggan in data_pelanggan:
            print(f"ID Pelanggan   : {pelanggan['id']}")
            print(f"Nama           : {pelanggan['nama']}")
            print(f"Usia           : {pelanggan['usia']}")
            print(f"Gender         : {pelanggan['gender']}")
            print(f"Nomor Telepon  : {pelanggan['no_telp']}")
            print(f"Jenis Kulit    : {pelanggan['jenis_kulit']}")
            print("===============================")
    return menu_pelanggan()

def cari_pelanggan():
    print("\n=== Cari Data Pelanggan ===")
    while True:
        cari = input("Masukkan ID pelanggan yang dicari: ")
        pelanggan = next((p for p in data_pelanggan if p['id'] == cari or p['nama'].lower() == cari.lower()), None)
        
        if not pelanggan:
            print("Tidak ada Pelanggan yang sesuai. Silakan coba lagi.")
            continue 

        print("\n===== Data Pelanggan Ditemukan =====")
        print(f"ID Pelanggan   : {pelanggan['id']}")
        print(f"Nama           : {pelanggan['nama']}")
        print(f"Usia           : {pelanggan['usia']}")
        print(f"Gender         : {pelanggan['gender']}")
        print(f"Nomor Telepon  : {pelanggan['no_telp']}")
        print(f"Jenis Kulit    : {pelanggan['jenis_kulit']}")
        print("====================================")

        next_search = input("Apakah Anda ingin mencari data lainnya? (y/n): ")
        if next_search.lower() != 'y':
            break
    return menu_pelanggan()

def hapus_pelanggan():
    print("\n=== Hapus Data Pelanggan ===")
    while True:
        id_pelanggan = input("Masukkan ID Pelanggan: ")
        for p in data_pelanggan:
            if p["id"] == id_pelanggan:
                data_pelanggan.remove(p)
                print("Data berhasil dihapus.")
                return
        print("Data tidak ditemukan!")

        next = input("Apakah Anda ingin menghapus data lainnya? (y/n): ")
        if next.lower() != 'y':
            break
    return menu_pelanggan()

def menu_reservasi():
    while True:
        print("\n=== Menu Data Reservasi ===")
        print("1. Lihat Semua Reservasi")
        print("2. Edit Status Reservasi")
        print("3. Hapus Reservasi")
        print("4. Cetak Nota Reservasi")
        print("0. Kembali")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_reservasi()
        elif pilihan == "2":
            edit_reservasi()
        elif pilihan == "3":
            hapus_reservasi()
        elif pilihan == "4":
            cetak_reservasi()
        elif pilihan == "0":
            admin_menu()
        else:
            print("Pilihan tidak valid!")

# Reservasi Admin (edit, cari, dan tampilkan)
def lihat_reservasi():
    print("\n=== Daftar Reservasi ===")
    if not data_reservasi:
        print("Belum ada reservasi yang dibuat.")
        return
    for reservasi in data_reservasi:
        pelanggan = next((p for p in data_pelanggan if p['id'] == reservasi['id_pelanggan']), None)
        print(f"ID Reservasi  : {reservasi['id']}")
        print(f"Nama Pelanggan: {pelanggan['nama'] if pelanggan else 'Tidak diketahui'}")
        print(f"Tanggal        : {reservasi['tanggal']}")
        print(f"Jadwal         : {jadwal_kode[reservasi['kode_jadwal']]}")
        print("Jenis Treatment:")
        for id_treatment in reservasi['jenis_treatment']:
            treatment = next((t for t in data_treatment if t['id'] == id_treatment), None)
            if treatment:
                print(f"- {treatment['jenis']} ({treatment['harga']})")
        print(f"Status         : {reservasi['status']}")
        print("===============================\n")

    return menu_reservasi()

def edit_reservasi():
    print("\n=== Edit Status Reservasi ===")
    while True:
        id_reservasi = input("Masukkan ID Reservasi: ")
        reservasi = next((r for r in data_reservasi if r['id'] == id_reservasi), None)
        if not reservasi:
            print("ID reservasi tidak ditemukan! Silakan coba lagi.")
            continue

        print("\nDetail Reservasi:")
        print(f"ID Reservasi    : {reservasi['id']}")
        print(f"ID Pelanggan    : {reservasi['id_pelanggan']}")
        print(f"Tanggal         : {reservasi['tanggal']}")
        print(f"Kode Jadwal     : {reservasi['kode_jadwal']}")
        print("Jenis Treatment :")
        for id_treatment in reservasi['jenis_treatment']:
            treatment = next((t for t in data_treatment if t['id'] == id_treatment), None)
            if treatment:
                print(f"- {treatment['jenis']} ({treatment['harga']})")
        print(f"Status Saat Ini : {reservasi['status']}")

        status_baru = input("\nMasukkan status baru (scheduled/completed/cancelled): ").lower()
        if status_baru not in ['scheduled', 'completed', 'cancelled']:
            print("Status tidak valid! Harap masukkan 'scheduled', 'completed', atau 'cancelled'.")
            continue
        reservasi['status'] = status_baru

        print("\nReservasi berhasil diperbarui!")
        print(f"ID Reservasi    : {reservasi['id']}")
        print(f"Status Baru     : {reservasi['status']}")

        lanjut = input("\nApakah Anda ingin mengedit status reservasi lainnya? (y/n): ").lower()
        if lanjut != 'y':
            break

    print("\nKembali ke menu reservasi.")
    return menu_reservasi()

def hapus_reservasi():
    print("\n=== Hapus Reservasi ===")
    while True:
        id_reservasi = input("Masukkan ID Reservasi yang akan dihapus: ")
        
        reservasi = next((r for r in data_reservasi if r['id'] == id_reservasi), None)
        
        if not reservasi:
            print(f"Reservasi dengan ID {id_reservasi} tidak ditemukan. Silakan coba lagi.")
        else:
            konfirmasi = input(f"Apakah Anda yakin ingin menghapus reservasi dengan ID {id_reservasi}? (y/n): ").lower()
            if konfirmasi == 'y':
                data_reservasi.remove(reservasi)
                print(f"Reservasi dengan ID {id_reservasi} telah dihapus.")
        
        next_action = input("Apakah Anda ingin menghapus reservasi lainnya? (y/n): ").lower()
        if next_action != 'y':
            break
    
    print("\nKembali ke menu reservasi.")
    return menu_reservasi()

def cetak_reservasi():
    print("\n=== Cetak Nota Reservasi ===")
    while True:
        id_reservasi = input("Masukkan ID Reservasi: ")
        reservasi = next((r for r in data_reservasi if r['id'] == id_reservasi), None)
        
        if not reservasi:
            print("ID reservasi tidak ditemukan! Silakan coba lagi.")
            continue 

        pelanggan = next((p for p in data_pelanggan if p['id'] == reservasi['id_pelanggan']), None)
        print("\n=== Calestia Facial Treatment ===")
        print("=== Nota Reservasi ===")
        print(f"ID Reservasi  : {reservasi['id']}")
        print(f"Nama Pelanggan: {pelanggan['nama'] if pelanggan else 'Tidak diketahui'}")
        print(f"Tanggal        : {reservasi['tanggal']}")
        print(f"Jadwal         : {jadwal_kode.get(reservasi['kode_jadwal'], 'Kode jadwal tidak valid')}")
        print("Jenis Treatment:")

        total_harga = 0
        for id_treatment in reservasi['jenis_treatment']:
            treatment = next((t for t in data_treatment if t['id'] == id_treatment), None)
            if treatment:
                print(f"- {treatment['jenis']} ({treatment['harga']})")
                total_harga += treatment['harga']
            else:
                print(f"- ID treatment {id_treatment} tidak ditemukan!")

        print(f"Total Harga    : {total_harga}")
        print(f"Status         : {reservasi['status']}")
        print("========================\n")

        next_action = input("Apakah Anda ingin mencetak reservasi lainnya? (y/n): ").lower()
        if next_action != 'y':
            break

    print("\nKembali ke menu reservasi.")
    return menu_reservasi()

def jadwal_harian():
    print("\nJadwal Harian Treatment")
    for kode, waktu in jadwal_kode.items():
        print(f"{kode}: {waktu}")

def pilih_pelanggan():
    print("\n=== Selamat Datang ===")
    while True:
        print("1. Saya pelanggan baru")
        print("2. Saya pelanggan lama (sudah punya ID)")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            pelanggan_aktif = tambah_pelanggan()
            if pelanggan_aktif:
                print("Silahkan Masuk dengan Akun Anda.")
            return pilih_pelanggan()
        elif pilihan == "2":
            id_pelanggan = input("Masukkan ID pelanggan Anda: ")
            pelanggan_aktif = next((p for p in data_pelanggan if p['id'] == id_pelanggan), None)
            if pelanggan_aktif:
                print(f"\nSelamat datang kembali, {pelanggan_aktif['nama']}!")

                pelanggan_menu(pelanggan_aktif)
                break
            else:
                print("ID pelanggan tidak ditemukan! Silakan coba lagi.")
        elif pilihan == "0":
            main()
        else:
            print("Pilihan tidak valid! Silakan pilih kembali.")

def pelanggan_menu(pelanggan_aktif):
    while True:
        print("\n=== Calestia Facial Treatment ===")
        print("1. Tampilkan Treatment")
        print("2. Jadwal Harian Treatment")
        print("3. Reservasi")
        print("4. Edit Data Diri")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_treatment()
        elif pilihan == "2":
            jadwal_harian()
        elif pilihan == "3":
            reservasi(pelanggan_aktif)
            #reservasi()
        elif pilihan == "4":
            update_data_diri(pelanggan_aktif["id"])
        elif pilihan == "0":
            print(f"Terima kasih, {pelanggan_aktif['nama']}! Jangan lupa ID Anda: {pelanggan_aktif['id']}")
            break
        else:
            print("Pilihan tidak valid!")

def tambah_pelanggan():
    print("\n=== Tambah Data Pelanggan ===")
    nama = input("Masukkan nama pelanggan: ")
    while True:
        usia = input("Masukkan usia (minimal 16): ").strip()
        
        if usia.isdigit() and int(usia) >= 16:
            break 
        print("Usia minimal adalah 16 dan harus berupa angka. Silakan coba lagi.")

    while True:
        gender = input("Masukkan gender (male/female): ").lower()
        if gender in ['male', 'female']:
            break
        print("Gender harus 'male' atau 'female'. Silakan coba lagi.")

    no_telp = input("Masukkan nomor telepon: ")
    jenis_kulit = input("Masukkan jenis kulit (1. berminyak, 2. normal, 3. kombinasi, 4. sensitif): ")

    id_pelanggan = f"PL{len(data_pelanggan) + 1:03}"
    pelanggan_baru = {
        "id": id_pelanggan,
        "nama": nama,
        "usia": usia,
        "gender": gender,
        "no_telp": no_telp,
        "jenis_kulit": jenis_kulit
    }
    data_pelanggan.append(pelanggan_baru)
    print(f"Pelanggan berhasil ditambahkan! ID Anda adalah {id_pelanggan}. Simpan ID ini untuk login di masa mendatang.")
    
    return pelanggan_baru

def tampilkan_treatment():
    print("\n===== Daftar Treatment =====")
    for treatment in data_treatment:
        print(f"ID Treatment   : {treatment['id']}")
        print(f"Jenis          : {treatment['jenis']}")
        print(f"Harga          : {treatment['harga']}")
        print("============================")

# Reservasi pelanggan =============

def reservasi(pelanggan_aktif):  
    print("\n=== Reservasi ===")
    id_pelanggan = pelanggan_aktif["id"] 
    print(f"ID Pelanggan: {id_pelanggan} ({pelanggan_aktif['nama']})")

    tanggal = input("Masukkan tanggal reservasi (DD-MM-YYYY): ")
    jadwal_harian()
    kode_jadwal = input("Masukkan kode jadwal (dusk/noon/dawn): ").lower()
    if kode_jadwal not in jadwal_kode:
        print("Kode jadwal tidak valid!")
        return

    if any(r["id_pelanggan"] == id_pelanggan and r["tanggal"] == tanggal and r["kode_jadwal"] == kode_jadwal for r in data_reservasi):
        print("Anda sudah memiliki reservasi di jadwal ini. Silakan pilih jadwal lainnya.")
        return

    jenis_treatment = []
    total_harga = 0
    while True:
        tampilkan_treatment()
        id_treatment = input("Pilih ID Treatment (atau ketik 'done' untuk selesai): ").upper()
        if id_treatment == "DONE":
            if not jenis_treatment:
                print("Anda harus memilih minimal 1 treatment!")
                continue
            break
        treatment = next((t for t in data_treatment if t["id"] == id_treatment), None)
        if treatment:
            if id_treatment in jenis_treatment:
                print("Treatment ini sudah dipilih! Silakan pilih treatment lain.")
            else:
                jenis_treatment.append(id_treatment)
                total_harga += treatment["harga"]
                print(f"Treatment {treatment['jenis']} ditambahkan.")
        else:
            print("ID treatment tidak valid! Silakan coba lagi.")

    # Diskon
    diskon_member = 0
    if input("Apakah Anda memiliki kartu member? (y/n): ").lower() == "y":
        diskon_member = total_harga * 0.05

    diskon_total = 0
    if total_harga >= 1500000:
        diskon_total = total_harga * 0.03

    total_diskon = diskon_member + diskon_total
    total_akhir = total_harga - total_diskon
    print(f"Total Harga       : {total_harga}")
    print(f"Diskon Member     : {diskon_member}")
    print(f"Diskon Tambahan   : {diskon_total}")
    print(f"Total Akhir       : {total_akhir}")

    id_reservasi = f"RV{len(data_reservasi) + 1:03}"
    data_reservasi.append({
        "id": id_reservasi,
        "id_pelanggan": id_pelanggan,
        "tanggal": tanggal,
        "kode_jadwal": kode_jadwal,
        "jenis_treatment": jenis_treatment,
        "status": "scheduled"
    })
    print(f"Reservasi berhasil dibuat dengan ID {id_reservasi}!")
    print(f"Total yang harus dibayar: {total_akhir}")

    cetak_nota(id_reservasi)
    return

def cetak_nota(id_reservasi):
    reservasi = next((r for r in data_reservasi if r['id'] == id_reservasi), None)
    if not reservasi:
        print("ID reservasi tidak ditemukan!")
        return

    pelanggan = next((p for p in data_pelanggan if p['id'] == reservasi['id_pelanggan']), None)
    print("\n=== Calestia Facial Treatment ===")
    print("\n=== Nota Reservasi ===")
    print(f"ID Reservasi  : {reservasi['id']}")
    print(f"Nama Pelanggan: {pelanggan['nama'] if pelanggan else 'Tidak diketahui'}")
    print(f"Tanggal        : {reservasi['tanggal']}")
    print(f"Jadwal         : {jadwal_kode[reservasi['kode_jadwal']]}")
    print("Jenis Treatment:")
    for id_treatment in reservasi['jenis_treatment']:
        treatment = next((t for t in data_treatment if t['id'] == id_treatment), None)
        if treatment:
            print(f"- {treatment['jenis']} ({treatment['harga']})")
    print(f"Status         : {reservasi['status']}")
    print("===============================")

def update_data_diri(id_login):
    print("\n=== Edit Data Diri ===")
    
    for pelanggan in data_pelanggan:
        if pelanggan["id"] == id_login:
            print("Data Diri Anda:")
            print(f"Nama          : {pelanggan['nama']}")
            print(f"Usia          : {pelanggan['usia']}")
            print(f"Gender        : {pelanggan['gender']}")
            print(f"Nomor Telepon : {pelanggan['no_telp']}")
            print(f"Jenis Kulit   : {pelanggan['jenis_kulit']}")
            
            nama_baru = input(f"Nama (kosongkan untuk tidak mengubah, saat ini: {pelanggan['nama']}): ")
            if nama_baru:
                pelanggan["nama"] = nama_baru
            
            usia_baru = input(f"Usia (kosongkan untuk tidak mengubah, saat ini: {pelanggan['usia']}): ")
            if usia_baru:
                pelanggan["usia"] = int(usia_baru)
            
            gender_baru = input(f"Gender (kosongkan untuk tidak mengubah, saat ini: {pelanggan['gender']}): ")
            if gender_baru:
                pelanggan["gender"] = gender_baru.lower()
            
            no_telp_baru = input(f"Nomor telepon (kosongkan untuk tidak mengubah, saat ini: {pelanggan['no_telp']}): ")
            if no_telp_baru:
                if len(no_telp_baru) <= 13:
                    pelanggan["no_telp"] = no_telp_baru
                else:
                    print("Nomor telepon terlalu panjang! Tidak mengubah nomor telepon.")
            
            jenis_kulit_baru = input(f"Jenis kulit (kosongkan untuk tidak mengubah, saat ini: {pelanggan['jenis_kulit']}): ")
            if jenis_kulit_baru:
                pelanggan["jenis_kulit"] = jenis_kulit_baru
            
            print("Data Anda berhasil diperbarui!")
            return
        
    print("Data tidak ditemukan.")

# Fungsi Utama
def main():
    while True:
        print("\n=== Calestia Facial Treatment ===")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Pelanggan")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            password = input("Masukkan password admin: ")
            if password == "admin123":
                admin_menu()
            else:
                print("Password salah!")
        elif pilihan == "2":
            pilih_pelanggan()
        elif pilihan == "0":
            print("Selamat Tinggal!")
            exit()
        else:
            print("Pilihan tidak valid!")

main()