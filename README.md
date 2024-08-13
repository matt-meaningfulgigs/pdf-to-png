# AI Studio PDF Resizer

This script, `ai_studio_pdf_resizer.py`, converts each page of a PDF into high-quality PNG images, resizes them if they exceed specified dimensions, and compresses them if their file size exceeds 10 megabytes. The images are saved in a directory named after the PDF file.

## How It Works

The script uses Ghostscript to convert the PDF pages into PNG images and then uses Pillow to resize and compress the images if needed. The maximum dimensions for each PNG image are set to 4800x4800 pixels, and the maximum file size is set to 10 megabytes.

The script will:

1. Take a PDF file as input.
2. Create a directory with the same name as the PDF file (excluding the `.pdf` extension).
3. Convert each page of the PDF into a PNG image using Ghostscript.
4. Resize each PNG image to ensure its dimensions do not exceed 4800x4800 pixels, maintaining the aspect ratio.
5. Compress each PNG image if its file size exceeds 10 megabytes, reducing the quality incrementally until it falls below the size threshold.
6. Save each resized and compressed PNG image in the created directory, with filenames like `page_001.png`, `page_002.png`, etc.

### Handling Large Images

- The script is configured to handle very large images by disabling Pillow's default protection against processing images with extremely large pixel dimensions. This is done by setting `Image.MAX_IMAGE_PIXELS = None` in the script.
- **Important**: While this change allows the script to handle large images, it may consume significant system resources (memory and CPU) when processing such files. Ensure your system has enough resources to handle the images you're working with.

### Detailed Code Explanation

- **Imports**: The script uses four modules:
  - `os`: For handling file and directory paths.
  - `subprocess`: For running Ghostscript as an external command.
  - `sys`: For accessing command-line arguments.
  - `PIL.Image`: From the Pillow library, used for resizing and compressing images.
  
- **Function `pdf_to_pngs(input_pdf_path, max_file_size_mb=10)`**:
  - Extracts the base name of the PDF file to name the output directory.
  - Creates the output directory if it doesn't exist.
  - Constructs a command to run Ghostscript, specifying the output format, resolution, and other necessary options.
  - Runs the Ghostscript command to convert the PDF pages to PNGs.
  - Uses Pillow to open each PNG image and resize it if necessary to fit within the 4800x4800 pixel limit.
  - Compresses the image if its file size exceeds 10 megabytes by reducing the image quality until it fits within the threshold.
  - Saves the resized and compressed images in the output directory.
  
- **Main Script Execution**:
  - Checks if the script was run with a PDF file as a command-line argument.
  - If not, it prints usage instructions and exits.
  - If a PDF file is provided, it calls the `pdf_to_pngs` function to perform the conversion, resizing, and compression.

## How to Use

1. **Ensure Ghostscript and Pillow are Installed**:
   - Run `gs --version` in your terminal to check if Ghostscript is installed.
   - If not, you can install it:
     - **Windows**: Download from the [official Ghostscript website](https://www.ghostscript.com/download/gsdnld.html).
     - **Mac**: Install via Homebrew with `brew install ghostscript`.
     - **Linux**: Install via your package manager, e.g., `sudo apt-get install ghostscript`.
   - Ensure Pillow is installed for image resizing and compression:
     ```bash
     pip install Pillow
     ```

2. **Save the Script**:
   - Save the provided code as `ai_studio_pdf_resizer.py` on your computer.

3. **Run the Script**:
   - Open a terminal and navigate to the directory where you saved the script.
   - Run the script by typing:
     ```bash
     python3 ai_studio_pdf_resizer.py /path/to/your/input.pdf
     ```
   - Replace `/path/to/your/input.pdf` with the path to the PDF file you want to convert.

4. **Output**:
   - The script will create a folder in the same directory as the PDF file, with the same name as the PDF (excluding the `.pdf` extension).
   - Inside this folder, you will find PNG images of each page of the PDF, resized to fit within 4800x4800 pixels and compressed to be under 10 megabytes if necessary.

## Example

If you have a PDF named `example.pdf` in your current directory, running:

```bash
python3 ai_studio_pdf_resizer.py example.pdf
