class rentalProperty():
    def __init__ (self):
        self.income_items = {}
        self.final_income = 0
        self.expense_items = {}
        self.final_expenses = 0
        self.ROI_items = {}
        self.final_ROI = 0
        self.cashOnCash_items = {}
        self.final_cashOnCash = 0
        self.sum_of_cashOnCash = 0

        
    def addIncomeItems(self):
        new_income_item = input('Please enter the name of the item on your rental income list ')
        new_income_item_price = int(input(f'Please enter the price of the item on your rental income list '))
        self.income_items[new_income_item] = new_income_item_price
        self.final_income = str(sum(self.income_items.values()))
        add_another_income = input('Would you like to add another item to the income list ? "yes" or "no" ').lower()
        while True:
            if add_another_income == 'yes':
                rentalProperty.addIncomeItems(self)   
                break 
            else:
                break
        return f'Please see your the items on your rental income list {self.income_items} \n The income total is ${self.final_income}'
                
        
    def rentalExpenses(self):
        new_expense_item = input('Please enter the name of the item on your rental expense list ')
        new_expense_item_price = int(input('Please enter the price of the item on your rental expense list '))
        self.expense_items[new_expense_item] = new_expense_item_price
        self.final_expenses = str(sum(self.expense_items.values()))
        add_another_expense = input('Would you like to add another item to the income list ? "yes" or "no" ').lower()
        while True:
            if add_another_expense == 'yes':
                rentalProperty.rentalExpenses(self)   
                break   
            else:
                break
        return f'Please see your the items on your rental expense list {self.expense_items} \n The total expenses are ${self.final_expenses}'
          


    def cashOnCash(self):
        downPayment = int(input('How much was your down payment? '))
        closingCost = int(input('How much was your closing costs? '))
        rehabBudget = int(input('How much was your rehab budget? '))
        while True:
            add_cashOnCash_expense = input('Would you like to add another item to the cash on cash list ? "yes" or "no" ').lower()
            if add_cashOnCash_expense == 'yes':
                new_cashOnCash_item = input('Please enter the name of the item on your cash on cash list ')
                new_cashOnCash_item_price = int(input('Please enter the price of the item on your cash on cash list '))
                self.cashOnCash_items[new_cashOnCash_item] = new_cashOnCash_item_price
                self.sum_of_cashOnCash =sum([value for value in self.cashOnCash_items.values()])
        
                self.final_cashOnCash = str(sum([self.sum_of_cashOnCash, downPayment, closingCost, rehabBudget]))   
                print({self.final_cashOnCash})
               
            else:
                self.final_cashOnCash = str(sum([self.sum_of_cashOnCash, downPayment, closingCost, rehabBudget]))   
                break
        return f'Please see your the items on your cash on cash list {self.cashOnCash_items} \n The total cash on cash items are ${self.final_cashOnCash }'

    def total_investment(self):
        rental_ROI = ((int(self.final_income) + int(self.final_expenses)) * 12 )/int(self.final_cashOnCash)
        return f'Your ROI is {rental_ROI}'

    def runner(self):
        while True:
            action = input('Type "start" to start the ROI calculator or "quit" to quit ').lower()
            if action == 'start':
                ROI_for_rental = rentalProperty()
                print(ROI_for_rental.addIncomeItems())
                print(ROI_for_rental.rentalExpenses())
                print(ROI_for_rental.cashOnCash())
                print(ROI_for_rental.total_investment())
            else:
                print('Thanks for using my ROI calculator, keep on investing! ')
                break


ROI_Calculator = rentalProperty()
ROI_Calculator.runner()

