while True:
    one_word = input('Первое сообщение: ')
    one_word_list = list(one_word)

    one_word_count = one_word_list.count("!")
    one_word_count += one_word_list.count("?")

    two_word = input('Второе сообщение: ')
    two_word_list = list(two_word)

    two_word_count = two_word_list.count("!")
    two_word_count += two_word_list.count("?")

    if one_word_count > two_word_count:
        print(f'Третье сообщение: {one_word + two_word}')
    elif one_word_count < two_word_count:
        print(f'Третье сообщение: {two_word + one_word}')
    else:
        print("Третье сообщение: Ой")
