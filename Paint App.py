from tkinter import *
import tkinter.font
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox


class PaintApp:

    def quit_app(self, event=None):
        root.quit()

    def clear(self, event=None):
        self.drawing_area.delete(ALL)

    def draw(self, value):
        self.drawing_tool = value
        return self.drawing_tool

    def font(self, value):
        self.fonts = value
        return self.fonts

    drawing_tool = ""
    fonts = "Arial"

    left_but = "up"

    x_pos, y_pos = None, None

    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

    # ---------- CATCH MOUSE Down ----------

    def left_but_down(self, event=None):
        self.left_but = "down"

        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

    # ---------- CATCH MOUSE UP ----------

    def left_but_up(self, event=None):
        self.left_but = "up"

        # Reset the line
        self.x_pos = None
        self.y_pos = None

        # Set x & y when mouse is released
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        if self.drawing_tool == "Line":
            self.line_draw(event)
        elif self.drawing_tool == "Arc":
            self.arc_draw(event)
        elif self.drawing_tool == "Oval":
            self.oval_draw(event)
        elif self.drawing_tool == "Rectangle":
            self.rectangle_draw(event)
        elif self.drawing_tool == "Text":
            self.text_draw(event)

    # ---------- CATCH MOUSE MOVEMENT ----------

    def motion(self, event=None):

        if self.drawing_tool == "Pencil":
            self.pencil_draw(event)

    # ---------- DRAW PENCIL ----------

    def pencil_draw(self, event=None):
        if self.left_but == "down":

            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth=TRUE)

            self.x_pos = event.x
            self.y_pos = event.y

    # ---------- DRAW LINE ----------

    def line_draw(self, event=None):

        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=TRUE,
                                     fill="green")

    # ---------- DRAW ARC ----------

    def arc_draw(self, event=None):

        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt

            event.widget.create_arc(coords, start=0, extent=150,
                                    style=ARC)

    # ---------- DRAW OVAL ----------

    def oval_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):


            event.widget.create_oval(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt,
                                     fill="midnight blue",
                                     outline="yellow",
                                     width=2)

    # ---------- DRAW RECTANGLE ----------

    def rectangle_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):

            event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt,
                                          fill="midnight blue",
                                          outline="yellow",
                                          width=2)

    # ---------- DRAW TEXT ----------

    def text_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt):
            # Show all fonts available
            print(tkinter.font.families())

            text_font = tkinter.font.Font(family=self.fonts,
                                          size=20, weight='bold', slant='italic')

            event.widget.create_text(self.x1_line_pt, self.y1_line_pt,
                                     fill="green",
                                     font=text_font,
                                     text="WOW")

    def show_about(self, event=None):
        messagebox.showwarning("About", "Made Paint APP in 2017")

    def __init__(self, root):

        root.title("Paint App")
        root.geometry("600x600")

        menu_bar = Menu(root)
        # --- FILE menu ---
        file_menu = Menu(root, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=lambda: self.quit_app())

        menu_bar.add_cascade(label="File", menu=file_menu)

        # ---- Tools MENU ----

        tool_menu = Menu(root, tearoff=0)
        tool_menu.add_radiobutton(label="Pencil", command=lambda: self.draw("Pencil"))
        tool_menu.add_radiobutton(label="Line", command=lambda: self.draw("Line"))
        tool_menu.add_radiobutton(label="Arc", command=lambda: self.draw("Arc"))
        tool_menu.add_radiobutton(label="Oval", command=lambda: self.draw("Oval"))
        tool_menu.add_radiobutton(label="Rectangle", command=lambda: self.draw("Rectangle"))
        tool_menu.add_radiobutton(label="Text", command=lambda :self.draw("Text"))

        # -- Fonts Menu --

        font_menu = Menu(root, tearoff=0)
        font_menu.add_radiobutton(label="Times New Roman", command=lambda: self.font("Times New Roman"))
        font_menu.add_radiobutton(label="Arial", command=lambda: self.font("Arial"))
        font_menu.add_radiobutton(label="Tahoma", command=lambda: self.font("Tahoma"))
        font_menu.add_radiobutton(label="Batang", command=lambda: self.font("Batang"))

        # -- Edit Menu --

        edit_menu = Menu(root, tearoff=0)
        edit_menu.add_cascade(label="Tools", menu=tool_menu)
        edit_menu.add_cascade(label="Fonts", menu=font_menu)
        edit_menu.add_separator()
        edit_menu.add_command(label="Clear Everything", command=self.clear)

        menu_bar.add_cascade(labe="Edit", menu=edit_menu)

        # -- HELP Menu --
        help_menu = Menu(root, tearoff=0)
        help_menu.add_command(label="About", accelerator="Ctrl-A",
                              command= self.show_about)

        menu_bar.add_cascade(label="Help", menu=help_menu)

        root.configure(menu=menu_bar)

        # ----- BUTTONS TOOLBAR -----
        toolbar = Frame(root, bd=2, relief=RAISED)

        pencil_img = Image.open("pencil.png")
        line_img = Image.open("line.png")
        arc_img = Image.open("arc.png")
        oval_img = Image.open("oval.png")
        rectangle_img = Image.open("rectangle.png")
        text_img = Image.open("text.png")
        exit_img = Image.open("exit.png")

        pencil_icon = ImageTk.PhotoImage(pencil_img)
        line_icon = ImageTk.PhotoImage(line_img)
        arc_icon = ImageTk.PhotoImage(arc_img)
        oval_icon = ImageTk.PhotoImage(oval_img)
        rectangle_icon = ImageTk.PhotoImage(rectangle_img)
        text_icon = ImageTk.PhotoImage(text_img)
        exit_icon = ImageTk.PhotoImage(exit_img)

        pencil_button = ttk.Button(toolbar, image=pencil_icon,
                        command=lambda: self.draw("Pencil"))
        line_button = Button(toolbar, image=line_icon,
                        command=lambda: self.draw("Line"))
        arc_button = Button(toolbar, image=arc_icon,
                             command=lambda: self.draw("Arc"))
        oval_button = Button(toolbar, image=oval_icon,
                             command=lambda: self.draw("Oval"))
        rectangle_button = Button(toolbar, image=rectangle_icon,
                             command=lambda: self.draw("Rectangle"))
        text_button = Button(toolbar, image=text_icon,
                             command=lambda: self.draw("Text"))
        exit_button = Button(toolbar, image=exit_icon,
                             command=lambda: self.quit_app())


        pencil_button.image = pencil_icon
        line_button.image = line_icon
        arc_button.image = arc_icon
        oval_button.image = oval_icon
        rectangle_button.image = rectangle_icon
        text_button.image = text_icon
        exit_button.image = exit_icon

        pencil_button.pack(side=LEFT, padx=5, pady=5)
        line_button.pack(side=LEFT, padx=5, pady=5)
        arc_button.pack(side=LEFT, padx=5, pady=5)
        oval_button.pack(side=LEFT, padx=5, pady=5)
        rectangle_button.pack(side=LEFT, padx=5, pady=5)
        text_button.pack(side=LEFT, padx=5, pady=5)
        exit_button.pack(side=LEFT, padx=5, pady=5)
        toolbar.pack(side=TOP, fill = X)

        # ----- KEYS BINDINGS -----
        self.drawing_area = Canvas(root, height=1000, width=1500)
        self.drawing_area.pack()
        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        self.drawing_area.bind("<ButtonRelease-1>", self.left_but_up)
        root.bind("<Command-a>", self.show_about)
        root.bind("<Command-A>", self.show_about)



root = Tk()

paint_app = PaintApp(root)

root.mainloop()