from myimports import *
from improve_contrast_greyscale import *
from segmenting_whole import *
#-----------------------------------------------------------------------------------------
# roi(img, vertices):              uses vertices to mask the image
#
# img:                             the image to be masked
#
# vertices:                        a set of vertices that define the region of interest
#
# returns:                         a masked image
#-----------------------------------------------------------------------------------------
def roi(img, vertices):
    
    # blank mask
    mask = np.zeros_like(img)

    # fill the mask
    cv2.fillPoly(mask, [vertices], 255)

    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    

    return masked

''' 
# unit test -----------------------------------------------------------------
fig, axarr = plt.subplots(nrows=4, ncols=4, figsize=(10,10))
#    
threat_zone = 11
i = 0
for row in range(4):
    for col in range(4):
        an_img = get_single_image(APS_FILE_NAME, i)
        img_rescaled = convert_to_grayscale(an_img)
        img_high_contrast = spread_spectrum(img_rescaled)
        if zone_slice_list[threat_zone -  1][i] is not None:
            masked_img = roi(img_high_contrast, zone_slice_list[threat_zone - 1][i])
            #resized_img = cv2.resize(masked_img, (0,0), fx=0.1, fy=0.1)
            axarr[row, col].imshow(masked_img, cmap=COLORMAP)
        i += 1
plt.show()
'''
