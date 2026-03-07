import random
when=['A Year ago', 'Yesterday', 'Last night', 'A long time ago', 'Few months ago']
name=['Samju', 'Teja', 'Usha', 'Bhanu', 'Pratyusha']
residence=['Hyderabad', 'Rajahmundry', 'Banglore', 'Chennai', 'Vizag']
placed=['Infosys', 'Accenture', 'Cognizant', 'Capgemini', 'Deloitte', 'Tcs']
print(random.choice(when) + ', ' + random.choice(name) + ', '  + 'placed in ' + random.choice(placed) + ' at ' + random.choice(residence))