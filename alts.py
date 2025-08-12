import keyboard
import sounddevice as sd
import numpy as np
import sys
import time
import requests

# ======= CONFIG =======
HOTKEY = "ctrl+esc"
USE_MIC = False  # On GCP VM, no real mic
API_URL = "http://localhost:8000/llm"  # Example endpoint for your LLM
# ======================

def record_audio():
    """Record from mic (if available)"""
    try:
        duration = 5  # seconds
        samplerate = 16000
        print("🎤 Listening...")
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
        sd.wait()
        return np.squeeze(audio)
    except Exception as e:
        print(f" Audio recording not available: {e}")
        return None

def send_to_llm(text):
    """Send text to LLM API and return the response."""
    # Replace with your LLM call
    payload = {"prompt": text}
    try:
        resp = requests.post(API_URL, json=payload)
        return resp.json().get("response", "(No response)")
    except Exception as e:
        return f" Failed to reach LLM API: {e}"

def main():
    print(f"🎤 Press {HOTKEY} to speak, or type your message below and press Enter:")

    while True:
        try:
            print(" Enter your query: ", end="")
            sys.stdout.flush()

            # Wait for hotkey or text input
            start_time = time.time()
            spoken_text = None

            if keyboard.is_pressed(HOTKEY):
                if USE_MIC:
                    audio_data = record_audio()
                    spoken_text = "(Speech recognized here)"  # Replace with actual STT
                else:
                    print("\n Microphone not available. Using typed input instead.")
            else:
                spoken_text = input().strip()

            if not spoken_text:
                continue

            print("\n THINKING...\n")
            # Simulate some LLM processing time
            time.sleep(1)

            response = send_to_llm(spoken_text)

            print(f" > Text splitted to sentences.")
            print(f"[{response}]")
            print(f" > Processing time: {time.time() - start_time}")
            print(f" > Real-time factor: {(time.time() - start_time)/1.0}")

        except KeyboardInterrupt:
            print("\n Exiting.")
            break

if __name__ == "__main__":
    main()
