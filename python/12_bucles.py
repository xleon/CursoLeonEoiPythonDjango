def print_everything(*args):
    for n in args:
        print(n)

print_everything('manzana', 'plátano', 'pera')

def print_all_with_position(*args):
    for count, thing in enumerate(args):
        print('{}. {}'.format(count, thing))

print_all_with_position('manzana', 'plátano', 'pera')

counter = 0
while True:
    counter += 1
    print(counter)
    if counter > 90:
        break
    
print('fin del while')

def count_until(n=3):
    counter = 0
    while counter < n:
        counter += 1
        print(counter)

count_until(30)
# count_until(800)

def show_keyword_arguments(**kwargs):
    for name, value in kwargs.items():
        print('{}: {}'.format(name, value))

show_keyword_arguments(uno=1, dos=2, nombre='Carlos')