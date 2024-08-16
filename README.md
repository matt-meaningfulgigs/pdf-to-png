# AI Studio PDF Resizer

This repository contains two scripts for handling PDFs: one converts PDF pages to PNG images and the other resizes PDFs while keeping them in PDF format.

## Scripts Overview

### 1. `ai_studio_pdf_to_png.py`

This script converts each page of a PDF into high-quality PNG images, resizes them if they exceed specified dimensions, and compresses them if their file size exceeds 10 megabytes. The images are saved in a directory named after the PDF file.

#### How It Works

The script uses Ghostscript to convert the PDF pages into PNG images and then uses Pillow to resize and compress the images if needed. The maximum dimensions for each PNG image are set to 3600x3600 pixels, and the maximum file size is set to 10 megabytes.

The script will:

1. Take a PDF file as input.
2. Create a directory with the same name as the PDF file (excluding the `.pdf` extension).
3. Convert each page of the PDF into a PNG image using Ghostscript.
4. Resize each PNG image to ensure its dimensions do not exceed 3600x3600 pixels, maintaining the aspect ratio.
5. Compress each PNG image if its file size exceeds 10 megabytes, reducing the quality incrementally until it meets the file size requirement.

### 2. `ai_studio_pdf_resizer.py`

This script resizes a PDF by adjusting its page dimensions and DPI, keeping the output as a PDF. It ensures the PDF pages are no larger than 3600x3600 pixels and allows you to set the DPI to control the quality and file size.

#### How It Works

The script uses Ghostscript to resize the content of the PDF to fit within the specified page dimensions, with a default DPI of 150. It also applies the `/screen` PDF setting to reduce the overall file size, making it suitable for on-screen viewing.

The script will:

1. Take a PDF file as input.
2. Resize each page of the PDF to fit within 3600x3600 pixels.
3. Adjust the DPI to 150 (or another value specified by the user) to control the output quality.
4. Save the resized PDF as a new file with `_resized` appended to the original file name.

## Installation Instructions

### Prerequisites

Before running the scripts, you need to install Ghostscript and Python with the Pillow library. Follow the instructions below for your operating system.

### Windows Installation

1. **Open Command Prompt**:
   - Press `Windows + R`, type `cmd`, and press `Enter`.

2. **Install Ghostscript**:
   - Visit the Ghostscript download page: [Ghostscript Downloads](https://www.ghostscript.com/download/gsdnld.html).
   - Download the appropriate installer for your system (usually the latest 64-bit version).
   - Run the installer and follow the instructions.
   - During installation, ensure you select the option to "Add installation path to the system PATH" if available.

3. **Install Python**:
   - Visit the Python download page: [Python Downloads](https://www.python.org/downloads/).
   - Download the latest Python installer for Windows.
   - Run the installer and check the box that says "Add Python to PATH" before clicking "Install Now".

4. **Install Pillow**:
   - Open Command Prompt (if not already open) and type the following command:
     ```sh
     pip install Pillow
     ```

5. **Verify Installation**:
   - To check that everything is installed correctly, run the following commands in the Command Prompt:
     ```sh
     python --version
     gswin64c --version
     pip show Pillow
     ```

   - You should see the Python version, Ghostscript version, and details about the Pillow package.

### Mac Installation

1. **Open Terminal**:
   - Press `Command + Space`, type `Terminal`, and press `Enter`.

2. **Install Homebrew** (if not already installed):
   - Homebrew is a package manager for macOS. Install it by running the following command in Terminal:
     ```sh
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

3. **Install Ghostscript**:
   - Once Homebrew is installed, run the following command to install Ghostscript:
     ```sh
     brew install ghostscript
     ```

4. **Install Python**:
   - If you don’t have Python installed, you can install it using Homebrew:
     ```sh
     brew install python
     ```

5. **Install Pillow**:
   - With Python installed, you can now install Pillow using pip:
     ```sh
     pip install Pillow
     ```

6. **Verify Installation**:
   - To ensure everything is installed correctly, run the following commands in Terminal:
     ```sh
     python3 --version
     gs --version
     pip show Pillow
     ```

   - You should see the Python version, Ghostscript version, and details about the Pillow package.

## Usage

### For `ai_studio_pdf_to_png.py`

To convert a PDF to PNGs, use the following command:

```sh
python ai_studio_pdf_to_png.py <input_pdf_path>
```

### For ai_studio_pdf_resizer.py

To resize a PDF, use the following command:

``` sh
python ai_studio_pdf_resizer.py <input_pdf_path>
```
