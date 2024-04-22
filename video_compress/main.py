# Importing the module
from moviepy.editor import *

# uploading the video we want to edit
video = VideoFileClip(r"C:\Users\PC\PROJECTS\comparativestudies\storage\app\public\XORIJ__TASSUROTLARI___2QISM__19_11_2023_LOGO.mp4")


# getting width and height of video 1
width_of_video1 = video.w
height_of_video1 = video.h

print("Width and Height of original video : ", end = " ")
print(str(width_of_video1) + " x ", str(height_of_video1))

print("#################################")

# compressing
video_resized = video.resize(0.2)

# getting width and height of video 2 which is resized
width_of_video2 = video_resized.w
height_of_video2 = video_resized.h

print("Width and Height of resized video : ", end = " ")
print(str(width_of_video2) + " x ", str(width_of_video2))

print("###################################")


# displaying final clip
# video_resized.ipython_display()

video_resized.h(r"C:\Users\PC\PROJECTS\comparativestudies\storage\app\public\XORIJ__TASSUROTLARI___2QISM__19_11_2023_LOGO1.mp4")