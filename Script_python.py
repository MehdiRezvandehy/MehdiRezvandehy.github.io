from PIL import Image
import os

def resize_images(input_folder, output_folder, target_width, target_height):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if the file is an image (you may want to add more checks based on your use case)
        if os.path.isfile(input_path) and filename.lower().endswith(('.png')):
            output_path = os.path.join(output_folder, filename)

            # Open the image
            with Image.open(input_path) as img:
                # Resize the image
                resized_img = img.resize((target_width, target_height))

                # Save the resized image
                resized_img.save(output_path, format=img.format)

if __name__ == "__main__":
    input_folder = "./images"
    output_folder = "./images/fixed_size"
    target_width = 900  # Adjust to your desired width
    target_height = 600  # Adjust to your desired height

    resize_images(input_folder, output_folder, target_width, target_height)
