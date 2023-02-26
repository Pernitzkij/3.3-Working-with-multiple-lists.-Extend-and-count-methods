def pacs_input():
    bit_list = []
    for i in range(1, 5):
        bit = int(input(f'{i} бит '))
        bit_list.append(bit)

    if bit_list.count(-1) <= 1:

        return bit_list

    else:
        print("Много ошибок в пакете.")
        return ()


while True:
    pacs_count = int(input('Кол-во пакетов: '))
    list_pacs = []
    for i_pacs in range(1, pacs_count + 1):
        print(f'Пакет номер {i_pacs}')
        list_pacs.extend(pacs_input())

    print(f'Полученное сообщение: {list_pacs}')
    errors = list_pacs.count(-1)
    print(f'Кол-во ошибок в сообщении: {errors}')
    print(f'Кол-во потерянных пакетов: {pacs_count - (len(list_pacs)//4) }')
