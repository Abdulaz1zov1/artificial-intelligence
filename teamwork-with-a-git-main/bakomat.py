class carta:
    def init(self,raqam,mudat,parol,hisobi):
        self.raqam = raqam
        self.mudat = mudat
        self.parol = parol
        self.hisobi = hisobi

    def parolni_almashtirish(self):
        paral = input("eski parolni kiriting: ")
        if self.parol == paral:
            yangi_p = input("yangi parolni kiriting: ")
            self.parol = yangi_p
            print ("operatsiya muvaffaqiyatli amalga oshirildi!...")
        else:
            print ("parol natogri")
            print("parolni qayta kiriting ")
            self.parolni_almashtirish()

    def hisob_ustida_a(self,ozgarma):
        if (self.hisobi+ozgarma)>0:
            self.hisobi += ozgarma
            print ("operatsiya muvaffaqiyatli amalga oshirildi!...")
        else:
            print("kartada mablag' yetarlimas ")

    def karta_hisobi(self):
        return f"""Karta\nRaqami: {self.raqam}\
            \nHisobi: {self.hisobi}\n\
            """
    def repr(self):
        return f"<class karta>: {self.raqam} {self.mudat}"


class bankamat:
    def init(self):
        self.karta_raqam = input("karta raqamini kiriting: ")
        self.malumotlar_bazasini_y()

    def malumotlar_bazasini_y(self, rewrite=False):
        if rewrite:
            with open("karta_m.txt", "w") as f:
                for karta in self.kartalar:
                    data = [karta.raqam, karta.mudat, karta.parol,str(karta.hisobi)]
                    if self.kartalar[-1]==karta:
                        f.write(" | ".join(data))
                    else:
                        f.write(" | ".join(data)+"\n")
        else:
            self.kartalar = []
            with open("karta_m.txt", "r") as f:
                for i in f.read().split("\n"):
                    karta = i.split(" | ")
                    self.kartalar.append(carta(karta[0], karta[1], karta[2], int(karta[3])))

    def naxt_pul_olish(self, ):
        sizni_kartayiz = self.karta_m_topish()
        ozgarma = int(input("sumani kiriting: "))
        sizni_kartayiz.hisob_ustida_a(-ozgarma)
        self.malumotlar_bazasini_y(rewrite=True)

    def hisobni_toldirish(self):
        sizni_kartayiz = self.karta_m_topish()
        suma = int(input("sumani kiriting: "))
        sizni_kartayiz.hisob_ustida_a(suma)
        self.malumotlar_bazasini_y(rewrite=True)

    def parolni_ozgartirish(self):
        sizni_kartayiz = self.karta_m_topish()
        sizni_kartayiz.parolni_almashtirish()
        self.malumotlar_bazasini_y(rewrite=True)

    def karta_hisobini_k(self):
        sizni_kartayiz = self.karta_m_topish()
        return sizni_kartayiz.karta_hisobi()

    def karta_m_topish(self):
        raqam = input("karta raqamini kiriting: ")
        for i in self.kartalar:
            if i.raqam == self.karta_raqam:
                return i
                break
        return -1
    def parolni_tekshir(self):
        sizni_kartayiz = self.karta_m_topish()
        parol = input("parolni kiriting: ")
        if sizni_kartayiz.parol == parol:
            return True
        else :
            print("parol nato'g'ri ")
            print("qayta kiriting ")
            self.parolni_tekshir()         

class bankamatni_ishlatish:
    def init(self):
        self.meni_kartam = bankamat()
        self.parolni_tekshirish()
    def parolni_tekshirish(self):
        self.meni_kartam.karta_m_topish()
        if self.meni_kartam == -1:
            print("karta topilmadi ")
            print ("qayta urinig ")
            self.meni_kartam.karta_m_topish()
        else :
            self.meni_kartam.parolni_tekshir()
            if self.meni_kartam:
                self.meni_kartam.karta_m_topish()
                self.amallar()

    def amallar(self):
        amal = int(input("Naxt pul yechish: 1,Hisobni ko'rish: 2, Kartani to'ldirish: 3, Parolni almashtirish: 4  Tanlang:... "))
        if amal == 1:
            self.meni_kartam.naxt_pul_olish()
            self.qayta_ishga_tushirish()

        elif amal == 2:
            print(self.meni_kartam.karta_hisobini_k())
            self.qayta_ishga_tushirish()

        elif amal == 3:
            self.meni_kartam.hisobni_toldirish()
            self.qayta_ishga_tushirish()

        elif amal == 4:
            self.meni_kartam.parolni_ozgartirish()
            self.qayta_ishga_tushirish()

        else:
            print("Bunaqa amal yo'q ")
            print("qayta tanlang ")
            self.amallar()

    def qayta_ishga_tushirish(self):
        print("yana bironta amal bajarishni hoxlaysizmi ")
        qaysi = input("ha yoki yoq: ")
        if qaysi == "ha":
            self.amallar()
        elif qaysi == "yoq":
            print ("bizning bankamatdan foydalanganiz uchun raxmat!...")
        else :
            print ("faqat ha yoki yoq ni tanlang ")
            self.qayta_ishga_tushirish()

#yangi malumot qoshish
        
meni_kartam = bankamatni_ishlatish()