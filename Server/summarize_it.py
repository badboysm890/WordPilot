from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch
# measure inference time
import time
import threading
import time

def background_task(eta):
    start_time = time.time()
    while True:
        time_left = eta - (time.time() - start_time)
        if time_left > 0:
            print(f'Time left: {time_left:.2f} seconds')
        else:
            break
        time.sleep(1)
        # clear_output
        print("\033c", end="")


model_id = "stabilityai/stable-diffusion-2-1"

# faster inference image size 256

pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_attention_slicing()
pipe = pipe.to("mps")

prompt = "Loss of Control of Your Dog's Bladder, realistic, cartoon, vector, illustration, isolated on white background"
start = time.time()

start = time.time()

eta = 125 # ETA in seconds
t = threading.Thread(target=background_task, args=(eta,))
t.daemon = True
t.start()
image = pipe(prompt).images[0]
end = time.time()

print(f"Time taken: {end - start}")
    
image.save("image.png")
t.join()


import os
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable

# headless = True
webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))

image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))
#add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]

# remove <pad> and </s> from headings
headings = [x.replace("<pad>","").replace("</s>","") for x in headings]

search_keys= headings
number_of_images = 2
headless = False
#min_resolution = (width,height)
min_resolution=(0,0)
#max_resolution = (width,height)
max_resolution=(1920,1080)
for search_key in search_keys:
    image_scraper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
    image_urls = image_scraper.find_image_urls()
    image_scraper.save_images(image_urls,False)
