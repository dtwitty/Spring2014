apps = [('A', 64, 1), ('B', 53, 9), ('C', 282, 8), ('D', 395, 5), ('E', 84, 6), ('F', 152, 4), ('G', 279, 3)]
def pareto_dominate(a, b):
    if a[1] >= b[1] and a[2] >= b[2]:
        return a[1] > b[1] or a[2] > b[2]
    else:
        return False

print pareto_dominate(apps[4], apps[0])
optimal = []
for app1 in apps:
    good = True
    for app2 in apps:
        if pareto_dominate(app2, app1):
            good = False
            break
    if good:
        optimal.append(app1[0])
print optimal