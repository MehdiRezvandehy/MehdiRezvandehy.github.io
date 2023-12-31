from PIL import Image, ImageSequence
import os

def resize_gif(input_path, output_path, target_width, target_height, resampling_filter=Image.ANTIALIAS):
    with Image.open(input_path) as img:
        # Create a list to hold resized frames
        resized_frames = []

        # Resize each frame
        for frame in ImageSequence.Iterator(img):
            resized_frame = frame.resize((target_width, target_height), resample=resampling_filter)
            resized_frames.append(resized_frame)

        # Save the resized frames as a new animated GIF
        resized_frames[0].save(
            output_path,
            save_all=True,
            append_images=resized_frames[1:],
            duration=img.info['duration'],
            loop=img.info['loop']
        )

if __name__ == "__main__":
    input_path = "./images/8.gif"
    output_path = "./images/fixed_size/8.gif"
    target_width = 900  # Adjust to your desired width
    target_height = 600  # Adjust to your desired height
    resampling_filter = Image.LANCZOS  # Experiment with different filters (ANTIALIAS, BICUBIC, LANCZOS, etc.)

    resize_gif(input_path, output_path, target_width, target_height)
