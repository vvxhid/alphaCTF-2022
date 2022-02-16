from moviepy import *

from moviepy.editor import *

flag = 'AlphaCTF{W3VV1LLN3V3RF0R93T900D0LDD4Y5}'
morse = ".-- ...-- ...- ...- .---- .-.. .-.. -. ...-- ...- ...-- .-. ..-. ----- .-. ----. ...-- - ----. ----- ----- -.. ----- .-.. -.. -.. ....- -.-- ....."

spack = VideoFileClip("spack spack.mov.mp4")
stack = VideoFileClip("Stack stack.mov.mp4")
ilFautTrepondi = VideoFileClip("il faut trepondi.mov.mp4")

# final_clip = concatenate_videoclips([clip, clip2, clip3, clip4])
clips = []
for i in morse:
    if i == ".":
        clips.append(spack) # . as spack
    elif i == '-':
        clips.append(stack) # - as stack
    elif i == ' ':
        clips.append(ilFautTrepondi) # space between chars as ilFautTrepondi

final_clip = concatenate_videoclips(clips)

final_clip.write_videofile("final.mp4")
