from myimports import *
from read_file import read_data
#----------------------------------------------------------------------------------
# plot_image_set(infile):  takes an aps file and shows all 16 90 degree shots
#
# infile:                  an aps file
#----------------------------------------------------------------------------------
def plot_image_set(infile):

    # read in the aps file, it comes in as shape(512, 620, 16)
    img = read_data(infile)
    
    # transpose so that the slice is the first dimension shape(16, 620, 512)
    img = img.transpose()
        
    # show the graphs
    fig, axarr = plt.subplots(nrows=4, ncols=4, figsize=(10,10))
    
    i = 0
    for row in range(4):
        for col in range(4):
            #resized_img = cv2.resize(img[i], (0,0), fx=0.1, fy=0.1)
            #axarr[row, col].imshow(np.flipud(resized_img), cmap=COLORMAP)
            axarr[row, col].imshow(np.flipud(img[i]), cmap=COLORMAP)
            i += 1
    
    print('Done!')

# unit test ----------------------------------
plot_image_set(APS_FILE_NAME)
plt.show()
