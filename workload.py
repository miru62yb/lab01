a=input('Введите название первого предмета:')
b=input('Введите количество занятий в неделю')
c=input('Введите длительность одного занятие в минутах')
e=input('Введите название второго предмета:')
f=input('Введите количество занятий в неделю')
g=input('Введите длительность одного занятие в минутах')
h=input('Введите доступное время на неделю в часах')
v=b*c
n=f*g
total_minut=v+n
total_hours=total_minut/60
free=h-total_hours
f_weeks_minut==total_minutes*4
f_weeks_hours=f_weeks_minut/60
print(a,v,'мин')
print(b,n,'мин')
print('Общая нагрузка в мин:'total minut:'В часах:'total_hours)
print('Общее доступное время в часах:'free)
print('Нагрузка за 4 недели в минутах:'f_weeks_minut'В часах'f_weeks_hours)
