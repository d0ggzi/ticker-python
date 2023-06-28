from moviepy.editor import *
import matplotlib.colors as mc

def ticker(message, duration=3, bg_color="black", text_color="white", screensize=(100, 100)):
    if not check_args(message, bg_color, text_color): return
    try:
        txtClip = TextClip(message, color=text_color, font="PT Mono",
                        kerning = -5, fontsize=80, bg_color=bg_color)
        speed = (len(message)-3)/duration * 30
        txtClip = txtClip.set_position(lambda t: (-speed*t, 0))
        bg_color = [el*255 for el in mc.to_rgb(bg_color)]
        cvc = CompositeVideoClip( [txtClip], size=screensize, bg_color=bg_color).set_duration(duration)

        cvc.write_videofile('res.avi',fps=25,codec='mpeg4')
        print("Успешно!")
    except Exception as e:
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
    message = input()
    ticker(message, 5, "black", "white")