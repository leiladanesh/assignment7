from moviepy import editor

video = editor.VideoFileClip(' marzieh.mp4 ')
video.audio.write_audiofile(' marzieh .mp3')