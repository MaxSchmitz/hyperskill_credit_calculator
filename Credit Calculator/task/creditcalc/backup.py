import math
import sys


def get_choice():
    print('What do you want to calculate?')
    print('type "n" for the count of months,')
    print('type "a" for the annuity monthly payment,')
    print('type "p" - for the credit principal:')
    user_choice = input()
    return user_choice


class CreditCalculator:

    def __init__(self):
        self.principal = None
        self.payment = None
        self.months = None
        self.lastpayment = None
        self.interest = None

        pass

    def get_principal(self):
        print('Enter the credit principal:')
        self.principal = int(input())
        return self.principal

    def get_payment(self):
        print('Enter the monthly payment:')
        self.payment = float(input())
        return self.payment

    def get_months(self):
        print('Enter the number of periods:')
        self.months = int(input())
        return self.months

    def get_interest(self):
        print('Enter the credit interest:')
        self.interest = float(input()) / (12 * 100)
        return self.interest

    def main_menu(self):
        # self.get_principal()
        choice = get_choice()
        if choice == 'n':
            self.get_principal()
            self.get_payment()
            self.get_interest()
            self.calculate_months()
            self.print_months()
        elif choice == 'a':
            self.get_principal()
            self.get_months()
            self.get_interest()
            self.calculate_payment()
            self.print_payment()
        elif choice == 'p':
            self.get_payment()
            self.get_months()
            self.get_interest()
            self.calculate_principal()
            self.print_principal()

        pass

    def calculate_months(self):
        # print(self.principal)
        # print(self.payment)
        # print(self.interest)
        self.months = math.log((self.payment / (self.payment - self.interest * self.principal)), (1 + self.interest))
        return self.months

    def calculate_payment(self):
        # self.payment = math.ceil(int(self.principal) / int(self.months))
        # self.lastpayment = int(self.principal) - (int(self.months) - 1) * int(self.payment)
        self.payment = self.principal * ((self.interest * (1 + self.interest) ** self.months) / (((1 + self.interest) ** self.months) - 1))
        pass

    def calculate_principal(self):
        # print(self.payment)
        # print(self.interest)
        # print(self.months)
        onepiton = (1 + self.interest) ** self.months
        # print(onepiton)
        den = (self.interest * onepiton) / (onepiton - 1)
        # print(den)
        self.principal = self.payment / den
        pass

    def calculate_interest(self):
        pass

    def print_months(self):
        mo = math.ceil(self.months)
        yr = int((mo - (mo % 12)) / 12)
        rem = mo % 12
        if mo > 12 and mo % 12 !=0:
            print(f'You need {yr} years and {rem} months to repay this credit!')
        elif mo > 12 and mo % 12 == 0:
            print(f'You need {yr} years to repay this credit!')
        elif mo == 12:
            print(f'You need 1 year to repay this credit!')
        else:
            print(f'You need {mo} months to repay this credit!')
        pass

    def print_payment(self):
        print(f'Your annuity payment = {math.ceil(self.payment)}!')
        pass

    def print_principal(self):
        print(f'Your credit principal = {math.ceil(self.principal)}!')
        pass

    def compute_differentiated_payment(self):

        pass



run = CreditCalculator()
run.main_menu()
