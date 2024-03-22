class BMI_Calculator:
    def __init__(self, berat, tinggi):
        self.berat = berat  #Berat dalam kilogram
        self.tinggi = tinggi  #Tinggi dalam meter

    def BMI_Value(self):
        return self.berat / (self.tinggi ** 2)

    def __eq__(self, other):
        return self.berat == other.berat and self.tinggi == other.tinggi


def main():
    try:
        #Input berat dan tinggi orang pertama
        berat1 = float(input("Masukkan berat orang pertama dalam kilogram (contoh : 70): "))
        tinggi1 = float(input("Masukkan tinggi orang pertama dalam meter (contoh : 1.70): "))

        #Input berat dan tinggi orang kedua
        berat2 = float(input("Masukkan berat orang kedua dalam kilogram (contoh : 70): "))
        tinggi2 = float(input("Masukkan tinggi orang kedua dalam meter (contoh : 1.70): "))

        #Buat objek BMI_Calculator untuk orang pertama dan kedua
        person1 = BMI_Calculator(berat1, tinggi1)
        person2 = BMI_Calculator(berat2, tinggi2)

        #Bandingkan dua objek BMI_Calculator menggunakan metode __eq__
        if person1 == person2:
            print("Berat dan tinggi kedua orang sama.")
        else:
            print("Berat dan/atau tinggi kedua orang berbeda.")

        #Output nilai BMI untuk kedua orang
        print("Nilai BMI untuk orang pertama:", person1.BMI_Value())
        print("Nilai BMI untuk orang kedua:", person2.BMI_Value())

    except ValueError:
        print("Masukkan berat dan tinggi dalam format yang benar.")


if __name__ == "__main__":
    main()