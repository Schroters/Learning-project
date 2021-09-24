# Meltdown Mitigation
# https://exercism.org/tracks/python/exercises/meltdown-mitigation

def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000:
        return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    colors = ((voltage * current) / theoretical_max_power) * 100
    if 100 >= colors >= 80:
        return 'green'
    elif 79 >= colors >= 60:
        return 'orange'
    elif 59 >= colors >= 30:
        return 'red'
    elif 30 > colors:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if (temperature * neutrons_produced_per_second) < (threshold / 100 * 40):
        return 'LOW'
    elif(threshold * 0.9) <= (temperature * neutrons_produced_per_second) <= (threshold * 1.1):
        return 'NORMAL'
    else:
        return 'DANGER'


print(is_criticality_balanced(750, 600))
print(reactor_efficiency(200, 50, 15000))
print(fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000))     # DANGER
print(fail_safe(temperature=100, neutrons_produced_per_second=45, threshold=5000))      # NORMAL
print(fail_safe(temperature=100, neutrons_produced_per_second=50, threshold=5000))      # NORMAL
