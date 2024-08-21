# Flask Video Record
A simple Flask web application that captures video from your webcam, saves it in MP4 format, and plays it back after stopping. This project demonstrates the integration of OpenCV with Flask to create a video recording and playback system.

## Features
Video Capture: Capture video from your webcam using OpenCV.
Video Recording: Save the recorded video in MP4 format.
Video Playback: Play the recorded video after stopping the recording, with a delay of 20 seconds.
Web Interface: A simple web interface to start and stop video recording, and view the recorded video.
## Requirements
Python 3.x
Flask
OpenCV (cv2)
## Installation
#### 1. Clone the Repository:
```git clone https://github.com/rock12231/Flask-Video-Record.git```
```cd Flask-Video-Record```
#### 2. Create a Virtual Environment: 
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
#### 3. Install Dependencies:
```pip install -r requirements.txt```

## Usage
#### 1. Run the Flask Application:
```python app.py```
#### 2. Access the Application:

Open your web browser and go to http://127.0.0.1:5000/.

#### 3. Start and Stop Recording:

- Click "Start Recording" to begin recording video.
- Click "Stop Recording" to stop the recording. After a 20-second delay, the recorded video will be played back.


##### Project Structure
```
Flask-Video-Record/
├── app.py              # Main Flask application file
├── templates/
│   ├── index.html      # HTML template for the main page
│   └── play_video.html # HTML template for video playback
├── static/
│   └── output.mp4      # Recorded video file (auto-generated)
├── venv/               # Virtual environment directory
└── requirements.txt    # Python dependencies file

```
## How It Works
- Recording Video: The application uses OpenCV to capture video frames from your webcam. These frames are encoded and saved as an MP4 file using the cv2.VideoWriter class.

- Serving Video: Once recording is stopped, the Flask server waits for 20 seconds and then serves the recorded video file using the play_video.html template.


## Contributing
Feel free to submit issues or pull requests. Contributions are welcome!

## Contact
For any inquiries or suggestions, please contact [Rock](https://github.com/rock12231).