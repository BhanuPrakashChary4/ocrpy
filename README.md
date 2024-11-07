# Tesseract OCR Project

Tesseract OCR with Docker and Installation Script

A simple setup for using Tesseract OCR with options for Docker deployment or direct installation on a Linux system. This repository includes:

    Docker Support: Run Tesseract OCR in a Docker container without installation.
    Installation Script: A Bash script for installing Tesseract OCR directly on your system.
    Usage Examples: Instructions for running Tesseract on images to extract text.

## Prerequisites

- Docker (for running the Docker container)
- Bash (for running the installation script on Linux systems)

## Installation Options

### Option 1: Run Tesseract OCR in Docker

You can use Docker to run Tesseract OCR without needing to install it directly on your machine.

1. **Build the Docker Image**:
   ```bash
   docker build -t tesseract-ocr .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run --rm -v "$(pwd)":/usr/src/app tesseract-ocr <input_image> <output_file>
   ```
   - Replace `<input_image>` with the path to the image file you want to process.
   - Replace `<output_file>` with the desired output file name for the extracted text.

#### Dockerfile Example

Here's an example `Dockerfile` you can use:

```dockerfile
# Dockerfile for Tesseract OCR
FROM ubuntu:latest

# Install dependencies and Tesseract OCR
RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /usr/src/app

# Set entrypoint to Tesseract
ENTRYPOINT ["tesseract"]
```

### Option 2: Install Tesseract OCR with a Bash Script

If you prefer to install Tesseract directly on your system, use the provided Bash script.

1. **Run the Installation Script**:
   ```bash
   ./install_tesseract.sh
   ```

2. **Usage**:
   Once installed, you can use Tesseract directly from the command line:
   ```bash
   tesseract <input_image> <output_file>
   ```

### `install_tesseract.sh` Script

This script installs Tesseract OCR on a Linux system.

```bash
#!/bin/bash

# Update package list
echo "Updating package list..."
sudo apt-get update

# Install Tesseract OCR
echo "Installing Tesseract OCR..."
sudo apt-get install -y tesseract-ocr

# Verify installation
echo "Verifying Tesseract installation..."
tesseract --version

# Optional: Install additional language packs
# Uncomment the next line and specify languages if needed (e.g., "eng", "deu", etc.)
# sudo apt-get install -y tesseract-ocr-<langcode>

echo "Tesseract OCR installation completed."
```

### Additional Information

- **Language Packs**: Tesseract supports multiple languages. You can install additional language packs by modifying the script to include the desired language codes (e.g., `tesseract-ocr-eng` for English).
- **Troubleshooting**: If you encounter any issues with Docker, ensure Docker is correctly installed and configured. For script issues, make sure it has executable permissions: `chmod +x install_tesseract.sh`.

### License

This project is licensed under the MIT License.

