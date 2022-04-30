import random
import os, os.path
from PIL import Image
import json

def createNFT(collection_size, myList,json_output,background):
    """each layer should be organized into a folder.
        then list out the layer folders in z order in the mylist variable
        then configure and create the art in assemble.nfts.py
    """
    i=1
    output=[]
    while i < collection_size+1:
        thisNFT = {}
        llist= os.listdir(background)
        lweights = create_weights(llist)
        bg_i = pick1(llist,lweights)
        bg = Image.open(background+bg_i[0]).convert('RGB')
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
        bg.save('output/output'+str(i)+'.png')
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
        lweights.append(100//x)
        x=x+1
    return lweights
def pick1(llist,lweights):
    myPick=random.choices(llist,lweights,k=1)
    return myPick