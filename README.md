# Gym Routine Generator
A Flask web app that suggests workout routines and nutrition tips based on your fitness goals.

## Features
- TDEE Calculator by personal information
- Workout selection by body part
- Nutrition plans for slimming vs muscle gain
- Responsive design

## Installation
1. Clone the repository
```bash
git clone https://github.com/Cyanishere/Gym-routine-generator.git
cd Gym_project
```
2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the Flask app
```bash
flask run
```
or explicitly:
```bash
python gym.py
```
5. Open in browser
Visit http://127.0.0.1:5000/ or http://localhost:5000/

## Project Structure
```bash
Gym_project/
├── gym.ipynb
├── megaGymDataset.csv
├── gym.py
├── README.md
├── requirements.txt
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

