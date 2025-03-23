from gtts import gTTS
import os
import platform

def text_to_speech(text, lang="hi", filename="output.mp3"):
    """
    Converts text to speech in Hindi using gTTS.

    :param text: The text to be converted to speech.
    :param lang: Language code (default is 'hi' for Hindi).
    :param filename: Output filename (default 'output.mp3').
    :return: Path of the saved audio file.
    """
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(filename)
    return filename

if __name__ == "__main__":
    hindi_text = "टेस्ला ने एक नया इलेक्ट्रिक वाहन लॉन्च किया है। यह बाजार में क्रांति ला सकता है।"
    audio_file = text_to_speech(hindi_text)

    # Play audio based on OS
    system_name = platform.system()
    if system_name == "Windows":
        os.system(f"start {audio_file}")  # Windows
    elif system_name == "Darwin":
        os.system(f"afplay {audio_file}")  # macOS
    else:
        os.system(f"mpg321 {audio_file} &")  # Linux (Install mpg321 if needed)

