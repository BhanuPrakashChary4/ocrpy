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
