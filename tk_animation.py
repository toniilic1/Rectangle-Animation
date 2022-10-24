import tkinter as tk
def main():
   root=tk.Tk()

   WIDTH = 500
   HEIGHT = 500
   canvas=tk.Canvas(root,width=WIDTH,height=HEIGHT)
   canvas.pack()

   rectangle_blue = canvas.create_rectangle(250, 250, 100, 100, outline="white",fill="blue")
   rectangle_green = canvas.create_rectangle(250, 250, 400, 400, outline="white",fill="green")
   rectangle_yellow = canvas.create_rectangle(250, 250, 100, 400, outline="white",fill="yellow")
   rectangle_red = canvas.create_rectangle(250, 250, 400, 100, outline="white",fill="red")
 
   def redraw_green():
      canvas.after(50,redraw_green)
      canvas.move(rectangle_green,15,15)

   def redraw_blue():
      canvas.after(50,redraw_blue)
      canvas.move(rectangle_blue,-15,-15)

   def redraw_yellow():
      canvas.after(50,redraw_yellow)
      canvas.move(rectangle_yellow,-15,15)

   def redraw_red():
      canvas.after(50,redraw_red)
      canvas.move(rectangle_red, 15,-15)

   redraw_green()
   redraw_blue()
   redraw_yellow()
   redraw_red()

   root.mainloop()


if __name__ == '__main__':
   main()