
from PIL import Image

pic="c:/mywife.jpg"
im = Image.open(pic)
# im.show()
print(im.format)
print(im.mode)
print(im.size)
print(im.info)
print(im)
# im.save('JPG')
# im.save("xinyuanjieyi")
im.save("c:/xinyuanjieyi.png")
im2 = Image.open("c:/xinyuanjieyi.png")
print(im2.format)
#
# box = (300, 100, 700, 700)              ##确定拷贝区域大小
# region = im.crop(box)                   ##将im表示的图片对象拷贝到region中，大小为box
# region.show()

sequ = im.getdata()
sequ0 = list(sequ)
print(sequ0[0])
print(sequ0[1])
print(sequ0[2])

print(im2.getpixel((4,0)))
r,g,b = im2.split()
print(b.getpixel((4,1)))


pix = im.load()
r,g,b = im.split()
print(b.pix[4,3])
print(pix[4,2])
r,g,b =im.split()

#定义：im.getcolors() ⇒ a list of(count, color) tuples or None
#im.getcolors(maxcolors) ⇒ a list of (count, color) tuples or None
#含义：（New in 1.1.5）返回一个（count，color）元组的无序list，其中count是对应颜色在图像中出现的次数。
#如果变量maxcolors的值被超过，该方法将停止计算并返回空。变量maxcolors默认值为256。为了保证用户可以获取图像中的所有颜色，you can pass in size[0]*size[1]（请确保有足够的内存做这件事）。

#例子：
#
from PIL import Image
im1 = Image.open("test.png")
print(im1.getcolors(8888888))
#输出：
