"""
Essentially going to get it to try and understand images.
Create a way of encoding rgb values into a range of 0-1
Then encode images into this custom format
Then create a similarity calculator which iterates through all the rgb values of pixels in an image and returns a similarity score
Then create a tree loader. Need to be able to save a network using a set of text files and then be able to load them back up to keep a trained netwokr going
For each image, set the number of input/output nodes to the number of pixels and have the hidden layers always be of bigger size
Then see if you can get the network, trained like evolution on trying to balance weights to produce a higher similarity values of images of  x
Then keep training it! Might take a while but eventually it'd be interesting to see if it can produce pictures that look vaguely like x

LAST THING I DID:
Finished the basic substructure of the network, created an encoder/decoder of images to the float format

NEXT THING TO DO:
^ refer to list above
"""