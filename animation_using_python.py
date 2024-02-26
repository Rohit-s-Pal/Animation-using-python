import imageio
import cv2
def convert_video_to_animation(video_path, output_path='output_animation.gif'):
    # Read the video frames
    vid = imageio.get_reader(video_path, 'ffmpeg')
    frames = [cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) for frame in vid]

    # Create animation
    imageio.mimsave(output_path, frames, fps=24)

# Example usage
# video_path = 'input_video.mp4'
# output_path = 'output_animation.gif'
# convert_video_to_animation(video_path, output_path)

# # Example usage
video_path = 'C:\Rohit Python\\track4.mp4'

output_path = 'C:\Rohit Python\\track100.mp4'
convert_video_to_animation(video_path, output_path)
