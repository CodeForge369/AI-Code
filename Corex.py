import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser
import platform
import time

# --- Global TTS Initialization Flag and Engine ---
engine = None
tts_available = False

try:
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Setting up the voice properties
    voices = engine.getProperty('voices')

    # Set voice (Index 0 or 1 usually works well, depends on OS)
    if voices:
        engine.setProperty('voice', voices[0].id)  # Typically male voice

    engine.setProperty('rate', 170)  # Adjust speed for a professional feel
    tts_available = True

except Exception as e:
    # Handles cases where TTS drivers fail to load
    print(f"Error initializing TTS engine: {e}")
    print("Speech output is disabled. Using print statements only.")
    tts_available = False

# --- Core Speech Function ---
def speak(audio):
    """
    Converts text to speech if the engine is available,
    and always prints the output to the console.
    """
    print(f"COREX: {audio}")
    if tts_available and engine:
        try:
            engine.say(audio)
            engine.runAndWait()  # Blocks while processing queued commands
        except Exception as e:
            print(f"Error during speech execution: {e}")

# --- Helper Functions ---
def wishMe():
    """Wishes the user good morning, afternoon, or evening based on the time."""
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning Sujal. I hope you had a restful night.")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sujal. Ready for the next task.")
    else:
        speak("Good Evening Sujal. Systems operational and standing by.")
    speak("I am COREX. How may I assist you today?")

def takeCommand():
    """
    Takes microphone input from the user and returns the recognized string output.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        r.adjust_for_ambient_noise(source, duration=0.5)

        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except sr.UnknownValueError:
        print("COREX: Unrecognized command. Please try again.")
        return "none"
    except sr.RequestError:
        speak("I am currently unable to connect to the Google speech service. Please check your internet connection.")
        return "none"
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "none"

    return query.lower()

# --- Main Logic ---
def run_jarvis():
    """Main function containing the logic for processing commands."""
    wishMe()

    while True:
        query = takeCommand()

        if query == "none":
            continue  # Loop again if no clear command was recognized

        # --- Google Search Command ---
        if ('search google for' in query or 'search for' in query or 'google' in query) and 'open' not in query:
            search_query = query.replace('search google for', '').replace('search for', '').replace('google', '').strip()
            if search_query:
                speak(f"Understood. Searching Google for {search_query} now.")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            else:
                speak("I did not catch the search term. Please try again.")

        # --- Open Specific Websites ---
        elif 'open youtube' in query:
            speak("Opening YouTube in your default browser.")
            webbrowser.open("https://www.youtube.com")

        elif 'open website' in query or 'open browser' in query:
            speak("Opening your default web browser to Google.com.")
            webbrowser.open("https://www.google.com")

        # --- Check the Time ---
        elif 'what is the time' in query or 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the current time is {strTime}")

        # --- Opening local applications ---
        elif 'open' in query:
            app_to_open = query.replace("open", "").strip()
            os_name = platform.system()

            if app_to_open:
                speak(f"Affirmative. Launching {app_to_open} now.")

                app_paths = {
                    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
                    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
                    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    "viber": r"C:\Users\Sujal shrestha\AppData\Local\Viber\Viber.exe",
                    "desktop": r"C:\Users\Sujal shrestha\OneDrive\Desktop",
                    "discord":r"C:\Users\Sujal shrestha\AppData\Local\Discord\Update.exe --processStart Discord.exe",
                    "asphalt 9":r"start shell:AppsFolder\\A278AB0D.Asphalt9_46.1.1000.0_x64__h6adky7gbf63m"
                }

                try:
                    if os_name == "Windows":
                        if app_to_open.lower() in app_paths:
                            os.startfile(app_paths[app_to_open.lower()])
                        else:
                            os.startfile(app_to_open)  # Try raw command

                    elif os_name == "Darwin":  # macOS
                        if app_to_open.lower() == "calculator":
                            os.system("open -a Calculator")
                        else:
                            os.system(f'open -a "{app_to_open}"')

                    elif os_name == "Linux":
                        os.system(app_to_open)

                    else:
                        speak("I cannot execute this command on your current operating system.")

                except Exception as e:
                    speak(f"I encountered an error trying to launch {app_to_open}.")
                    print(f"Execution Error: {e}")

            else:
                speak("I need a specific app name like Notepad or Calculator. Please try again.")

        # --- Fallback / Unrecognized Command ---
        else:
            speak("I heard your command, but I don't have a protocol for that yet. Please stick to time, search, or application commands.")

        # --- Exit Command ---
        if 'exit' in query or 'stop listening' in query or 'goodbye' in query:
            speak("Goodbye Sir. All systems powered down. Have a productive day.")
            break

# --- Main Execution Block ---
if __name__ == "__main__":
    if tts_available or not engine:  # Run even if TTS fails, just without voice
        run_jarvis()
    else:
        print("\nFATAL ERROR: Jarvis cannot run because the Text-to-Speech engine failed to initialize completely.")
        print("Please check your pyttsx3 and system dependencies, such as the eSpeak library on Linux.")
