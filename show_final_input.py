from myimports import *
#from improve_contrast_greyscale import *
#from segmenting_whole import *
#from mask_using_vertices import *
#from normalize_zero_center import *
#from crop_250_250 import * 
from get_single_image import *
from tsahelper_whole import *
from optparse import OptionParser
# unit test -----------------------------------------------------------------
fig, axarr = plt.subplots(nrows=4, ncols=4, figsize=(10,10))
#    
op = OptionParser()
op.add_option("-t", "--tzone", dest="threat_zone", help="Threat Zone", default=None)
op.add_option("-i", "--input", dest="input_subject_id", help="Input Subject Id", default=None)
(opts, args) = op.parse_args()

if not opts.threat_zone:
    op.print_help()
    op.error("Threat zone is needed")

if not opts.input_subject_id:
    op.print_help()
    op.error("Input subject id is needed")

threat_zone = int(opts.threat_zone)
file_name = INPUT_FOLDER + "/" + opts.input_subject_id + ".aps"
i = 0
for row in range(4):
    for col in range(4):
        an_img = get_single_image(file_name, i)
        img_rescaled = convert_to_grayscale(an_img)
        img_high_contrast = spread_spectrum(img_rescaled)
        if zone_slice_list[threat_zone - 1][i] is not None:
            masked_img = roi(img_high_contrast, zone_slice_list[threat_zone -  1][i])
            cropped_img = crop(masked_img, zone_crop_list[threat_zone - 1][i])
            normalized_img = normalize(cropped_img)
            zero_centered_img = zero_center(normalized_img)
            #resized_img = cv2.resize(cropped_img, (0,0), fx=0.1, fy=0.1)
            axarr[row, col].imshow(zero_centered_img, cmap=COLORMAP)
        i += 1
plt.show()
