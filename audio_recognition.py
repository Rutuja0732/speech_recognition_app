import speech_recognition as sr

def recognize_speech_from_file(audio_file_path):
    """
    Recognizes speech from an audio file using Google Speech Recognition.

    Parameters:
    audio_file_path (str): The path to the audio file.

    Returns:
    str: The transcription result or an error message.
    """
    recognizer = sr.Recognizer()

    # Use the audio file as the audio source
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio = recognizer.record(source)  # Read the entire audio file

        # Recognize speech using Google Speech Recognition
        try:
            transcription = recognizer.recognize_google(audio)
            return transcription
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

    except Exception as e:
        return f"An error occurred while processing the audio file: {e}"

# Test the function
if __name__ == "__main__":
    # Prompt the user to enter the path to their audio file
    AUDIO_FILE = input("Please enter the path to your audio file (e.g., C:/path/to/your/audio.wav): ")
    
    result = recognize_speech_from_file(AUDIO_FILE)
    
    # Print the result
    print(f"Google Speech Recognition: {result}")