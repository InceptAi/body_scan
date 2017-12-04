from myimports import *
from get_single_image import *
#----------------------------------------------------------------------------------
# convert_to_grayscale(img):           converts a ATI scan to grayscale
#
# infile:                              an aps file
#
# returns:                             an image
#----------------------------------------------------------------------------------
def convert_to_grayscale(img):
    # scale pixel values to grayscale
    base_range = np.amax(img) - np.amin(img)
    rescaled_range = 255 - 0
    img_rescaled = (((img - np.amin(img)) * rescaled_range) / base_range)

    return np.uint8(img_rescaled)

# unit test ------------------------------------------
#an_img = get_single_image(APS_FILE_NAME, 0)
#img_rescaled = convert_to_grayscale(an_img)

#fig, axarr = plt.subplots(nrows=1, ncols=2, figsize=(20, 5))

#axarr[0].imshow(img_rescaled, cmap=COLORMAP)
#plt.subplot(122)
#plt.hist(img_rescaled.flatten(), bins=256, color='c')
#plt.xlabel("Grayscale Pixel Value")
#plt.ylabel("Frequency")
#plt.show()
