from googletrans import Translator



class Google_Tradutor:

    def __init__(self, name):
        self.name = name
        print(self.name)



    def __en__(self):

        translate = Translator()
        entrada1 = input(">>Texto em Português para Englês: ")
        entancia = translate.translate(entrada1, src="pt", dest="en")
        print(f"(*)EN: {entancia.text}\n")
        return translate



    def __pt__(self):

        translate = Translator()
        entrada2 = input(">>Texto em Englês para Português: ")
        entancia = translate.translate(entrada2, src="en", dest="pt")
        print(f"(*)PT: {entancia.text}\n")
        return translate



    def __ExecCode__(self):

        while True:

            entrada = input("[0] Português para Englês.\n[1] Englês para Português.\n\n(opcao): ")
            if entrada == "0":
                code_translate.__en__()

            elif entrada == "1":
                code_translate.__pt__()

            else:
                print(">> SinxtaError.")
                quit()



code_translate = Google_Tradutor(name="(API)\tGoogle Tranlator\n")

if __name__ == "__main__":
    code_translate.__ExecCode__()
