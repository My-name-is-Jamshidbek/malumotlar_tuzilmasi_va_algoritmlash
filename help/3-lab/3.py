class Mebel:
    def __init__(self,uzunligi,turi,vazni):
        self.uzunligi = uzunligi
        self.turi = turi
        self.vazni = vazni
    def vazni_haqida(self):
        """
        mebel vazni
        :return:
        """
        return self.vazni()
    def turi_haqida(self):
        """
        mebel turi
        :return:
        """
        return self.turi()
    def uzunligi_haqida(self):
        """
        mebelning uzunligi
        :return:
        """
        return self.uzunligi()
    def umumiy_malumot(self):
        """
        ummumiy malumot
        :return:
        """
        return f"vazni:{self.vazni}\nturi:{self.turi}\nuzunligi:{self.uzunligi}"