'''Layering and Combining Images'''
import nftmaker as nft

if __name__ == "__main__":
    collection_size=10
    json_output_filename = 'output/1json.json'
    """
    The List is each folder of traits, in order of how they should be layered.
    lists are pngs
    Backgrounds are gifs
    """
    backgrounds='data/bg/'
    music='music/'
    myList=[
    'data/lion/robe/',
    'data/lion/belts/',
    'data/lion/arms/',
    'data/lion/emblem/',
    'data/lion/accessory/',
    'data/lion/head/',
    'data/lion/head_headgear/',
    'data/lion/mouth/',
    'data/lion/eyes/'
    ]
    nft.createNFT(collection_size, myList,json_output_filename,backgrounds, music)
   


