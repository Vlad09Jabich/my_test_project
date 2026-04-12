from random import randint


def calculate_efficiency(data_size, processing_time):
    # efficiency = data_size / processing_time
    # return efficiency
    return data_size / processing_time

def show_report(name, value):
    print(f'\n Отчёт для системы {name}: Эффективность {value} \n')

systems = ['AI Processing Unit',
           'Thermal Control System',
           'Information Transfer System'
            ]

efficiency = calculate_efficiency(randint(1, 1000), randint(1, 250))

show_report(systems[randint(0,2)], int(efficiency))