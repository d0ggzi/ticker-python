from moviepy.editor import *

def ticker(message, duration=3, bg_color="black", text_color="white", screensize=(100, 100)):
    if not check_args(message, bg_color, text_color): return
    try:
        txtClip = TextClip(message, color=text_color, font="Amiri-Bold",
                        kerning = -5, fontsize=80, bg_color=bg_color)
        speed = 50 + len(message)*10
        txtClip = txtClip.set_position(lambda t: (-speed*t, 0)).set_duration(duration)
        cvc = CompositeVideoClip( [txtClip], size=screensize)

        cvc.write_videofile('res.avi',fps=25,codec='mpeg4')
        print("Успешно!")
    except:
        print("Произошла ошибка. Проверьте правильно ли Вы указали параметры.")


def check_args(message, bg_color, text_color):
    if len(message) > 300:
        print("Введите сообщение поменьше")
        return False
    colors = [el.decode("utf-8") for el in TextClip.list('color')]
    if bg_color not in colors or text_color not in colors:
        print("Некорректные цвета")
        return False
    return True

if __name__ == "__main__":
    message = 'This is text'
    ticker(message, 3, "black", "chocolate")