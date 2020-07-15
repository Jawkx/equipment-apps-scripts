# equipment-apps-scripts
Contain scripts that would aid in the equipment list apps. **READ ME BEFORE USING**

## Setup
This action only need to do one time on each device.

### Download and install python 

Download python from this [website](https://www.python.org/) (Must be Python 3.x.x or above)

Note that when installing python remember to tick the box add to path

![add to path](https://datatofish.com/wp-content/uploads/2018/10/0001_add_Python_to_Path.png)

### Verify if Python is downloaded correctly.

Open command prompt and type this code 
`python -- version`

If python was installed correctly the command prompt will print out the version of your python

### Install relevant packages

In the command prompt copy and paste this

```
pip install opencv-python
pip install pyqrcode
```
### Downloading this respo
Download this respo, if you dont have git installed you can download it as ZIP file

## Using the Application

### QR code Generator

1. Open the text file `qr_text.txt`.
2. Type in the custom ID of the equipment that needed to generate the qr code. Remember type everything above the line as shown
`-----type the custom ID above this line press enter for every new line-----`
3. Save the text file.
4. Double click the file `qrcodegenerator.py`.
5. Generated QR code are now located at qrcodes.

**Warning: don't delete the textfile inside each folder** 

### Image resizer
1. Place the image that are needed to resize at the folder before_resized
2. For the image to not be distorted please put square image inside the before_resized folder you can crop the image here [photoresizer](https://www.photoresizer.com/)
3. Double click the file `imageresizer.py`
4. The resized image are now in the the folder resized

**Warning: Dont delete the texfile inside each folder**

## Footnote
If there is any question please [email](mailto:j_kaixuan@live.com) me as I am probably not working at lumiled when you are reading this
