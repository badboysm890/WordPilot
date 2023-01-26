from __future__ import unicode_literals
import whisper
from pydub import AudioSegment
import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer
import torch
import os
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable
import urllib
import platform


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
models = T5ForConditionalGeneration.from_pretrained("Michau/t5-base-en-generate-headline")
tokenizer = T5Tokenizer.from_pretrained("Michau/t5-base-en-generate-headline")
models = models.to(device)
model = whisper.load_model("base")

url = "https://youtu.be/Aa83vRghue4"

# http://img.youtube.com/vi/<insert-youtube-video-id-here>/maxresdefault.jpg

# delete the audio file if it exists
if os.path.exists("audio.mp3"):
    os.remove("audio.mp3")

# download the youtube video logo and save it as logo.png
os.system("youtube-dl "+"--write-thumbnail "+"--skip-download "+url + " -o logo.png")
os.system("yt-dlp -f 140 -o audio.mp3 " + url)

# download the youtube video logo and save it as logo.png 

# wait until the audio file is downloaded
while not os.path.exists("audio.mp3"):
    continue



 if os.path.exists("segments"):
    if platform.system() == "Windows":
        # remove entire segments folder
        os.system("rd /s /q segments")
    else:
        os.system("rm -rf segments")

audio = AudioSegment.from_file("audio.mp3")
segment_length = 30 * 1000

if not os.path.exists("segments"):
    os.makedirs("segments")

for i, segment in enumerate(audio[::segment_length]):
    segment.export(f"segments/{i}.mp3", format="mp3")

orginal_text = ""
audio_list = os.listdir("segments")
headings = []
orginal_texts = []
dataForWeb = {
    
}

for i  in range(len(audio_list)):
   audio = whisper.load_audio(f"segments/{i}.mp3")
   audio = whisper.pad_or_trim(audio)
   mel = whisper.log_mel_spectrogram(audio).to(model.device)
   _, probs = model.detect_language(mel)
   options = whisper.DecodingOptions(fp16 = False)
   result = whisper.decode(model, mel, options)
   

#    building the headline
   text =  "headline: " + result.text
   max_len = 256
   encoding = tokenizer.encode_plus(text, return_tensors = "pt")
   input_ids = encoding["input_ids"].to(device)
   attention_masks = encoding["attention_mask"].to(device)
   beam_outputs = models.generate(
       input_ids = input_ids,
       attention_mask = attention_masks,
       max_length = 64,
       num_beams = 3,
       early_stopping = True,
   )
   results = tokenizer.decode(beam_outputs[0])
   headings.append(results) 
   dataForWeb[i] = {
        "heading" : results,
        "text" : result.text
    }
   
   orginal_text += "\n"
   orginal_text += "<h3>"+results + "</h3>"
   # new line
   orginal_text += "\n"
   orginal_text += "<p>"+result.text+ "</p>"

with open("text.txt", "w") as f:
    f.write(orginal_text)


