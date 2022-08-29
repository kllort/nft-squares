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
    backgrounds='data/bgs/'
    music='data/music/'
    eagle=[
    'data/eagle/1-skins/',
    'data/eagle/3-eyes/',
    'data/eagle/2-beaks/',
    'data/eagle/4-headgear/',
    'data/weapons/R/'
    ]

    panda=[
    'data/panda/1-skins/',
    'data/panda/2-eyes/',
    'data/panda/3-snouts/',
    'data/panda/4-headgear/',
    'weapons/combo/'
    ]

    tiger=[
    'data/tiger/1-skins/',
    'data/tiger/2-eyes/',
    'data/tiger/3-snout/',
    'data/tiger/4-headgear/',
    'weapons/combo/'
    ]

    monke=[
    'data/monke/1-skins/',
    'data/monke/2-eyes/',
    'data/monke/3-mouth/',
    'data/monke/4-headgear/',
    'weapons/combo/'
    ]

    #nft.createNFT(collection_size, eagle,json_output_filename,backgrounds, music)
    nft.create_my_NFT(collection_size, eagle,json_output_filename,backgrounds)


