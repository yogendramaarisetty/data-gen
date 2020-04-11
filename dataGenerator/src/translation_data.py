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
businesscenter_list = ['plan71']
productline_list = ['plan101']
geography_list = ['code_107']  # ,plan71,plan101,Code_107,Code_341,
icsegment_list = ['code341']
fiscalyears_list = [2013]
months_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
amounts_list = [1000]
segment_index_list = ['', accounts_list,
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
        segment_list.append(str(preceding_string + i))
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


def random_string(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


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


def generic_segment_input(segment):
    cprint(f'\n{segment.upper()}', 'yellow', attrs=['bold'])
    cprint(f'Select Input Format for {segment}', "grey")
    option = 0
    cprint("OPTIONS:\n [1] Text file\n [2] Generate sequence\n [3] Random numbers\n [4] Custom strings\n [5] SKIP",
           'magenta')
    cprint('select SKIP if you have initialized the list', 'grey')
    option = chooseOption(5)
    if option == 1:
        file_reader(segment)
    elif option == 2:
        sequence_generator(segment)
    elif option == 3:
        random_number_generator(segment)
    elif option == 4:
        custom_strings(segment)
    elif option == 5:
        cprint(f'Skipped {segment}.', 'white',
               'on_green')
    cprint(f'Successfully read the {segment} data', 'white', 'on_green')


def custom_trans_data():
    for seg in segment_list_mapper:
        generic_segment_input(seg)

    cprint('Input submitted successfully', 'blue', attrs=['bold'])
    for segl in segment_list_mapper:
        print(segl, len(segment_list_mapper[segl]))
    my_custom_script.custom_file(segment_list_mapper)
