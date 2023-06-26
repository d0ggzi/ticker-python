from moviepy.editor import *

screensize = (100,100)
message = 'Cool effect so what if it does not fit and now i gonna say also and also'
txtClip = TextClip(message, color='white', font="Amiri-Bold",
                   kerning = 5, fontsize=80)
speed = 80 + len(message)*13
txtClip = txtClip.set_position(lambda t: (-speed*t, 0)).set_duration(3)
cvc = CompositeVideoClip( [txtClip], size=screensize)


cvc.write_videofile('wtf.avi',fps=25,codec='mpeg4')
# print(TextClip.list('color'))