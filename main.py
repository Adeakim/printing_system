# The entry point of you application
from data.data import resources,FORMAT
class Ability:
    '''
    this class contain three methods that chacks in the user require and match it with the ability of the 
    user to print in greyscale or coloured.
    the welcome method is to welcome the user.
    the format_type method ask the user to input their choice of printing and tell them how much the printint
    would cost them per page and
    the off method off the printer when the user type off.
        '''
    coloured_price=FORMAT['coloured']['price']
    greyscale_price=FORMAT['greyscale']['price']
    def __init__(self,colour_type):
        self.colour_type=colour_type
            
    def welcome(self):
        print('Welcome to our automated printing machine')
        
        
    def format_type(self):
        format=self.colour_type
        self.colour_type=input('What format would you like to print(coloured or greyscale)?\n ')
        
        while self.colour_type not in['coloured','off','greyscale','report']:
            self.colour_type=input('Invalid format. What format would you like to print(coloured or greyscale)?\n ')
        if self.colour_type=='coloured':
                print(f"coloured printing costs #{Ability.coloured_price} per page")
        elif self.colour_type=='greyscale':
                print(f"greyscale printing costs #{Ability.greyscale_price} per page")
    def off_printer(self):
        while self.colour_type=='off':
                print('Thank you for using our service.We hope to see you next time')
                exit()  

class MoneyOperation(Ability):
    '''
    This MoneyOperation class takes infomation from Ability class(inherit its method)
    process the price of the user_request together wih checking whether there's enough 
    resources to print the user request or not.
    The report method checks the report and returns the number of papers,volume of ink and the total profit 
    at the initial stage.
    The check_resource method checks whether the resources to print is enough or not.
    
    
        '''
    ink=resources['ink']
    paper=resources['paper']
    profit=resources['profit']
    def __init__(self,pages=0,required_ink=1):
        super().__init__(colour_type='')
        self.pages=pages
        self.required_ink=required_ink
       
    def report(self):
        if self.colour_type=='report':
            print(f'Ink :{MoneyOperation.ink}\npaper :{MoneyOperation.paper}\nprofit:{MoneyOperation.profit}')
            self.colour_type=input('What format would you like to print(coloured or greyscale)?\n ')
        Ability.off_printer(self)
        
    def check_resource(self):  
        while True:
            
            try:
                self.pages =int(input(('how many pages do you want to print: '))) 
                
                if self.colour_type=='coloured':
                    ink_per_page=7
                    self.required_ink=ink_per_page * self.pages
                
                elif self.colour_type=='greyscale':
                    ink_per_page=5
                self.required_ink=ink_per_page * self.pages
                break    
            except ValueError:
                print('Invalid number of pages. How many pages do you want to print')
   
    def further_check(self):
        while  self.pages>self.paper or self.required_ink >self.ink:
            print('There is no enough resources')
            MoneyOperation.check_resource(self)      
        
                
               
class ProcessPrice(MoneyOperation,Ability):
    '''
    The ProcessPrice class takes infomation from ability and Moneyopertaion and 
    process the price of the number of pages the user want to print and also collect
    money from the user.
    The amount method recieve the number of pages and calculate the amount it will cost
    the user and tell them.
    the insert currency method collect the money and check if the money inserted is enough to 
    print the number of pages requested.If enough,the printer prints their work and if not,the user 
    refund thei money.
    '''
    def __init__(self,total_deposit=0):
        super().__init__(pages=0,required_ink=1)
        self.total_deposit=total_deposit
        
    def amount(self,price=0):
        one_coloured_page=FORMAT['coloured']['price']
        one_greyscale_page=FORMAT['greyscale']['price']
        Ability.format_type(self)
        MoneyOperation.report(self)
        MoneyOperation.check_resource(self)
        MoneyOperation.further_check(self)
        if self.colour_type=='coloured':
            self.price=one_coloured_page* self.pages
            print(f'your price is #{self.price}')
        elif self.colour_type=='greyscale':
            self.price=one_greyscale_page* self.pages
            print(f'your price is #{self.price}')
        
    
    def insert_currency(self):
        print('Please insert currency')
        while True:
            try:
                
                biyar=int(input('How many Biyar: '))*5
                faiba=int(input('How many Faiba: '))*10
                muri=int(input('How many Muri: '))*20
                wazobia=int(input('How many Wazobia: ')) * 50  
                self.total_deposit= biyar + faiba + muri + wazobia
                break
            except ValueError:
                print('currency should be integer')
        if self.price>self.total_deposit:
            print("sorry that's not enough money,money refunded")
            
        elif self.price< self.total_deposit:
            balance=self.total_deposit-self.price
            print(f"Here's your #{balance} balance")
            print ("Here's your work")
            
        else:
            print ("Here's your work")
            
            
    
    def updated_report(self):
        while self.price< self.total_deposit or self.price==self.total_deposit:
            Ability.format_type(self)
            MoneyOperation.ink -=self.required_ink
            MoneyOperation.paper -=self.pages
            MoneyOperation.profit +=self.price
            if self.colour_type=='report':
                print(f'Ink :{MoneyOperation.ink}\npaper :{MoneyOperation.paper}\nprofit:{MoneyOperation.profit}')
            break   
            
            
            
def reusable():     
    testing=MoneyOperation()  
    controling=ProcessPrice()
    controling.amount()
    controling.insert_currency()
    controling.updated_report()
    
        
        
while True:
    reusable()
