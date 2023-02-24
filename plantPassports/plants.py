
import jinja2
import pdfkit
import os

template_loader = jinja2.FileSystemLoader(os.getcwd() + r'\templates')
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template(r'passport_template.html')

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')


class plant:
    def __init__(self, botName, family="--", genus="--", species="MXX", parents="AA", ID=0):
        self.family = family
        self.genus = genus
        self.species = species
        self.parents = parents
        self.number = ID

        self.botName = botName
        self.passportNumber = "This is the passport"

        self.pictures = []


    def makeID(self):
        self.id = self.family + self.genus + self.species + self.parents + "0"*(4-len(str(self.number))) + str(self.number)

    def addPicture(self, pic):
        self.pictures.append(pic)

    def printPassport(self):


        output_text = template.render({'botName': self.botName,
                                       'passport': self.passportNumber,
                                       'plantID': self.id})

        pdfkit.from_string(output_text, 'pdf_generated.pdf', configuration=config)

class Aizoaceae(plant):
    def __init__(self, botName, genus="--", species="MXX", parents="AA", ID=0):
        super().__init__(botName, family="AZ", genus=genus, species=species, parents=parents, ID=ID)


class lithop(Aizoaceae):
    def __init__(self, botName, species="MXX", parents="AA", ID=0):
        super().__init__(botName, genus="LI", species=species, parents=parents, ID=ID)



# class


p = plant("david")
p.makeID()
p.printPassport()

l = lithop("david")
l.makeID()

l2 = lithop("david", ID=99)
l2.makeID()