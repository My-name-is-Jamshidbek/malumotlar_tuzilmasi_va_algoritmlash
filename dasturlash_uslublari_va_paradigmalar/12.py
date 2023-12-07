class Telefon:
    def __init__(self, abonent_ismi, raqam, manzil, turi):
        self.abonent_ismi = abonent_ismi
        self.raqam = raqam
        self.manzil = manzil
        self.turi = turi

    def __str__(self):
        return f"{self.abonent_ismi}, {self.raqam}, {self.manzil}, {self.turi}"


def create_telefon_list(input_file):
    telefon_list = []
    with open(input_file, 'r') as file:
        for _ in range(10):
            line = file.readline().strip()
            if line:
                abonent_ismi, raqam, manzil, turi = line.split(', ')
                telefon = Telefon(abonent_ismi, raqam, manzil, turi)
                telefon_list.append(telefon)
    return telefon_list


def write_output_file(output_file, telefon_list):
    with open(output_file, 'w') as file:
        for telefon in telefon_list:
            file.write(str(telefon) + '\n')


def main():
    input_file = '/home/kkr/projects/malumotlar_tuzilmasi_va_algoritmlash/dasturlash_uslublari_va_paradigmalar/input.txt'
    output_file = '/home/kkr/projects/malumotlar_tuzilmasi_va_algoritmlash/dasturlash_uslublari_va_paradigmalar/output.txt'
    telefon_list = create_telefon_list(input_file)
    filtered_telefon_list = [telefon for telefon in telefon_list if telefon.raqam.startswith('93')]
    write_output_file(output_file, filtered_telefon_list)


if __name__ == "__main__":
    main()
