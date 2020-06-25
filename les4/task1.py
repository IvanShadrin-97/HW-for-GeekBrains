from sys import argv

_, work_hours, salary_per_hours = argv

bonus = 0
work_hours = int(work_hours)
salary_per_hours = int(salary_per_hours)
total_awards = work_hours * salary_per_hours

if work_hours >= 20:
    bonus = 1000
else:
    bonus = 0
total_awards += bonus

print('Ваше время работы:', work_hours)
print('Ствка в час: ', salary_per_hours)
print('Премия:', bonus)
print('Ваша итоговая зароботная плата:', total_awards)
