"""
Create Image abstract class with instance attributes as parameters: width, length, bit_depth
Image class defines abstract method export()
Create Jpeg and Png derived classes that implement export() method
"""


class Image:
    ...


class Jpeg:
    ...


class Png:
    ...


jpeg = Jpeg(width=1080, length=960, bit_depth=24)
jpeg.export()
