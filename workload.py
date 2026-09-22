#TODO первый предмет
name_1=input('Введите название первого предмета.')
total_1=int(input('Введите количество занятий по этому предмету.'))
time_1=int(input('Введите продолжительность занятие в минутах.'))
#TODO второй предмет
name_2=input('Введите название второго предмета.')
total_2=int(input('Введите количество занятий по этому предмету.'))
time_2=int(input('Введите продолжительность занятие в минутах.'))
#TODO свободное время
free=int(input('Введите доступное время на неделю в часах (не меньше суммарной нагрузки)'))
#todo нагрузка по предметам
time_total_1=total_1*time_1
time_total_2=total_2*time_2
#todo общая нагрузка
total_load_min=time_total_1+time_total_2
total_load_hrs=total_load_min/60
#todo остаток свободного времени
free_remainde=free-total_load_hrs
#todo 4 недели
total_load_4_weeks_min=total_load_min*4
total_load_4_weeks_hrs=total_load_hrs*4
print(f'Время на предмет {name_1}; {time_total_1}')
print(f'Время на предмет {name_2}; {time_total_2}')
print(f'Общая нагрузка в минутах: {total_load_min}')
print(f'Общая нагрузка в часах: {total_load_hrs}')
print(f'Остаток свободного времени: {free_remainde}')
print(f'Нагрузка за 4 недели в минутах: {total_load_4_weeks_min}')
print(f'Нагрузка за 4 недели в часах: {total_load_4_weeks_hrs}')