import tkinter
import math


def branch(point, angle, length):
    # Условие выхода из рекурсии
    if (length < minLength): return

    # Вычислим и нормализуем углы на которые направлены новые ветки
    # Нормализовать угол, значит преобразовать его к промежутку от 0 до 360 градусов
    lb_angle = normalize(angle + angleBetween)
    rb_angle = normalize(angle - angleBetween)

    x, y = point[0], point[1]
    # Получим точки в которые нужно провести линии
    lb_point = getBranchEnding(x, y, lb_angle, length)
    rb_point = getBranchEnding(x, y, rb_angle, length)

    # Узнаем насколько близко длина новых веток к минимальной
    # и в соответствии с этим зададим толщину линий
    branch_width = 10 * ((length - minLength) / (startLength - minLength))
    can.create_line(x, y, lb_point[0], lb_point[1], width=branch_width, fill='black')
    can.create_line(x, y, rb_point[0], rb_point[1], width=branch_width, fill='black')

    # Рекурсивно генерируем следующие ветки
    branch(lb_point, lb_angle, length * lenFactor)
    branch(rb_point, rb_angle, length * lenFactor)


# Функция, возвращающая кортеж с координатами точки конца очередной ветки
def getBranchEnding(x, y, angle, length):
    return (
        x - (math.sin(math.radians(angle)) * length),
        y - (math.cos(math.radians(angle)) * length))


def normalize(angle):
    while (angle < 0):
        angle += 360
    while (angle >= 360):
        angle -= 360
    return angle

def delete_canvas():
    can.delete("all")


def Start_paint():

    global angleBetween, minLength, startLength, lenFactor
    angleBetween = int(entry_1.get())
    lenFactor = float(entry_2.get())
    startLength = int(entry_3.get())
    minLength = int(entry_4.get())


    root_x = width / 2
    root_y = height * 0.98
    x = root_x
    y = root_y - startLength
    can.create_line(root_x, root_y, x, y, fill='black', width=10)
    branch((x, y), 0, startLength * lenFactor)


#Создали окно и canvas для отрисовки дерева
window = tkinter.Tk()
width, height = 900, 600
can = tkinter.Canvas(window, width=width, height=height)
can.grid(row=0, column=1)

text_1 = tkinter.Label(text="Угол между ветками: ")
text_1.place(x=10, y=10)

text_2 = tkinter.Label(text="Множитель длины вложенных веток: (До 0.9)")
text_2.place(x=10, y=30)

text_3 = tkinter.Label(text="Начальная длина ветки: ")
text_3.place(x=10, y=50)

text_4 = tkinter.Label(text="Минимальная длина ветки: ")
text_4.place(x=10, y=70)

entry_1 = tkinter.Entry()
entry_1.place(x=270, y=10)

entry_2 = tkinter.Entry()
entry_2.place(x=270, y=30)

entry_3 = tkinter.Entry()
entry_3.place(x=270, y=50)

entry_4 = tkinter.Entry()
entry_4.place(x=270, y=70)

start_button = tkinter.Button(text="Отрисовать дерево", command=Start_paint)
start_button.place(x=10, y=90)

clean_button = tkinter.Button(text="Очистить экран", command=delete_canvas)
clean_button.place(x=10, y=120)

window.resizable(width=False, height=False) #Не дает пользователю изменить размер окна
window.mainloop()


