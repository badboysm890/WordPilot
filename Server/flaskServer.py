from __future__ import unicode_literals
from flask import Flask, request
from flask_cors import CORS
import whisper
from pydub import AudioSegment
import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer
import torch
import os
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable
import urllib
import pymongo

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
models = T5ForConditionalGeneration.from_pretrained("Michau/t5-base-en-generate-headline")
tokenizer = T5Tokenizer.from_pretrained("Michau/t5-base-en-generate-headline")
models = models.to(device)
model = whisper.load_model("base")
client = pymongo.MongoClient("")
db = client.WordPiloted
print(db.list_collection_names())

client = pymongo.MongoClient("<>")
db = client.test
print(db.list_collection_names())

app = Flask(__name__)
CORS(app)

def audioToText(audio):
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    options = whisper.DecodingOptions(fp16 = False)
    result = whisper.decode(model, mel, options)
    return result.text

def youtubeToAudioSegments(url):
      if os.path.exists("audio.mp3"):
       os.remove("audio.mp3")
      os.system("youtube-dl "+"--write-thumbnail "+"--skip-download "+url + " -o logo")
      os.system("yt-dlp -f 140 -o audio.mp3 " + url)
      while not os.path.exists("audio.mp3"):
          continue
      
      if os.path.exists("segments"):
          os.system("rm -rf segments")
      
      audio = AudioSegment.from_file("audio.mp3")
      segment_length = 50 * 1000
      
      if not os.path.exists("segments"):
          os.makedirs("segments")
      
      for i, segment in enumerate(audio[::segment_length]):
          segment.export(f"segments/{i}.mp3", format="mp3")


def generateHeadLine(text):
    ext =  "headline: " + text
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
    return results


@app.route("/getData", methods=["GET", "POST"])
def helloWorld():
 url = request.args.get('url')
 video_id = ""
 try:
  video_id = url.split("=")[1]
 except:
  video_id = url.split("/")[-1] 
  
#  find the video duration and store it in a variable
 duration = os.popen("youtube-dl --get-duration " + url).read().strip()
#  get video title
 title = os.popen("youtube-dl --get-title " + url).read().strip()
 print(duration, title)
 dataForWeb = {}
 dataToStore = {}
 dataToStore["duration"] = str(duration)
 dataToStore["title"] = str(title)

 if  video_id not in db.list_collection_names():
   youtubeToAudioSegments(url) 
   for i  in range(len(os.listdir("segments"))):
      orginal_text = audioToText("segments/"+str(i)+".mp3")
     
      dataForWeb[i] = {
           "heading" : generateHeadLine(orginal_text),
           "text" :  orginal_text
       }
    #   headings.append(dataForWeb[i]["heading"])

      try:
       db[video_id].insert_one(dataForWeb[i])
      except: 
         print("Error in inserting data in database")
 else:
        j = 0
        for i in db[video_id].find({}, {"_id":0}):
            dataForWeb[j] = {
                "heading" : i["heading"],
                "text" : i["text"]
            }
            j += 1
 # loop through the dataForWeb and remove _id
 for  i in range(len(dataForWeb)):
    dataForWeb[i].pop("_id", None)
 dataToStore["data"] = dataForWeb
 return dataToStore
 
     
     
 

if __name__ == "__main__":
    app.run(debug=True)