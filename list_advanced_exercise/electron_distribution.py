def electron_distribution(electron):
    fulled_shells = []
    shell_count = 1

    while electron:
        max_electron_held_in_shell = 2 * shell_count ** 2
        if max_electron_held_in_shell >= electron:
            fulled_shells.append(electron)
            break
        fulled_shells.append(max_electron_held_in_shell)
        electron -= max_electron_held_in_shell
        shell_count += 1

    return fulled_shells


electrons = int(input())
result = electron_distribution(electrons)
print(result)
