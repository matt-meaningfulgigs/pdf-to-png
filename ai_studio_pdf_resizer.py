import os  # For handling file and directory paths
import subprocess  # For running Ghostscript as an external command
import sys  # For accessing command-line arguments

def resize_pdf(input_pdf_path, max_dimensions=(3600, 3600), resolution=72):
    # Extract the base name of the PDF file (without the extension)
    base_name = os.path.splitext(os.path.basename(input_pdf_path))[0]
    
    # Create the output path for the resized PDF
    output_pdf_path = os.path.join(os.path.dirname(input_pdf_path), f"{base_name}_resized.pdf")

    # Construct the Ghostscript command to resize the PDF, set the DPI, and apply screen settings
    gs_command = [
        "gs",
        "-sDEVICE=pdfwrite",  # Use the pdfwrite device to output a PDF
        "-dCompatibilityLevel=1.4",  # Set PDF version compatibility
        "-dPDFSETTINGS=/screen",  # Use screen settings for lower quality and smaller size
        "-dNOPAUSE",  # Do not pause between pages
        "-dBATCH",  # Process all pages and exit
        "-dFIXEDMEDIA",  # Forces the content to fit within the specified media size
        "-dPDFFitPage",  # Scales the page content to fit the specified size
        f"-dDEVICEWIDTHPOINTS={max_dimensions[0]}",  # Set the maximum width in points
        f"-dDEVICEHEIGHTPOINTS={max_dimensions[1]}",  # Set the maximum height in points
        f"-r{resolution}",  # Set the resolution (DPI) for the output PDF
        f"-sOutputFile={output_pdf_path}",  # Specify the output file path
        input_pdf_path  # The path to the input PDF file
    ]

    # Run the Ghostscript command
    subprocess.run(gs_command, check=True)

    print(f"Resized PDF saved at {output_pdf_path}")

if __name__ == "__main__":
    # Check if the user provided a PDF file as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python3 ai_studio_pdf_resizer.py <input_pdf_path>")
        sys.exit(1)

    # Get the PDF file path from the command-line arguments
    input_pdf_path = sys.argv[1]

    # Resize the PDF
    resize_pdf(input_pdf_path)
