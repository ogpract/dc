# client code:
clocks = {'P1': 0, 'P2': 0, 'P3': 0}
num_events = 10
output = {'P1': [], 'P2': [], 'P3': []}

for i in range(num_events):
    clocks['P1'] += 6
    if i == 8:
        clocks['P1'] = 70
    output['P1'].append(clocks['P1'] if i != 7 else "")
    
    clocks['P2'] += 8
    if i == 6:
        clocks['P2'] = 61
    output['P2'].append(clocks['P2'] if i != 5 else "")
    
    clocks['P3'] += 10
    output['P3'].append(clocks['P3'] if i != 6 else "")

print("Initial Logical Clock")
print(" Process P1  Process P2  Process P3")
for i in range(11):
    print(f"{str(6*i):>10}{str(8*i):>12}{str(10*i):>12}")

print("\nUpdated Logical Clock")
print(" Process P1  Process P2  Process P3")
for i in range(num_events):
    p1_val = output['P1'][i] if output['P1'][i] != "" else ""
    p2_val = output['P2'][i] if output['P2'][i] != "" else ""
    p3_val = output['P3'][i] if output['P3'][i] != "" else ""
    print(f"{str(p1_val):>10}{str(p2_val):>12}{str(p3_val):>12}")
