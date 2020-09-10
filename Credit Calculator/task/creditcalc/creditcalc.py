import argparse, sys, math

parser = argparse.ArgumentParser(description="calculate differentiated payment")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("--type", choices=['annuity', 'diff'], help="indicated the type of payment: 'annuity' or 'diff'")
parser.add_argument("--payment", type=int, help="monthly payment")
parser.add_argument("--principal", type=int, help="the principal")
parser.add_argument("--periods", type=int, help="number of months")
parser.add_argument("--interest", type=float, help="interest without")
args = parser.parse_args()


def calculate_differentiated_payment(interest, periods, principal):
    i = interest / (12 * 100)
    differentiated_payment = []
    for m in range(1, periods+1):
        differentiated_payment.append(math.ceil((principal / periods) + i * (principal - ((principal * (m - 1)) / periods))))
    return differentiated_payment


def calculate_annuity_payment(principal, periods, interest):
    i = interest / (12 * 100)
    payment = math.ceil(principal * ((i * (1 + i) ** periods) / (((1 + i) ** periods) - 1)))
    return payment

def calculate_annuity_principal(payment, periods, interest):
    i = interest / (12 * 100)
    onepiton = (1 + i) ** periods
    den = (i * onepiton) / (onepiton - 1)
    answer = math.floor(payment / den)
    return answer

def calculate_annuity_years(principal, payment, interest):
    i = interest / (12 * 100)
    months = math.log((payment / (payment - i * principal)), (1 + i))
    return months

def months_to_years(months):
    mo = math.ceil(months)
    yr = int((mo - (mo % 12)) / 12)
    rem = mo % 12
    if mo > 12 and mo % 12 != 0:
        return f'{yr} years and {rem} months'
    elif mo > 12 and mo % 12 == 0:
        return f'{yr} years'
    elif mo == 12:
        return f'1 year'
    else:
        return f'{mo} months'
    pass

if not args.type:
    print("Incorrect parameters")
    # print(args.type)
    exit()
if args.type == "diff" and args.payment:
    print("Incorrect parameters")
    # print(f'args.principal: {args.principal}')
    # print(f'args.type: {args.type}')
    exit()
if not args.interest:
    print("Incorrect parameters")
    # print(f'args.interest: {args.interest}')
    exit()
if len(sys.argv) <= 4:
    print("Incorrect parameters")
    # print(f'len(sys.argv): {len(sys.argv)}')
    exit()
if args.interest < 0:
    print("Incorrect parameters")
    # print(f'args.periods: {args.periods}')
    # print(f'args.principal: {args.principal}')
    # print(f'args.interest: {args.interest}')
    exit()
elif args.interest and args.periods and args.principal and args.type == 'diff':
    payments = calculate_differentiated_payment(args.interest, args.periods, args.principal)
    for month, payment in enumerate(payments, 1):
        print(f'Month {month}: payment is {payment}')
    print(f'\nOverpayment = {sum(payments)-args.principal}')
elif args.type == 'annuity' and args.principal and args.periods and args.interest:
    payment = calculate_annuity_payment(args.principal, args.periods, args.interest)
    print(f'Your annuity payment = {payment}!')
    print(f'Overpayment = {payment*args.periods - args.principal}')
elif args.type == 'annuity' and args.payment and args.periods and args.interest:
    principal = calculate_annuity_principal(args.payment, args.periods, args.interest)
    print(f'Your credit principal = {principal}!')
    print(f'Overpayment = {args.payment * args.periods - principal}')
elif args.type == 'annuity' and args.principal and args.payment and args.interest:
    months = calculate_annuity_years(args.principal, args.payment, args.interest)
    time = months_to_years(months)
    print(f'It will take {time} to repay this credit!')
    print(f'Overpayment = {args.payment * math.ceil(months) - args.principal}')

