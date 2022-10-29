class Hayvon:
    def __init__(self,nomi,turi,vazni):
        self.nomi = nomi
        self.turi = turi
        self.vazni = vazni
    def vazni_haqida(self):
        """
        hayvon vazni
        :return:
        """
        return self.vazni
    def turi_haqida(self):
        """
        hayvon turi
        :return:
        """
        return self.turi
    def nomi_haqida(self):
        """
        hayvon nomi
        :return:
        """
        return self.nomi
    def umumiy_malumot(self):
        """
        ummumiy malumot
        :return:
        """
        return f"vazni:{self.vazni}\nturi:{self.turi}\nnomi:{self.nomi}"
a = Hayvon(nomi='Sher',turi='Yirtqich',vazni='150')
print(a.turi_haqida())
print(a.vazni_haqida())
print(a.nomi_haqida())
print(a.umumiy_malumot())