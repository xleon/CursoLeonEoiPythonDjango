"""
Ejemplo simple de calculadora para IVA e IRPF dada una base imponible
"""

from colorama import init, Fore, Back, Style
init()

IVA_PERCENT = 0.21
IRPF_PERCENT = 0.15
CURRENCY = '€'

def run():
    separator = '----------------------------'
    print('\nCalculadora de IVA / IRPF')

    def format_number(number):
        return '{0:,.2f}'.format(number)

    while True:
        print(separator + Fore.CYAN)
        subtotal_str = input('Escribe base imponible (decimales con punto): ')
        try:
            subtotal = float(subtotal_str) if '.' in subtotal_str else int(subtotal_str)
            iva = subtotal * IVA_PERCENT
            irpf = subtotal * IRPF_PERCENT
            total = subtotal + iva - irpf
            revenue = subtotal - irpf
            print(Fore.WHITE + separator)
            print('Subtotal:', format_number(subtotal), CURRENCY)
            print('IVA:', format_number(iva), CURRENCY)
            print('IRPF: -' + Fore.RED + format_number(irpf) + Fore.WHITE, CURRENCY)
            print('Total:', Fore.CYAN + format_number(total) + Fore.WHITE, CURRENCY)
            print('Neto:', Fore.GREEN + format_number(revenue) + Fore.WHITE, CURRENCY)
            print(' ')
        except ValueError:
            print('formato de cantidad no válido')
        
if __name__ == '__main__':
    run()