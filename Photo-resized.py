
# Kütüphaneleri içe aktarma
import PIL.Image
from resizeimage import resizeimage
import cv2
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox 

# Fotoğraf seçme
def select_file():
  global image_file_name
  # Fotoğraf seçme
  image_file_name = filedialog.askopenfilename(initialdir = "/",title = "Dosya Seç")

# Fotoğrafı yeniden boyutlandırma
def image_resize():
  # Fotoğrafı binary biçimde açma
  with open(image_file_name, 'rb') as file:

    # Fotoğrafı seçme
    image = PIL.Image.open(file)

    # Fotoğrafı yeniden boyutlandırma
    resized_image = resizeimage.resize_cover(image, [int(width.get()), int(height.get())],validate=False)
    resized_image.save('resized_image.png', image.format)

  # Mesaj kutusu: Fotoğraf yeniden oluşturma başarılı
  messagebox.showinfo("Image Resized", "Image Successfully Resized") 

# Fotoğrafı görüntüleme
def view_image():
  # Fotoğrafı Okuma
  view_resized_image = cv2.imread("resized_image.png")

  # Fotoğrafı okuma
  cv2.imshow("Resized Image",view_resized_image)
  cv2.waitKey(0)

# Tkinter nesnesi oluşturma
root = Tk()

# Başlık 
root.title("Image Resizer")

# App Boyutu
root.geometry("340x250")

# Gerekli label , buton vs.
Label(root,text="Image Resizer",font=("Comic Sans MS", 16, "bold")).grid(row=0,column=1,columnspan=3)

Label(root,text="Select Image:- ",font=("Comic Sans MS", 16, "bold")).grid(row=1,column=1)
Button(root,text="Image File",command=select_file,font=13).grid(row=1,column=2)

Label(root,text="Width:- ",font=("Comic Sans MS", 16, "bold")).grid(row=2,column=1)
width = Entry(root,font=13,width=15)
width.grid(row=2,column=2)

Label(root,text="Height:- ",font=("Comic Sans MS", 16, "bold")).grid(row=3,column=1)
height = Entry(root,font=13,width=15)
height.grid(row=3,column=2)

Button(root,text="Resize",command=image_resize,font=13).grid(row=4,column=1)
Button(root,text="View",command=view_image,font=13).grid(row=4,column=2)

# Tkinter çalıştıma
root.mainloop()