from fpdf import FPDF

class Shirtificate(FPDF):
    def __init__(self, name = "I"):
        super().__init__()
        self._name = name

    def header(self):
        self.set_font("Times", "B", size=48)
        self.set_text_color(0,0,0)
        self.cell(0, 40, "CS50 Shirtificate", align="C", center=True)
    def shirt_text(self):
        self.set_font("Times", size=24)
        self.set_text_color(250,250,250)
        self.cell(0, 260, f"{self._name} took CS50", align="C", center=True)

def main():
    pdf = Shirtificate(input("Name: "))
    pdf.add_page()
    pdf.image("shirtificate.png", x=10, y=70, w=190)
    pdf.shirt_text()
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()