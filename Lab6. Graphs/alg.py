def get_code(a, rect): 
    code = [0, 0, 0, 0] 
    if a[0] < rect[0]:
        code[0] = 1  
    if a[0] > rect[1]: 
        code[1] = 1 
    if a[1] < rect[2]:  
        code[2] = 1  
    if a[1] > rect[3]:  
        code[3] = 1  

    return code  

def log_prod(code1, code2):  # (9.6)
    p = 0  # (9.6.1)
    for i in range(4):  # (9.6.2)
        p += code1[i] & code2[i]  # (9.6.3)

    return p  # (9.6.4)

def is_visible(bar, rect): # (9)
    """Видимость - 0 = невидимый
                   1 = видимый
                   2 = частично видимый"""
    # вычисление кодов концевых точек отрезка
    s1 = sum(get_code(bar[0], rect)) # (9.1)
    s2 = sum(get_code(bar[1], rect)) # (9.2)

    # предположим, что отрезок частично видим
    vis = 2 # (9.3)

    # проверка полной видимости отрезка
    if not s1 and not s2: # (9.4)
        vis = 1 # (9.5)
    else:
        # проверка тривиальной невидимости отрезка
        l = log_prod(get_code(bar[0], rect), get_code(bar[1], rect)) # (9.6 == 9.6.4)
        if l != 0: # (9.7)
            vis = 0 # (9.8)

    return vis  # (9.9)


def cohen_sutherland(bar, rect): #9 (0)
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
        vis = is_visible(bar, rect) # (9 == 9.9)
        if vis == 1:  # (10)
            scene.addLine(bar[0][0], bar[0][1], bar[1][0], bar[1][1])  # (11)
            return  # (12)
        elif not vis:  # (13)
            return  # (14)

        # проверка пересечения отрезка и стороны окна
        code1 = get_code(bar[0], rect)  # (15)
        code2 = get_code(bar[1], rect)  # (16)

        if code1[i] == code2[i]:  # (17)
            continue  # (18)

        # проверка нахождения Р1 вне окна; если Р1 внутри окна, то Р2 и Р1 поменять местами
        if not code1[i]:  # (19)
            bar[0], bar[1] = bar[1], bar[0]  # (20)

        # поиск пересечений отрезка со сторонами окна
        # контроль вертикальности отрезка
        if flag != -1:  # (21)
            if i < 2:  # (22)
                bar[0][1] = t * (rect[i] - bar[0][0]) + bar[0][1]  # (23)
                bar[0][0] = rect[i]  # (24)
                continue  # (25)
            else:
                bar[0][0] = (1 / t) * (rect[i] - bar[0][1]) + bar[0][0]  # (26)

        bar[0][1] = rect[i]  # (27)
    scene.addLine(bar[0][0], bar[0][1], bar[1][0], bar[1][1]) # (28)
    
