import FoxHustle_QR


class QrCodeGenerator:
    url: str = None
    color: str = None
    filename: str = None

    def get_url(self):
        self.url = input("Entrez (ou copiez/collez) l'URL de destination : ")
        while not self.url.startswith('http'):
            print("L'URL n'est pas valide")
            self.get_url()
        return self.url

    def get_color(self):
        self.color: str = input("Entrez la couleur dominante (dark / light) : ")
        while self.color != 'dark' and self.color != 'light':
            print("Seulement 2 choix possibles, 'dark' ou 'light'")
            print("Recommencez l'opération...")
            self.get_color()
        return "colored " + self.color

    def get_filename(self):
        self.filename: str = input("Entrez un nom pour le QRcode : ")
        return self.filename + ".png"

    def generate_qrcode(self):
        QRGen = FoxHustle_QR.QRGenerator()
        try:
            link = QRGen(self.get_url(), qr=self.get_color())
            link.save(f'outputs/{self.get_filename()}')
            print(f"Votre QRcode {self.filename} a été créé avec succès...")
        except:
            print(f"\n\t Erreur lors de la création du QRCode {self.filename}... \n")
            print("\t Opération annulée...")


QrCodeGenerator().generate_qrcode()
