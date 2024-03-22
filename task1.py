def main():
    try:
        #Buka file indata.txt untuk dibaca
        with open("indata.txt", "r") as file:
            #Membaca setiap baris dalam file
            lines = file.readlines()

            #Inisialisasi variabel untuk menyimpan jumlah
            total = 0

            #Loop melalui setiap baris dan tambahkan angka ke total
            for line in lines:
                #Konversi setiap baris menjadi integer dan tambahkan ke total
                total += int(line)

            #Output total dengan koma sebagai pemisah ribuan dan dua digit desimal
            print("{:,.2f}".format(total))

    except FileNotFoundError:
        print("File 'indata.txt' tidak ditemukan.")
    except ValueError:
        print("File 'indata.txt' berisi data yang tidak valid.")

if __name__ == "__main__":
    main()
