# Импортирование библиотеки компьютерного зрения, которая предназначена для анализа, классификации и обработки изображений
import cv2
# Импортирование модуля работы со временем
import time
# Запись в переменную ссылки на потоковый протокол реального времени ,записи с определенной камеры видеонаблюдения
src = 'rtsp://admin:@188.162.85.173:561/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream'
# создание объект VideoCapture, чтобы «захватывать» видео с камеры видеонаблюдения,которую мы указали в переменную src.
capture = cv2.VideoCapture(src)
# Определияем кодек
codec = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')

#Получаем ширину формата видео ,полученного из переменной capture,объекта VideoCapture
frame_width = int(capture.get(3))
#Получаем высоту формата видео ,полученного из переменной capture,объекта VideoCapture
frame_height = int(capture.get(4))

#Выводим в консоль ширину формата видео ,полученного из переменной capture,объекта VideoCapture
print('frame_width', frame_width)
#Выводим в консоль высоту формата видео ,полученного из переменной capture,объекта VideoCapture
print('frame_height', frame_height)
# Создаем обьект содержащий в себе Имя выходного файла будет первым аргументом. Затем нужно передать кодеку, количество кадров в
# секунду (fps) и размер кадра.
output_video = cv2.VideoWriter(
    'out.avi',
    codec,
    10.5,
    (frame_width, frame_height)
)

# записываем в переменную число секунд текущего времени.
t = time.time()
# Чтобы сохранить видео, нужно записать каждый кадр в цикле while.
while(True):

    ret, frame = capture.read()
    output_video.write(frame)
    # Если прошло больше 30 секунд,то остановить запись кадров
    if time.time() - t >30:
        break

# Уничтожить все окна записи с камер видеонаблюдения
cv2.destroyAllWindows()
