# Google-Image-Downloader

## Overview

It aims to develop a machine learning model that accurately predicts the orientation of a human face as "Right," "Left," or "Front." This project utilizes advanced computer vision techniques and deep learning algorithms to analyze facial features and determine their positions using Landing.ai website.

## Features

Predict the position of a human face (Right, Left, Front).
Utilize a pre-trained deep learning model for enhanced accuracy.

## Project Overview
The pipeline executes the following tasks:

Download Images: Downloads images from the internet based on a given keyword.
Convert to Grayscale: Converts the downloaded images to grayscale.
Resize Images: Scales images by a specified percentage.
Compress Files: Archives the processed images into a ZIP file.
Send Email: Emails the ZIP file as an attachment to a specified recipient.

## Files in the Project
download.py: Downloads images based on a search keyword.
grayscaleconvert.py: Converts images to grayscale.
scale.py: Resizes images based on a specified percentage.
zip.py: Compresses processed images into a ZIP file.
sendEmail.py: Sends the ZIP file to an email recipient.
pipeline.py: Runs the entire image processing pipeline.
main.py: Simplifies the pipeline with predefined parameters.

## Individual Script Execution
Each step can be executed independently:

Download Images:
python download.py <max_num> <keyword> <output_folder>
Convert to Grayscale:
python grayscaleconvert.py <input_folder> <output_folder>
Resize Images:
python scale.py <input_folder> <output_folder> <scale_percent>
Compress Files:
python zip.py <input_folder> <zip_file_name>
Send Email:
python sendEmail.py <zip_file_path> <recipient_email>

## License
This project is licensed under the MIT License.
