# ALTS-GCPVM
alts (stt and tts) code and its working on the Google cloud VM

### Installation Steps on GCP VM
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv -y
sudo apt install ffmpeg -y

### Create Python virtual environment
python3 -m venv alts_env
source alts_env/bin/activate

### Install Python dependencies
pip install --upgrade pip
pip install keyboard sounddevice numpy requests  (sounddevice is for mic input will fail gracefully on GCP VM).
pip install openai

### Create the project file
cat > alts.py



###### Drawbacks
Drawbacks of No Physical Audio on GCP VM
No microphone access -> speech input won’t work.
You must type your queries instead.
No speaker/audio output -> TTS output can still be generated as an audio file, but you can’t hear it in real time unless you download it to your local machine.
Keyboard hotkey detection works in most VM terminals, but some GCP browser consoles may block certain key combos.
Higher latency if LLM API is remote.

Need to work on the drawbacks for better outcome.
