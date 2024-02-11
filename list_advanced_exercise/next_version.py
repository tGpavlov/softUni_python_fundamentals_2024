software_version = [int(digit) for digit in input().split('.')]
software_version[-1] += 1
for index in range(len(software_version) - 1, 0, -1):
    if software_version[index] > 9:
        software_version[index] = 0
        software_version[index - 1] += 1

print('.'.join(str(digit) for digit in software_version))
