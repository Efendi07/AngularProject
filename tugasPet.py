from os import system

# Ketentuan Nilai Kehadiran 10%, Tugas 20%, UTS 30%, UAS 40%
# Ketentuan Predikat
# Deklarasi Variabel
d_namaMakul = []
d_hadir = []
d_tugas = []
d_uts = []
d_uas = []
d_total = []
d_akhir = []
d_predikat = []


def judul():
    print('=====================================')
    print('|    PROGRAM NILAI DATA MAHASISWA   |')
    print('=====================================')

def menu():
    system('cls')
    print('=====================================')
    print('Input Data Nilai Mahasiswa'.center(40))
    print('=====================================')
    print('| 1. Tambah Data                    |')
    print('| 2. Lihat Data Mahasiswa           |')
    print('| 3. Selesai                        |')
    print('=====================================')
    pilih = input('Pilih Menu : ')
    if pilih == '1':
        tambah()
    elif pilih == '2':
        lihat()
    elif pilih == '3':
        selesai()
    else:
        tidak = input('Menu Tidak Ada ')
        system('cls')
        menu()

def tambah():
    system('cls')
    judul()
    print('Tambah Data'.center(40))
    print('=====================================')
    
    
    namaMakul = input('Nama Mata Kuliah  : ')
    d_namaMakul.append(namaMakul)
    
    system('cls')
    judul()
    print('Tambah Data'.center(40))
    print('=====================================')
    hadir = float(input('Jumlah Hadir : '))
    j_hadir = ((hadir)*10/100)
    d_hadir.append(j_hadir)

    tugas = float(input('Nilai Tugas  :'))
    j_tugas = tugas*(20/100)
    d_tugas.append(j_tugas)

    uts = float(input('Nilai UTS  :'))
    j_uts = uts*(30/100)
    d_uts.append(j_uts)

    uas = float(input('Nilai UAS  : '))
    j_uas = uas*(40/100)
    d_uas.append(j_uas)

    total = j_hadir+j_tugas+j_uts+j_uas
    d_total.append(total)
    print ('Data Tersimpan'.center(40))
    kembali = input('Kembali [enter]')
    menu()

def lihat():
    system('cls')
    judul()


    for i in range (len(d_namaMakul)):
        # if d_total >= 80 :
        #     d_predikat = "A"
        # elif d_total >= 70 and d_akhir <80:
        #     d_predikat = "B"
        # elif d_total >= 50 and d_akhir <70:
        #     d_predikat = "C"
        # elif d_total <50 :
        #     d_predikat = "D"
        # else :
        #     d_predikat = "E"
        

        print('%d. Nama Mata Kuliah   : %s'%(i+0, d_namaMakul[i]))
        print('    Kehadiran   : %.2f'%d_hadir[i])
        print('    Tugas       : %.2f'%d_tugas[i])
        print('    UTS         : %.2f'%d_uts[i])
        print('    UAS         : %.2f'%d_uas[i])
        print('    Total Nilai : %.2f'%d_total[i])
        # print('    Predikat    : %.2f'%d_predikat[i])
        print('---------------------------')
        
        
        print('--------TOTAL NILAI--------')
        # d_akhir = d_total[i] % i
        # print('    Nilai Akhir : %.2f'%d_akhir[i])
        # print('    Predikat    : %.2f'%d_predikat[i])
        
        
    kembali = input('Kembali Tekan [enter]')
    menu()

def selesai():
    exit()
    
menu()
