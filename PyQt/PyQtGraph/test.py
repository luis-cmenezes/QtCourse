SUPERIOR_LIMIT = 430
INFERIOR_LIMIT = 320
COLORS_DICT = {'above': (1,0,0,1), 'below': (0,0,1,0), 'normal': (0,1,0,1)}

acquisition = []
with open('PyQtGraph/retI-retV-rmsI-rmsV-heatInput-T.txt', 'r') as file:
    acq_lines = file.readlines()

for line in acq_lines:
    data = (line.split(' '))
    data = [float(n_data) for n_data in data]

    acquisition.append(data)

for index, row in enumerate(acquisition):

    current_data = row[4]
    if current_data > INFERIOR_LIMIT and current_data < SUPERIOR_LIMIT:
        acquisition[index] = COLORS_DICT['normal']
    elif current_data >= SUPERIOR_LIMIT:
        acquisition[index] = COLORS_DICT['above']      
    elif current_data <= INFERIOR_LIMIT:
        acquisition[index] = COLORS_DICT['below']
    else:
        print(f'Caso não encontrado para index {index}')

print(acquisition)