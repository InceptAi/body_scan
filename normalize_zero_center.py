from myimports import *
from improve_contrast_greyscale import *
from segmenting import *
from mask_using_vertices import *
from crop_250_250 import *
#------------------------------------------------------------------------------------------
# normalize(image): Take segmented tsa image and normalize pixel values to be 
#                   between 0 and 1
#
# parameters:      image - a tsa scan
#
# returns:         a normalized image
#
#------------------------------------------------------------------------------------------

def normalize(image):
    MIN_BOUND = 0.0
    MAX_BOUND = 255.0
    
    image = (image - MIN_BOUND) / (MAX_BOUND - MIN_BOUND)
    image[image>1] = 1.
    image[image<0] = 0.
    return image


#unit test ---------------------
'''
an_img = get_single_image(APS_FILE_NAME, 0)
img_rescaled = convert_to_grayscale(an_img)
img_high_contrast = spread_spectrum(img_rescaled)
masked_img = roi(img_high_contrast, zone_slice_list[0][0])
cropped_img = crop(masked_img, zone_crop_list[0][0])
normalized_img = normalize(cropped_img)
#print ('Normalized: length:width -> {:d}:{:d}|mean={:f}'.format(len(normalized_img), len(normalized_img[0]), normalized_img.mean()))
#print (' -> type ', type(normalized_img))
#print (' -> shape', normalized_img.shape)
'''

#-------------------------------------------------------------------------------------
# zero_center(image): Shift normalized image data and move the range so it is 0 c
#                     entered at the PIXEL_MEAN
#
# parameters:         image
#
# returns:            a zero centered image
#
#-----------------------------------------------------------------------------------------------------------
def zero_center(image):
     
    PIXEL_MEAN = 0.014327
    
    image = image - PIXEL_MEAN
    return image

#unit test ---------------------
'''
an_img = get_single_image(APS_FILE_NAME, 0)
img_rescaled = convert_to_grayscale(an_img)
img_high_contrast = spread_spectrum(img_rescaled)
masked_img = roi(img_high_contrast, zone_slice_list[0][0])
cropped_img = crop(masked_img, zone_crop_list[0][0])
normalized_img = normalize(cropped_img)
zero_centered_img = zero_center(normalized_img)
print ('Zero Centered: length:width -> {:d}:{:d}|mean={:f}'.format(len(zero_centered_img), len(zero_centered_img[0]), zero_centered_img.mean()))
print ('Conformed: Type ->', type(zero_centered_img), 'Shape ->', zero_centered_img.shape)
'''
