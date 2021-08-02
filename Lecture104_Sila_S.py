class Customer :
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Add to Cart")

    def notifyCustormer(self):
        print(f"Added product to {self.name} {self.lastname}'s cart.")


customer1 = Customer()
customer1.name = "Sila"
customer1.lastname = "Sob-aeam"
customer1.notifyCustormer()

customer2 = Customer()
customer2.name = "Somnuek"
customer2.lastname = "Mahakan"
customer2.notifyCustormer()

customer3 = Customer()
customer3.name = "Surin"
customer3.lastname = "Sob-aeam"
customer3.notifyCustormer()