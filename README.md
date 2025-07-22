# Real-Time-Object-Tracker

## Project Overview

This project provides a real-time object tracking system using OpenCV’s CSRT and KCF trackers. A user can select an object in the first frame of a webcam stream, and the system will track it as it moves within the video feed.

<div align="center">
  <img width="800" height="598" alt="image" src="https://github.com/user-attachments/assets/1c5fe56b-9d88-42b4-805b-4bec9f641c39" />
</div>

## Features

- Live object tracking using webcam input.
- Supports CSRT and KCF tracking algorithms.
- Displays bounding box and real-time FPS on screen.
- Command-line switch to choose tracker type.

## Directory Structure

```
real-time-object-tracker/
├── requirements.txt
├── tracker.py
├── utils.py
├── README.md
├── demo.mp4
├── .gitignore
```
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ahmed-Mostafa-88/real-time-object-tracker.git
   cd real-time-object-tracker

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

To run the tracking system, use the following command:

    python tracker.py --tracker CSRT

To use the KCF tracker:

    python tracker.py --tracker KCF

## Controls

- Press S to select the object to track.
- Press Q to quit the application.

## Implementation Details

 - The tracker.py script initializes webcam video capture and waits for the user to press S to define a region of interest.
 - The selected tracker (CSRT or KCF) is initialized and updates the bounding box for each new frame.
 - The FPS is calculated using OpenCV’s TickMeter and displayed in real time.
 - The utils.py module contains a utility function create_tracker() to return the appropriate OpenCV tracker based on user input.

## Demo

A recorded demo of the tracking system is available in the repository as demo.mp4.

## Dependencies

- opencv-python
- imutils

Install them via the included requirements.txt.

## License

This project is licensed under the MIT License.
 
