from moviepy.editor import *

def ticker(message, duration = 3, bg_color="black", text_color="white", screensize=(100, 100)):
    txtClip = TextClip(message, color=text_color, font="Amiri-Bold",
                    kerning = -5, fontsize=80, bg_color=bg_color)
    speed = 50 + len(message)*10
    txtClip = txtClip.set_position(lambda t: (-speed*t, 0)).set_duration(duration)
    cvc = CompositeVideoClip( [txtClip], size=screensize)

    cvc.write_videofile('res.avi',fps=25,codec='mpeg4')


if __name__ == "__main__":
    message = 'This is text for testing out my new function'
    ticker(message, 3, "gray", "chocolate")