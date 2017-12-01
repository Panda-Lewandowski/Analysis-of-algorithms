def cohen_sutherland(bar, rect, win):
    # инициализация флага
    flag = 1 # общего положения (1)
    t = 1 # (2)

    # проверка вертикальности и горизонтальности отрезка
    if bar[1][0] - bar[0][0] == 0: # (3)
        flag = -1   # вертикальный отрезок (4)
    else:
        # вычисление наклона
        t = (bar[1][1] - bar[0][1]) / (bar[1][0] - bar[0][0]) # (5)
        if t == 0: # (6) 
            flag = 0   # горизонтальный (7)

    # для каждой стороны окна
    for i in range(4): # (8)
        vis = is_visible(bar, rect) # (9)
        if vis == 1:  #
            scene.addLine(bar[0][0], bar[0][1], bar[1][0], bar[1][1])  # (10)
            return  # (11)
        elif not vis:  # (12)
            return  # (13)

        # проверка пересечения отрезка и стороны окна
        code1 = get_code(bar[0], rect)  # (14)
        code2 = get_code(bar[1], rect)  # (15)

        if code1[i] == code2[i]:  # (16)
            continue  # (17)

        # проверка нахождения Р1 вне окна; если Р1 внутри окна, то Р2 и Р1 поменять местами
        if not code1[i]:  # (18)
            bar[0], bar[1] = bar[1], bar[0]  # (19)

        # поиск пересечений отрезка со сторонами окна
        # контроль вертикальности отрезка
        if flag != -1:  # (20)
            if i < 2:  # (21)
                bar[0][1] = t * (rect[i] - bar[0][0]) + bar[0][1]  # (22)
                bar[0][0] = rect[i]  # (23)
                continue  # (24)
            else:
                bar[0][0] = (1 / t) * (rect[i] - bar[0][1]) + bar[0][0]  # (25)

        bar[0][1] = rect[i]  # (26)
    scene.addLine(bar[0][0], bar[0][1], bar[1][0], bar[1][1]) # (27)
