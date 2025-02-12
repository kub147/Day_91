import fitz
import pyttsx3


def pdf_to_speech(pdf_path, rate=150, volume=1.0, voice_id=None):
    try:
        doc = fitz.open(pdf_path)
        text = ""

        for page in doc:
            text += page.get_text("text") + "\n"

        engine = pyttsx3.init()

        engine.setProperty("rate", rate)

        engine.setProperty("volume", volume)

        if voice_id:
            engine.setProperty("voice", voice_id)

        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")

    speech_rate = 125
    speech_volume = 0.9

    pdf_to_speech(pdf_path, rate=speech_rate, volume=speech_volume)
