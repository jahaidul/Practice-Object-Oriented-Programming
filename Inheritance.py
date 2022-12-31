class Oneplus:
    company = "Oneplus"
    webiste = "www.oneplus.com"
 
    def contact_details(self):
        print("Address : Bhosundhara shopping Mall")
 
 
class Oneplus8(Oneplus):
    def __init__(self):
        self.name = "Oneplus8"
        self.year = 2013
 
    def product_details(self):
        print("Name     : ", self.name)
        print("Year     : ", self.year)
        print("Company  : ", self.company)
        print("Website  : ", self.webiste)
 
 
mobile = Oneplus8()
mobile.product_details()
mobile.contact_details()
 
