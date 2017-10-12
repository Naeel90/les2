studenten = {'Ahmad': 11.0, 'Giedo': 9.0, 'Abed': 10.5, 'niek': 12.0, 'mohammad': 8.0, 'Dj': 7.0, 'Nael': 4.5, 'Sudo': 3.0}
for student in studenten:
    if studenten[student] > 9:
        print('{:10}{}'.format(student,studenten[student]))