import random
import os, os.path
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import json
from moviepy.editor import AudioFileClip, ImageClip
import ffmpeg

def create_my_NFT(collection_size, myList,json_output,background):
    i=1
    output=[]
    while i < collection_size+1:
        myPNG, thisNFT= makePNG(myList,i)
        paste_png_on_mp4(background,myPNG,i)
        output.append(thisNFT)
        i=i+1
        
    
    json_object = json.dumps(output, indent=4)
    with open(json_output,'w') as f:
        f.write(json_object)
        f.close




def createNFT_222(collection_size, myList,json_output,background,music):
    """each layer should be organized into a folder.
        then list out the layer folders in z order in the mylist variable
        then configure and create the art in assemble.nfts.py
    """
    i=1
    output=[]
    while i < collection_size+1:
        thisNFT = {}

        ''' add a method to map backgrounds to specific beats'''

        x=0 
        while x<len(myList):
            trait = myList[x]
            llist=os.listdir(trait)
            lweights = create_weights(llist)
            choice = pick1(llist,lweights)
            if x==0:
                bg=Image.open(trait+choice[0])
            else:
                L1=Image.open(trait+choice[0])
                thisNFT[trait]=choice[0]
                bg.paste(L1,(0,0),L1)
            x+=1
            image_path = 'output/output'+str(i)+'.png'
            
            
            bg_mp4, bg_i=add_mp4(background,)
        thisNFT[background]=bg_i[0]
        bg.save(image_path,quality=100)
        bg = Image.open(image_path)
        bg = bg.resize((1000,1000))
        bg = add_text(bg, thisNFT)
        bg.save(image_path,quality=100)
        add_static_image_to_audio(image_path, audio_path, output_path)
        os.remove(image_path)
        output.append(thisNFT)
        print(i)
        i+=1
    json_object = json.dumps(output, indent=4)
    with open(json_output,'w') as f:
        f.write(json_object)
        f.close

def makePNG(myList,i):
    """each layer should be organized into a folder.
        then list out the layer folders in z order in the mylist variable
        then configure and create the art in assemble.nfts.py
    """
    x=0 
    thisNFT = {}

    trait = myList[x]
    llist=os.listdir(trait)
    lweights = create_weights(llist)
    choice = pick1(llist,lweights)
    bg=Image.open(trait+choice[0])
    thisNFT[trait]=choice[0]
    
    while x<len(myList):
        trait = myList[x]
        llist=os.listdir(trait)
        lweights = create_weights(llist)
        choice = pick1(llist,lweights)
        L1=Image.open(trait+choice[0])
        thisNFT[trait]=choice[0]
        bg.paste(L1,(0,0),L1)
        x+=1
    image_path = 'output/output'+str(i)+'.png'
    bg.save(image_path,quality=100)
    return image_path, thisNFT


def createNFT(collection_size, myList,json_output,background,music):
    """each layer should be organized into a folder.
        then list out the layer folders in z order in the mylist variable
        then configure and create the art in assemble.nfts.py
    """
    i=1
    output=[]
    while i < collection_size+1:
        thisNFT = {}

        ''' add a method to map backgrounds to specific beats'''
        bg, bg_i=add_background(background)
        thisNFT[background]=bg_i[0]
        x=0 
        while x<len(myList):
            trait = myList[x]
            llist=os.listdir(trait)
            lweights = create_weights(llist)
            choice = pick1(llist,lweights)
            L1=Image.open(trait+choice[0])
            thisNFT[trait]=choice[0]
            bg.paste(L1,(0,0),L1)
            x+=1
            image_path = 'output/output'+str(i)+'.png'
            
            
            llist=os.listdir(music)
            lweights = create_weights(llist)
            choice = pick1(llist,lweights)
            audio_path = music + choice[0]
            thisNFT[music]=choice[0]
            output_path = 'output/output'+str(i)+'.mp4'
        bg.save(image_path,quality=100)
        bg = Image.open(image_path)
        bg = bg.resize((1000,1000))
        bg = add_text(bg, thisNFT)
        bg.save(image_path,quality=100)
        add_static_image_to_audio(image_path, audio_path, output_path)
        os.remove(image_path)
        output.append(thisNFT)
        print(i)
        i+=1
    json_object = json.dumps(output, indent=4)
    with open(json_output,'w') as f:
        f.write(json_object)
        f.close

def create_weights(llist):
    ilength=len(llist)
    lweights=[]
    x=1
    while x<ilength+1:
        lweights.append(100000//x)
        x=x+1
    print(lweights)
    return lweights
def pick1(llist,lweights):
    myPick=random.choices(llist,lweights,k=1)
    return myPick



def add_static_image_to_audio(image_path, audio_path, output_path):
    """Create and save a video file to `output_path` after 
    combining a static image that is located in `image_path` 
    with an audio file in `audio_path`"""
    # create the audio clip object
    audio_clip = AudioFileClip(audio_path)
    # create the image clip object
    image_clip = ImageClip(image_path)
    # use set_audio method from image clip to combine the audio with the image
    video_clip = image_clip.set_audio(audio_clip)
    # specify the duration of the new clip to be the duration of the audio clip
    video_clip.duration = audio_clip.duration
    # set the FPS to 1
    video_clip.fps = 1
    # write the resuling video clip
    video_clip.write_videofile(output_path)

def add_text(bg, thisNFT):
    I1 =ImageDraw.Draw(bg)
    # Custom font style and font size

 
    # Add Text to an image
    I1.text((10, 10), str(thisNFT).replace(",","\n"), fill =(255, 255, 255))
    return bg

def add_background(background):
        llist= os.listdir(background)
        lweights = create_weights(llist)
        bg_i = pick1(llist,lweights)
        bg = Image.open(background+bg_i[0]).convert('RGB')
        return  bg, bg_i

def paste_png_on_mp4(background,myPNG,i):
    llist= os.listdir(background)
    lweights = create_weights(llist)
    output_path = 'output/output'+str(i)+'.mp4'
    bg_i = pick1(llist,lweights)
    

    (
    ffmpeg 
    .filter([ffmpeg.input(background + bg_i[0]),ffmpeg.input(myPNG)],'overlay',10,10)
    .output(output_path)
    .run()
    )

    