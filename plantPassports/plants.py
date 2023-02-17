
import jinja2
import pdfkit

template_loader = jinja2.FileSystemLoader(r'C:\Users\PC User\PycharmProjects\gaybay\plantPassports\plantPassports\templates')
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template(r'passport_template.html')

# C:\Program Files\wkhtmltopdf\bin

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')


class plant:
    def __init__(self, botName):
        self.order = "--"
        self.family = "---"
        self.parents = "--"
        self.number = 0

        self.botName = botName
        self.passportNumber = "This is the passport"

        self.pictures = []


    def makeID(self):
        self.id = self.order + self.family + self.parents + "0"*(4-len(str(self.number))) + str(self.number)

    def addPicture(self, pic):
        self.pictures.append(pic)

    def printPassport(self):


        output_text = template.render({'botName': self.botName,
                                       'passport': self.passportNumber,
                                       'plantID': self.id})

        pdfkit.from_string(output_text, 'pdf_generated.pdf', configuration=config)


class lithop(plant):
    def __init__(self, botName):
        super().__init__(botName)
        self.order = "LI"


# class


p = plant("david")
p.makeID()
p.printPassport()

l = lithop("david")
l.makeID()
