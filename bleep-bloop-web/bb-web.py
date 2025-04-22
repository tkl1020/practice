from flask import Flask, send_file
import numpy as np
from scipy.io.wavfile import write
import random
import io

app = Flask(__name__)

# Parameters
sample_rate = 44100  # Standard audio sample rate
max_duration = 0.06   # Maximum duration for each bleep/bloop (in seconds)
bleep_frequency_range = (2000, 6000)  # Range for bleep frequency (in Hz)
bloop_frequency_range = (75, 600)   # Range for bloop frequency (in Hz)

def generate_bleep(duration):
    """Generates a bleep sound using a square wave."""
    frequency = random.randint(bleep_frequency_range[0], bleep_frequency_range[1])
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    bleep_wave = np.sign(np.sin(2 * np.pi * frequency * t))  # Square wave (sharp, bleepy sound)
    bleep_wave = np.int16(bleep_wave * 32767)  # Scale to 16-bit PCM
    return bleep_wave

def generate_bloop(duration):
    """Generates a bloop sound using a sine wave."""
    frequency = random.randint(bloop_frequency_range[0], bloop_frequency_range[1])
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    bloop_wave = np.sin(2 * np.pi * frequency * t)  # Sine wave (smoother, bloopy sound)
    bloop_wave = np.int16(bloop_wave * 32767)  # Scale to 16-bit PCM
    return bloop_wave

def generate_random_bleeps_and_bloops(num_sounds):
    """Generates a series of random bleeps and bloops and returns it as a byte stream."""
    all_sounds = []
    for _ in range(num_sounds):
        # Randomly choose between a bleep or a bloop
        sound_type = random.choice(['bleep', 'bloop'])
        duration = random.uniform(0.1, max_duration)  # Random duration between 0.1s and max_duration
        
        if sound_type == 'bleep':
            sound = generate_bleep(duration)
        else:
            sound = generate_bloop(duration)
        
        all_sounds.append(sound)
    
    # Combine all sounds into one array
    final_audio = np.concatenate(all_sounds)
    
    # Save to a byte buffer (in-memory WAV file)
    byte_io = io.BytesIO()
    write(byte_io, sample_rate, final_audio)
    byte_io.seek(0)  # Rewind the buffer to the beginning
    
    return byte_io

# Endpoint for generating random bleeps and bloops and returning the WAV file
@app.route('/generate', methods=['GET'])
def generate():
    # Generate the random bleeps and bloops and return as a downloadable file
    bleep_bloop_file = generate_random_bleeps_and_bloops(100)  # Generate 100 sounds
    return send_file(
        bleep_bloop_file,
        mimetype='audio/wav',
        as_attachment=True,
        download_name='random_bleeps_bloops.wav'
    )

# Home route to display a simple button
@app.route('/')
def home():
    return '''
        <html>
            <head>
                <style>
                    body {
                        text-align: center;
                        margin-top: 100px;
                        font-family: Arial, sans-serif;
                    }
                    button {
                        background-color: #4CAF50;
                        color: white;
                        border: none;
                        padding: 20px 40px;
                        font-size: 20px;
                        cursor: pointer;
                        border-radius: 10px;
                        transition: background-color 0.3s;
                    }
                    button:hover {
                        background-color: #45a049;
                    }
                </style>
            </head>
            <body>
                <h1>Random Bleep & Bloop Generator</h1>
                <p>Click the button below to generate random bleeps and bloops!</p>
                <a href="/generate">
                    <button>Generate Sounds</button>
                </a>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)