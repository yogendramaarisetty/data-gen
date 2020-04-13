import os
from termcolor import colored, cprint
from generator import chooseOption
import my_custom_script
import random, string
import msvcrt as m

accounts_list = []
company_list = []
department_list = []
costcenter_list = []
businesscenter_list = ['Code_185', 'Code_186','Code_187']
productline_list = ['Code_465','Code_466','Code_467','Code_468']
geography_list = ['code_107']  # ,plan71,plan101,Code_107,Code_341,
icsegment_list = ['code341']
fiscalyears_list = [2013]
months_list = [1]
amounts_list = [1000]
segment_index_list = [ 
                      accounts_list,
                      company_list,
                      department_list,
                      costcenter_list,
                      businesscenter_list,
                      productline_list,
                      geography_list,
                      icsegment_list,
                      fiscalyears_list,
                      months_list,
                      amounts_list
                      ]
segment_list_mapper = {
    'account': accounts_list,
    'company': company_list,
    'department': department_list,
    'costcenter': costcenter_list,
    'businesscenter': businesscenter_list,
    'productline': productline_list,
    'geography': geography_list,
    'icsegment': icsegment_list,
    'fiscalyear': fiscalyears_list,
    'month': months_list,
    'amount': amounts_list
}


def integer_input(msg):
    try:
        print(colored(msg, 'white', attrs=['bold']), end=": ")
        a = int(input())
        return a
    except ValueError:
        cprint("Wrong Input! Please give integer input", 'white', 'on_red')
        print()
        chooseOption()
    except KeyboardInterrupt:
        exit()


# This method reads segements input from the file from  location - "./dataGenerator/input/<segment_name>.txt"
def file_reader(segment):
    segment_list = segment_list_mapper[segment]
    cwd = os.getcwd()
    input_file = open(os.path.join(cwd, f'input/{segment}.txt'), 'r')
    for line in input_file:
        line = line.rstrip('\n')
        segment_list.append(line)
    input_file.close()
    cprint(len(segment_list), 'red', attrs=['bold'], end="")
    print('', segment.lower() + "s read")


# This generates sequence for segment input data
def sequence_generator(segment):
    segment_list = segment_list_mapper[segment]
    cprint(
        f'Sequence generator example: \n if you want to generate sequence like below\n code1,code2,code3,code4...code 120\n  Preceding Sting: code\n  Starting Integer: 1\n  Ending Integer: 120',
        'grey')
    cprint('Preceding string', 'white', attrs=['bold'], end="")
    preceding_string = input()
    start = integer_input("Starting Integer")
    end = integer_input("Ending Integer")
    for i in range(start, end + 1):
        segment_list.append(f'{preceding_string}{i}')
    cprint(len(segment_list), 'red', attrs=['bold'], end="")
    print('', segment.lower() + "s read")


# Random number generator
def random_number_generator(segment):
    segment_list = segment_list_mapper[segment]
    cprint('Number of random number needed', 'yellow', attrs=['bold'], end=": ")
    size = integer_input('')
    cprint(f'Random numbers between range', 'yellow')
    cprint(f'Enter the range of numbers', 'white')
    start = integer_input('Starting integer')
    end = integer_input('Ending integer')
    for i in range(0, size):
        random_number = random.randint(start, end)
        segment_list.append(random_number)
    cprint(len(segment_list), 'red', attrs=['bold'], end="")
    print('', segment.lower() + "s read")


spl1 = "~!@#$%)(*&^}{';\":{}.></?|\\"; #supported special characters
def random_string(length):
    return ''.join(random.choices(string.ascii_letters+ spl1+string.digits, k=length))


def custom_strings(segment):
    segment_list = segment_list_mapper[segment]
    cprint('Number of custom strings needed', 'yellow', attrs=['bold'], end=": ")
    size = integer_input('')
    cprint('Enter the string Expression: ', 'yellow', end=": ")
    expression = input()
    for i in range(0, size):
        parsed_string = expression
        parsed_string = parsed_string.replace('%', random_string(random.randint(3, 5)))
        parsed_string = parsed_string.replace('?', random_string(1))
        segment_list.append(parsed_string)
    cprint(len(segment_list), 'red', attrs=['bold'], end="")
    print('', segment.lower() + "s read")


def default_months():
    for i in range(1, 13):
        months_list.append(i)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1



def csv_reader(segment):
    cprint('Enter the file name( please make sure file exist in src/input/)', 'white', attrs=['bold'], end=": ")
    input_file_name = input()
    f_p = f'./input/{input_file_name}.csv'
    if os.path.exists(f_p):
        rec = file_len(f_p)
        print(f'Found {rec} records in {f_p}\n Do you want to continue?')
        m.getch()
        cols = integer_input('Enter number of columns to map')
        input_csv_file = open(f_p,'r')
        for line in input_csv_file:
            line = line.split(',')
            for i in range(0,cols):
                segment_index_list[i].append(line[i])
        cprint(f'Successfully read first {cols} columns from {input_file_name}', 'white', 'on_green',end=" ")
        # print()
    else:
        csv_reader(segment)



def generic_segment_input(segment):
    cprint(f'\n{segment.upper()}', 'yellow', attrs=['bold'])
    cprint(f'Select Input Format for {segment}', "grey")
    option = 0
    cprint("OPTIONS:\n [1] Text file\n [2] Generate sequence\n [3] Range numbers\n [4] Custom spl strings\n [5] SKIP\n [6] CSV file(bulk)",
           'magenta')
    cprint('select SKIP if you have initialized the list', 'grey')
    option = chooseOption(6)
    if option == 1:
        file_reader(segment)
    elif option == 2:
        sequence_generator(segment)
    elif option == 3:
        random_number_generator(segment)
    elif option == 4:
        custom_strings(segment)
    elif option == 5:
        cprint(f'Default values for {segment}. found {len(segment_list_mapper[segment])}', 'white',
               'on_green')
    elif option == 6:
        csv_reader(segment)

    if option != 6:
        cprint(f'Successfully read the {segment} data', 'white', 'on_green')


def custom_trans_data():
    for seg in segment_list_mapper:
        generic_segment_input(seg)

    cprint('Input submitted successfully', 'blue', attrs=['bold'])
    for segl in segment_list_mapper:
        print(segl, len(segment_list_mapper[segl]))
    my_custom_script.custom_file(segment_list_mapper)
