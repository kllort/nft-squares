import random
import os, os.path
from PIL import Image


def createNFT(collection_size):
    """each layer should be organized into a folder.
        then list out the layer folders in z order in the mylist variable
        then configure and create the art in assemble.nfts.py
    """
    myList=[
    'data/lion/robe/',
    'data/lion/belts/',
    'data/lion/arms/',
    'data/lion/head/',
    'data/lion/head_headgear/',
    'data/lion/mouth/',
    'data/lion/eyes/',
    'data/lion/accessory/',
    'data/lion/emblem/',
    ]
    i=1
    while i < collection_size+1:
        bg='data/bg/'
        bg = Image.open(bg+random.choice(os.listdir(bg))).convert('RGB')
        x=0 
        while x<len(myList):
            L1=random.choice(os.listdir(myList[x]))
            L1=Image.open(myList[x]+L1)
            bg.paste(L1,(0,0),L1)
            x+=1
        bg.save('output/output'+str(i)+'.png')
        print(i)
        i+=1

def dirLength(DIR):

    # path joining version for other paths
    print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

if __name__ == "__main__":
    createNFT(1)
