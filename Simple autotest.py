from functions import salary, hello_who

assert hello_who('romas') == 'Hello, romas', 'Hello who Error'
assert hello_who('bot') == 'Hello, bot', 'Hello who Error'
assert hello_who('alenka') == 'Hello, alenka', 'Hello who Error'
assert salary(2,10) == 40
assert salary(5,30) == 300