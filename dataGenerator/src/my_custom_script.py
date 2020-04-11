import os
from termcolor import cprint
import msvcrt as msv

def custom_file(segment_mapper):
    acc = segment_mapper['account']
    comp = segment_mapper['company']
    dep = segment_mapper['department']
    cs = segment_mapper['costcenter']
    rec = 1
    cprint(f'Total generated records are{rec}.\nDo you want to continue?')
    msv.getch()
    cprint('Enter the Result file name to generate:', 'white', attrs=['bold'], end=" ")
    file_name = input()
    cwd = os.getcwd()
    output_file = open(os.path.join(cwd, f'output/{file_name}.csv'), 'a+')
    cprint('Please wait! It may take some time...', 'magenta', attrs=['bold'])
    for i in range(0,30454):
        for bc in segment_mapper['businesscenter']:
            for pl in segment_mapper['productline']:
                for g in segment_mapper['geography']:
                    for ic in segment_mapper['icsegment']:
                        for fy in segment_mapper['fiscalyear']:
                            for m in segment_mapper['month']:
                                for a in segment_mapper['amount']:
                                    s = f'{acc[i]},{comp[i]},{dep[i]},{cs[i]},{bc},{pl},{g},{ic},{fy},{m},{a}\n'
                                    output_file.write(s)
    output_file.close()




def range_file(segment_mapper):
    for i in range(0,):
        a=1

def special_file(segmen):
    a=1
