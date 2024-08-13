import os  # For handling file and directory paths
import subprocess  # For running Ghostscript as an external command
import sys  # For accessing command-line arguments
from PIL import Image  # For image processing, resizing, and compression

# Increase the maximum allowed image size (in pixels) to avoid DecompressionBombError
Image.MAX_IMAGE_PIXELS = None

def pdf_to_pngs(input_pdf_path, max_file_size_mb=10):
    # Extract the base name of the PDF file (without the extension)
    base_name = os.path.splitext(os.path.basename(input_pdf_path))[0]
    
    # Create a directory with the same name as the PDF file to store the PNG images
    output_dir = os.path.join(os.path.dirname(input_pdf_path), base_name)
    
    # If the output directory doesn't exist, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Construct the Ghostscript command to convert PDF to PNG
    gs_command = [
        "gs",
        "-dBATCH",  # Process all pages and exit
        "-dNOPAUSE",  # Do not pause between pages
        "-sDEVICE=png16m",  # Use png16m to avoid transparency
        f"-sOutputFile={output_dir}/page_%03d.png",  # Output file pattern
        "-r300",  # Set the resolution to 300 DPI for high quality
        input_pdf_path  # The path to the input PDF file
    ]

    # Run the Ghostscript command
    subprocess.run(gs_command, check=True)

    # Now resize and compress the images if they exceed the max dimensions or file size
    max_dimensions = (4800, 4800)
    max_file_size_bytes = max_file_size_mb * 1024 * 1024
    
    for filename in os.listdir(output_dir):
        if filename.endswith(".png"):
            file_path = os.path.join(output_dir, filename)
            
            # Open the image using Pillow
            with Image.open(file_path) as img:
                # Convert the image to RGB mode to avoid transparency
                img = img.convert("RGB")

                # Check if the image needs to be resized
                if img.width > max_dimensions[0] or img.height > max_dimensions[1]:
                    # Maintain the aspect ratio while resizing
                    img.thumbnail(max_dimensions, Image.LANCZOS)
                    img.save(file_path, "PNG")
                    print(f"Resized and saved {file_path}")

                # Check if the image needs to be compressed
                file_size = os.path.getsize(file_path)
                if file_size > max_file_size_bytes:
                    # Reduce quality incrementally until the file size is under the threshold
                    quality = 95  # Start with high quality
                    while file_size > max_file_size_bytes and quality > 10:
                        img.save(file_path, "PNG", quality=quality)
                        file_size = os.path.getsize(file_path)
                        quality -= 5  # Decrease quality by 5% each time
                    print(f"Compressed and saved {file_path}, final size: {file_size / (1024 * 1024):.2f} MB")

    print(f"All PNG files are saved, resized, and compressed in {output_dir}")

if __name__ == "__main__":
    # Check if the user provided a PDF file as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python3 ai_studio_pdf_resizer.py <input_pdf_path>")
        sys.exit(1)

    # Get the PDF file path from the command-line arguments
    input_pdf_path = sys.argv[1]

    # Convert the PDF to PNGs
    pdf_to_pngs(input_pdf_path)
