while True:
    start = input('Здраствуйте,'
                  ' я вам помогу вычислить среднюю температуру воздуха в КР, нажмите "Enter" чтобы продолжить.')
    region = input('Вы должны ввести среднюю температуру воздуха в каждой области.')

    chui = int(float(input('Введите среднюю температуру  воздуха в Чуйской области - ')))

    talas = int(float(input('Введите среднюю температуру воздуха в Таласской области - ')))

    issyk_Kul = int(float(input('Введите среднюю температуру воздуха в Иссык-кульской области - ')))

    narun = int(float(input('Введите среднюю температуру воздуха в Нарынской области - ')))

    jalal_abad = int(float(input('Введите среднюю температуру воздуха в Жалал-Абадской области - ')))

    osh = int(float(input('Введите среднюю температуру воздуха в Ошской области - ')))

    batken = int(float(input('Введите среднюю температуру воздуха в Баткенской области - ')))

    # print((chui + talas + issyk_Kul + narun + jalal_abad + osh + batken) / 7)

    sum_regions = ((chui + talas + issyk_Kul + narun + jalal_abad + osh + batken) / 7)

    sum_regions = round(sum_regions, 1)

    print(f"Средний показатель температуры воздуха по КР на сегодня {sum_regions} С")

    # это просто для закрепления:)

    if sum_regions >= 19 and sum_regions < 31:
        print("В КР прохладно, советуем одеться по теплее")

    elif sum_regions >= 32 and sum_regions < 50:
        print("В КР тепло, советуем одеться по легче")

    else:
        print("Одевайся по погоде")
