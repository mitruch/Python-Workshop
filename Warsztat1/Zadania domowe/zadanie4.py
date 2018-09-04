week = {
    1: 'Poniedziałek',
    2: 'Wtorek',
    3: 'Środa',
    4: 'Czwartek',
    5: 'Piątek',
    6: 'Sobota',
    7: 'Niedziela'
}
result = { v: k for k, v in week.items() if k%2 != 0 }

assert 'Poniedziałek' in result
print(result)