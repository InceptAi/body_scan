from myimports import *
from read_file import read_data
#----------------------------------------------------------------------------------
# get_single_image(infile, nth_image):  returns the nth image from the image stack
#
# infile:                              an aps file
#
# returns:                             an image
#----------------------------------------------------------------------------------

def get_single_image(infile, nth_image):

    # read in the aps file, it comes in as shape(512, 620, 16)
    img = read_data(infile)
    
    # transpose so that the slice is the first dimension shape(16, 620, 512)
    img = img.transpose()
    
    return np.flipud(img[nth_image])

  

# unit test ---------------------------------------------------------------
#an_img = get_single_image(APS_FILE_NAME, 0)

#fig, axarr = plt.subplots(nrows=1, ncols=2, figsize=(20, 5))

#axarr[0].imshow(an_img, cmap=COLORMAP)
#plt.subplot(122)
#plt.hist(an_img.flatten(), bins=256, color='c')
#plt.xlabel("Raw Scan Pixel Value")
#plt.ylabel("Frequency")
#plt.show()
