from myimports import *
from get_single_image import *
from convert_to_greyscale import *
#-------------------------------------------------------------------------------
# spread_spectrum(img):        applies a histogram equalization transformation
#
# img:                         a single scan
#
# returns:                     a transformed scan
#-------------------------------------------------------------------------------

def spread_spectrum(img):
    #img = stats.threshold(img, threshmin=12, newval=0)
    img = np.clip(img, a_min=10, a_max=None)
    #img = cv2.equalizeHist(img)
    # see http://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img= clahe.apply(img)
    
    return img
  
# unit test ------------------------------------------
#an_img = get_single_image(APS_FILE_NAME, 0)
#img_rescaled = convert_to_grayscale(an_img)
#img_high_contrast = spread_spectrum(img_rescaled)

#fig, axarr = plt.subplots(nrows=1, ncols=2, figsize=(20, 5))

#axarr[0].imshow(img_high_contrast, cmap=COLORMAP)
#plt.subplot(122)
#plt.hist(img_high_contrast.flatten(), bins=256, color='c')
#plt.xlabel("Grayscale Pixel Value")
#plt.ylabel("Frequency")
#plt.show()
