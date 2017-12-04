from myimports import *
from improve_contrast_greyscale import *
from segmenting import *
from mask_using_vertices import *
 
#-----------------------------------------------------------------------------------------
# crop(img, crop_list):                uses vertices to mask the image
#
# img:                                 the image to be cropped
#
# crop_list:                           a crop_list entry with [x , y, width, height]
#
# returns:                             a cropped image
#-----------------------------------------------------------------------------------------
def crop(img, crop_list):

    x_coord = crop_list[0]
    y_coord = crop_list[1]
    width = crop_list[2]
    height = crop_list[3]
    cropped_img = img[x_coord:x_coord+width, y_coord:y_coord+height]
    
    return cropped_img
  
'''
# unit test -----------------------------------------------------------------
fig, axarr = plt.subplots(nrows=4, ncols=4, figsize=(10,10))
#    
threat_zone = 14
i = 0
for row in range(4):
    for col in range(4):
        an_img = get_single_image(APS_FILE_NAME, i)
        img_rescaled = convert_to_grayscale(an_img)
        img_high_contrast = spread_spectrum(img_rescaled)
        if zone_slice_list[threat_zone][i] is not None:
            masked_img = roi(img_high_contrast, zone_slice_list[threat_zone][i])
            cropped_img = crop(masked_img, zone_crop_list[threat_zone][i])
            #resized_img = cv2.resize(cropped_img, (0,0), fx=0.1, fy=0.1)
            axarr[row, col].imshow(cropped_img, cmap=COLORMAP)
        i += 1

plt.show()
'''
