#!/usr/bin/env python3
# Reference: https://pypi.org/project/qrcode/
"""
qr_generator.py

Generates a QR Code PNG for the Biox Systems homepage (https://www.bioxsystems.com/)
and saves it as biox_qr-code.png.

Usage:
    python qr_generator.py
"""

import qrcode

BIOX_URL = "https://www.bioxsystems.com/"       # URL for Biox Systems
OUTPUT_FILE = "biox_qr-code.png"                # Output file to save QR Code

def main():
    # Configure QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(BIOX_URL)
    qr.make(fit=True)

    # Render and save
    img = qr.make_image(fill_color="black", back_color="white")
    # Save QR Code to the output file mentioned above
    img.save(OUTPUT_FILE)

    print(f"[Biox Systems] QR Code for {BIOX_URL} saved as {OUTPUT_FILE}")

if __name__ == "__main__":
    main()