import os
import subprocess

# Select the ExifTool binary name here (if exiftool(-k).exe at the same directory)
EXIFTOOL_PATH = 'exiftool.exe'  # or 'exiftool(-k).exe'

current_dir = os.getcwd()

image_files = [f for f in os.listdir(current_dir) if f.lower().endswith(('.jpg', '.jpeg'))]

for image in image_files:
    print(f"Processing: {image}")
    
    # ExifTool command and settings.
    cmd = [
        EXIFTOOL_PATH,
        '-overwrite_original',
        '-XMP-GPano:UsePanoramaViewer=True',
        '-XMP-GPano:ProjectionType=equirectangular',
        '-XMP-GPano:CroppedAreaImageWidthPixels<ImageWidth',
        '-XMP-GPano:CroppedAreaImageHeightPixels<ImageHeight',
        '-XMP-GPano:FullPanoWidthPixels<ImageWidth',
        '-XMP-GPano:FullPanoHeightPixels<ImageHeight',
        '-XMP-GPano:CroppedAreaLeftPixels=0',
        '-XMP-GPano:CroppedAreaTopPixels=0',
        image
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Done.")
