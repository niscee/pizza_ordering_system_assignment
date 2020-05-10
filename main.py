class Cart:
    def __init__(self):
        self.pizza = []
        self.pasta = []

    def choose_item(self):   #choosing the order menu
        while True:
            try:
                choose_item = int(input("Enter 1 for 'PIZZA' and 2 for 'PASTA':"))
                if choose_item == 1 or choose_item == 2:
                    item_name = "Pizza"
                    if choose_item == 2: item_name = "Pasta"
                    no_of_item = int(input(f'Choose NO of {item_name}:'))
                    self.pasta.append(no_of_item) if choose_item == 2 else self.pizza.append(no_of_item)
                    break
                else:
                    print('INVALID INPUT')
            except:
                print("INVALID INPUT")


    def order_more(self):  #option for adding more item to menu
        add_more = (input("Want to add more?..Enter y for 'Yes' and n for 'No': ")).upper()
        if add_more == 'Y':
            return True
        elif add_more == 'N':
            return False
        else:
            self.order_more()



class Total(Cart):
      def __init__(self):
          super().__init__()
          self.total_pizza = 0
          self.total_pasta = 0
          self.complimentary_bread = 0
          self.complimentary_drink = 0
          self.complimentary_special = 0

      def total_items(self):  #cart total number of individual menu
          self.total_pizza += sum(self.pizza)
          self.total_pasta += sum(self.pasta)


      def total_complimentary(self):  #total number of complimentary stuff
           self.complimentary_bread = self.total_pizza // 3

           self.complimentary_drink = self.total_pasta // 3

           self.complimentary_special = min(self.complimentary_bread,self.complimentary_drink)



      def total(self):  #display total number of pizza and pasta
          print(f'{self.total_pizza} Pizza and  {self.total_pasta} Pasta')





class Price(Total,Cart):
       def __init__(self):
           super().__init__()
           self.total_pizzaprice = 0
           self.total_pastaprice = 0
           self.total_orderprice = 0

       def total_price_pizza(self):    #total price of pizza items
           if self.total_pizza == 1:
               self.total_pizzaprice += 12
           elif self.total_pizza ==2:
               self.total_pizzaprice += 22
           else:
               self.total_pizzaprice = self.total_pizza*10



       def total_price_pasta(self):    #total price of pasta items
           if self.total_pasta == 1:
               self.total_pastaprice += 8
           elif self.total_pasta == 2:
               self.total_pastaprice += 15
           else:
               self.total_pastaprice = self.total_pasta*7



       def total(self):  #display total price of pizza and pasta

          print('**************************************************************************')
          print('Total_No                  Sub_Total Price')
          if self.total_pizza>0:
             print(f'Pizza: {self.total_pizza}                       ${self.total_pizzaprice}')
          if self.total_pasta > 0:
             print(f'Pasta: {self.total_pasta}                       ${self.total_pastaprice}')
          print('**************************************************************************')
          print(f'Total : ${self.total_pizzaprice + self.total_pastaprice}')
          print('--------------------------------------------------------------------------')
          print('Complimentary:')
          if(self.complimentary_bread > 0):
              print(f'{self.complimentary_bread} Garlic bread')

          if(self.complimentary_drink > 0):
              print(f'{self.complimentary_drink} Soft Drinks')

          if (self.complimentary_special > 0):
              print(f'{self.complimentary_special} Desert ')

          









print('-------------------------------------------------------------------------------------')
print("                        Please Place Your Order:")
print('-------------------------------------------------------------------------------------')


obj1 = Price()
while True:
      obj1.choose_item()
      confirm = obj1.order_more()
      if not confirm: break

obj1.total_items()
obj1.total_price_pizza()
obj1.total_price_pasta()
obj1.total_complimentary()
obj1.total()





