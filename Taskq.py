class Hesab:
    def __init__(self, hesab_nomresi: int, balans: float):
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans

    def balans_artir(self, mebleq: float):
        self.balans += mebleq
        print(f"{mebleq} AZN balansınıza əlavə olundu. Yeni balans: {self.balans} AZN")

    def pul_cek(self, mebleq: float):
        if mebleq <= self.balans:
            self.balans -= mebleq
            print(f"{mebleq} AZN balansınızdan çıxarıldı. Yeni balans: {self.balans} AZN")
        else:
            print("Kifayət qədər balansınız yoxdur.")

    def balans_goster(self):
        print(f"Hesab nömrəsi: {self.hesab_nomresi}, Balans: {self.balans} AZN")

class KreditHesab(Hesab):
    def __init__(self, hesab_nomresi: int, balans: float, kredit_mebliyi: float):
        super().__init__(hesab_nomresi, balans)
        self.kredit_mebliyi = kredit_mebliyi

    def kredit_ver(self):
        self.balans += self.kredit_mebliyi
        print(f"{self.kredit_mebliyi} AZN kredit olaraq hesabınıza əlavə olundu. Yeni balans: {self.balans} AZN")

    def kredit_odenisi(self):
        ayliq_odenis = self.kredit_mebliyi / 12
        self.balans -= ayliq_odenis
        print(f"Kredit ödənişi olaraq {ayliq_odenis} AZN balansınızdan çıxarıldı. Yeni balans: {self.balans} AZN")


hesab = Hesab(20202020, 1100.0)
hesab.balans_goster()
hesab.balans_artir(800.0)
hesab.pul_cek(300.0)


kredit_hesab = KreditHesab(789012, 2000.0, 10000.0)
kredit_hesab.balans_goster()
kredit_hesab.kredit_ver()
kredit_hesab.kredit_odenisi()
