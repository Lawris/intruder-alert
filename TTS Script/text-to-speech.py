from playsound import playsound
import os
from google.cloud import speech


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'id.json'


def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Neural2-E",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        effects_profile_id=["medium-bluetooth-speaker-class-device"],
        pitch=-0.4,
        speaking_rate=0.89,
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )


    # The response's audio_content is binary.
    with open("output.wav", "wb") as out:
        out.write(response.audio_content)
        playsound('output.wav')




def main():
    text = "Chemical compond ready."
    synthesize_text(text)




if __name__ == "__main__":
    main()