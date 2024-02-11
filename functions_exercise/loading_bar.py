def loading_bar_status(number):
    loading_bar = ''
    is_loading_bar_full = True

    if 100 >= number >= 0 == number % 10:
        for i in range(1, 10 + 1):
            if i <= number // 10:
                loading_bar += '%'
            else:
                loading_bar += '.'
                is_loading_bar_full = False

    if is_loading_bar_full:
        print(f'100% Complete!\n[{loading_bar}]')
    else:
        print(f'{number}% [{loading_bar}]\nStill loading...')


num_input = int(input())
loading_bar_status(num_input)



