# make sure ffmpeg-python installed
# make sure ffmpeg/bin is already set up inside the path variable

import os
path = os.getcwd()
input_path = os.path.join(path, 'videoplayback.mp4')
output_path = os.path.join(path, 'output.m3u8')

import ffmpeg
input_stream = ffmpeg.input(input_path, f='mp4')
output_stream = ffmpeg.output(input_stream, output_path, format='hls', start_number=0, hls_time=0, hls_list_size=0)
ffmpeg.run(output_stream)