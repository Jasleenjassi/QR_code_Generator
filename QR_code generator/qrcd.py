from tkinter import *
import qrcode
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Student QR Code Generator")
root.geometry("500x400")
option = StringVar()
option.set("select class")
options = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]

# Create input fields for student information
label_roll_number = Label(root, text="Roll Number:", font=('verdana', 10), fg='black')
label_roll_number.place(x=10, y=50)
entry_roll_number = Entry(root, width=20)
entry_roll_number.place(x=100, y=50)

label_name = Label(root, text="Name:", font=('verdana', 10), fg='black')
label_name.place(x=10, y=100)
entry_name = Entry(root, width=20)
entry_name.place(x=100, y=100)

label_class = Label(root, text="Class:", font=('verdana', 10), fg='black')
label_class.place(x=10, y=150)
drop = OptionMenu(root, option, *options)
drop.place(x=100, y=147)

label_age = Label(root, text="Age:", font=('verdana', 10), fg='black')
label_age.place(x=10, y=200)
entry_age = Entry(root, width=20)
entry_age.place(x=100, y=200)

# Create a button to generate the student QR code
submit_button = Button(root, text="Submit", command=lambda: mainwin(root))
submit_button.place(x=70, y=290)


def mainwin(root):
    global qr_label, qr_img_tk

    # Create the second window
    main = Toplevel(root)
    main.title("Student QR Code Generator")
    main.geometry("500x400")
    result_label = Label(root)
    result_label.place(x=200, y=290)

    def generate_student_qr_code():
        global qr_img

        # Get the student information from the input fields
        roll_number = entry_roll_number.get()
        name = entry_name.get()
        student_class = option.get()
        age = entry_age.get()

        # Combine the information into a single string
        student_info = f"Roll Number: {roll_number}\nName: {name}\nClass: {student_class}\nAge: {age}"

        # Generate the QR code
        qr = qrcode.QRCode(
            version=10,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
        )
        qr.add_data(student_info)
        qr.make(fit=True)

        # Create a QR code image
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Display the QR code image in the second window
        qr_img.thumbnail((200, 200))
        qr_img_tk = ImageTk.PhotoImage(qr_img)
        qr_label.config(image=qr_img_tk)
        qr_label.image = qr_img_tk
   
    def down():
        if qr_img is not None:
            # Prompt the user to choose a location to save the QR code image
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

            if file_path:
                qr_img.save(file_path)
                result_label.config(text=f"QR Code saved as '{file_path}'")
        else:
            result_label.config(text="Please generate the QR Code first.")
    generate_button = Button(main, text="Generate QR Code", command=generate_student_qr_code)
    generate_button.place(x=20, y=30)
    down_button = Button(main, text="Download", command=down)
    down_button.place(x=200, y=290)

    qr_label = Label(main)
    qr_label.place(x=200, y=40)

    # Disable the submit button in the
    submit_button.config(state=DISABLED)

    # Bind the main window's close event to a function that closes the second window as well
    main.protocol("WM_DELETE_WINDOW", lambda: main.destroy())

    main.mainloop()


# Start the tkinter main loop
root.mainloop()