from myimports import *

body_zones_img = plt.imread(BODY_ZONES)
fig, ax = plt.subplots(figsize=(15,15))
ax.imshow(body_zones_img)
plt.show()
