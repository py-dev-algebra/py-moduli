# import datetime
# from datetime import *
from datetime import datetime as dt


# print(dt.datetime.now()) # 2024-01-18 20:10:50.735236
TAX = 0.25


class Customer:
    def __init__(self, 
                 name: str, 
                 vat_id: str, 
                 address: str) -> None:
        self.name = name
        self.vat_id = vat_id
        self.address = address


class Employee:
    def __init__(self, 
                 first_name: str, 
                 last_name: str, 
                 job_title: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title


class Items:
    def __init__(self,
                 title: str,
                 amount: float = 0.00,
                 unit_price: float = 0.00,
                 discount: float = 0.00) -> None:
        self.title = title
        self.amount = amount
        self.unit_price = unit_price
        self.discount = discount
        self.total_price = 0.00
        self.calculate_total_price()


    def calculate_total_price(self):
        self.total_price = (self.amount * self.unit_price) * (1 - (self.discount / 100))


class Invoice:
    def __init__(self, 
                 customer: Customer,
                 employee: Employee,
                 comment: str,
                 items: list[Items]) -> None:
        self.customer = customer
        self.employee = employee
        self.comment = comment
        self.items = items

        self.number = ''
        self.invoice_date = ''
        self.total = 0.00
        self.tax = TAX
        self.total_w_tax = 0.00
        self.construct_invoice_number()
        self.construct_invoice_date()
        self.calculate_total_price()


    def construct_invoice_number(self):
        self.number = f'I-{dt.now().strftime('%Y%m')}-{str(1).zfill(4)}' # 202401


    def construct_invoice_date(self):
        self.invoice_date = dt.now().strftime('%d.%m.%Y. %H:%M') # '18.01.2024. 20:05'

    def calculate_total_price(self):
        for item in self.items:
            self.total += item.total_price

        self.total_w_tax = self.total * (1 + self.tax)

    def print(self):
        pass # TODO Dovrsiti kao zadaca
        '''
        ZADACA - kreirati metodu koja ispisuje racun

        1. podaci korisnika
        2. podaci djelatnika
        3. Broj racuna TAB datum izdavanja
        4. header liste stavki (Nazlov TAB KOM TAB Jed. Cijena TAB Ukupno)
        5. lista vrijednosti ITEMA
        6. komentar ako ga ima, a ako nema nemojte ispisati nista
        '''










customer_01 = Customer('Pajdo und Jaranen GmbH',
                    '1234564',
                    'Berliner Str. 1234, 8000 Muenchen, D')

items = [
    Items('Notebook', 1.00, 890.99),
    Items('Monitor', 1.00, 530.99),
    Items('Python za pocetnike', 2.00, 35.59, 10),
]

invoice = Invoice(customer=customer_01,
                  employee=Employee('Pero', 'Peric', 'Direktor svemira'),
                  comment='',
                  items=items)



# print(invoice.total)
# print(invoice.total_w_tax)

# invoice.print()

print(invoice.customer.address)
print(customer_01.address)
