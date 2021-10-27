"""
Purpose: Dictionary that holds letters and the corresponding pictures urls. 
"""
from PIL import Image

letter_dictionary = {"a": "resources\letters\letterA.png", "b": "resources\letters\letterB.png", "c": "resources\letters\letterC.png",
                     "d": "resources\letters\letterD.png", "e": "resources\letters\letterE.png", "f": "resources\letters\letterF.png",
                     "g": "resources\letters\letterG.png", "h": "resources\letters\letterH.png", "i": "resources\letters\letterI.png",
                     "j": "resources\letters\letterJ.png", "k": "resources\letters\letterK.png", "l": "resources\letters\letterL.png",
                     "m": "resources\letters\letterM.png", "n": "resources\letters\letterN.png", "o": "resources\letters\letterO.png",
                     "p": "resources\letters\letterP.png", "q": "resources\letters\letterQ.png", "r": "resources\letters\letterR.png",
                     "s": "resources\letters\letterS.png", "t": "resources\letters\letterT.png", "u": "resources\letters\letterU.png",
                     "v": "resources\letters\letterV.png", "w": "resources\letters\letterW.png", "x": "resources\letters\letterX.png",
                     "y": "resources\letters\letterY.png", "z": "resources\letters\letterZ.png"}

im = Image.open(letter_dictionary["u"])
im.show()