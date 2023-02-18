
# Alexa, Intruder alert

Code from the *Alexa, Intruder Alert* TikTok https://www.tiktok.com/@plassonade/video/7198620329860730118

## Text to Speech script usage

Install the requiered dependencies with `pip3`

```bash
  pip3 install playsound google-cloud-speech google-cloud-texttospeech
```

The script is using the Google TTS AI library to generate an audio file for a given text input. The access to their API isn't free but they give you $300 free credits or a 90-day trial, which is more than enough to do what we're doing here.

You can test it out here: https://cloud.google.com/text-to-speech

Follow this tutorial until *Step 5* to create your Google Service Account key: https://medium.com/dataman-in-ai/create-your-first-text-to-speech-natural-voices-f71f8f7b5168

Copy your Google Service Account key into the same directory as the Python script and rename it `id.json`.

Type anything you want on the variable `text` at the end of the file.

Run the script with this command:

```bash
    python3 text-to-speech.py
```

The script will send the text to Google's API, create an `output.wav` file and play it.
## Audio files

If you don't feel like using Google's API, feel free to use the audio files provided on this GitHub.
I created them using Google's API and are the ones I used on the TikTok.

## Home Assistant automation script

`automation.yaml` is the raw automation file I wrote for the TikTok.

On Home Assistant you can go:
Settings > Automations & Scenes > Create Automation > Start with an empty automation

Click on the three dots and then Edit in YAML.

Paste the content of the script here and adapt it to your needs.




## Support

Join our Discord channel, The Smart Playground: https://discord.gg/tdPBusY7tt

