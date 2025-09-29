# Gym Routine Suggestor
A Flask web app that suggests workout routines and nutrition tips based on your fitness goals.

## Features
- TDEE Calculator by personal information
- Workout selection by body part
- Nutrition plans for slimming vs muscle gain
- Responsive design

## Installation
```bash
git clone https://github.com/Cyanishere/Gym-routine-generator.git
cd Gym_project
pip install -r requirements.txt
flask run
```
run this with terminal
```bash
cd Gym_project
python3 gym.py
```

## Usage
Open http://127.0.0.1:5000/ in your browser(You can also use http://localhost:5000/), input your personal information
Select your workout mode, and get the suggested diet and routine

## Project Structure
```bash
Gym_project/
├── gym.ipynb
├── megaGymDataset.csv
├── gym.py
├── templates/
│   ├── gym_input.html
│   ├── TDEE.html
│   └── routine.html
└── static/
    └── images/
        └── routine_background_image.jpeg
```
## License
MIT License © 2025 Jasper Hang

