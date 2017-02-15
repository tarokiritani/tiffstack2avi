tiffstack2avi
=============
tiffstack2Avi.convert() converts multiple tiff sequences to avi files using ffmpeg (https://ffmpeg.org/). Intended to work on tiff sequences generated by fastCamRecord (http://www.brain-recording.science/software).

Install
-------

    pip install tiffstack2avi

Usage
-----
You first need to install ffmpeg (https://ffmpeg.org/) on your computer. Then,
    import tiffstack2avi
    tiffstack2avi.convert()

Choose the folders that contain tiff sequences. The tiff files should be named frame%d.tif. It would be great if you could aknowledge my work and cite my paper.