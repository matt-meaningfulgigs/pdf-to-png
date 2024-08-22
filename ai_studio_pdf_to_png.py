import os
import subprocess
import sys
from PIL import Image

# Disable the decompression bomb check (be cautious with this in production)
Image.MAX_IMAGE_PIXELS = None

def resize_if_needed(img):
    """Resize the image if it exceeds the maximum pixel limit."""
    max_pixels = 178956970
    if img.size[0] * img.size[1] > max_pixels:
        scaling_factor = (max_pixels / (img.size[0] * img.size[1])) ** 0.5
        new_size = (int(img.size[0] * scaling_factor), int(img.size[1] * scaling_factor))
        img = img.resize(new_size, Image.LANCZOS)  # Use LANCZOS for high-quality downscaling
        print(f"Image resized to {new_size} to fit within pixel limit.")
    return img

def pdf_to_png(input_pdf_path, output_folder='output_images', resolution=1200):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Command to convert PDF to PNG using Ghostscript with higher resolution
    gs_command = [
        "gs",
        "-dNOPAUSE",
        "-dBATCH",
        "-sDEVICE=pngalpha",  # Use pngalpha to retain transparency
        f"-r{resolution}",  # Increase the resolution (quadruple the original 300 DPI to 1200 DPI)
        "-sOutputFile={}/page_%03d.png".format(output_folder),
        input_pdf_path
    ]
    
    # Run the command
    subprocess.run(gs_command, check=True)
    
    # Collect all image paths and fill transparent backgrounds with white
    image_paths = sorted([os.path.join(output_folder, f) for f in os.listdir(output_folder) if f.endswith('.png')])
    
    for image_path in image_paths:
        img = Image.open(image_path).convert("RGBA")
        img = resize_if_needed(img)  # Resize the image if it's too large
        # Create a white background
        white_bg = Image.new("RGBA", img.size, "WHITE")
        # Composite the image onto the white background
        white_bg.paste(img, (0, 0), img)
        # Convert back to RGB and save
        white_bg.convert("RGB").save(image_path, "PNG")
    
    return image_paths

def png_to_pdf(image_paths, output_pdf_path):
    if not image_paths:
        print("No valid images to process into PDF.")
        return

    # Open the first image to create the base PDF
    first_image = Image.open(image_paths[0])
    image_list = [Image.open(img).convert("RGB") for img in image_paths[1:]]
    
    # Save the images as a PDF
    first_image.save(output_pdf_path, save_all=True, append_images=image_list)
    print(f"Flattened PDF saved as {output_pdf_path}")

if __name__ == "__main__":
    # Check if the user provided a PDF file as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python3 script_name.py <input_pdf_path>")
        sys.exit(1)
    
    # Get the PDF file path from the command-line arguments
    input_pdf_path = sys.argv[1]
    
    # Generate the output file name based on the original file name
    base_name = os.path.splitext(os.path.basename(input_pdf_path))[0]
    output_pdf_path = os.path.join(os.path.dirname(input_pdf_path), f"{base_name}_squashed.pdf")
    
    # Step 1: Convert PDF to PNG images using Ghostscript and fill with white background
    image_paths = pdf_to_png(input_pdf_path)
    
    # Step 2: Combine PNG images into a new PDF using Pillow
    png_to_pdf(image_paths, output_pdf_path)
