from win10toast import ToastNotifier

previousemailPath = "" # PUT THE FULL PATH OF THE TXT FILE NAMED "previousemail.txt"

with open(previousemailPath, "r") as file:
    data = file.read().rstrip()

text = f"The currently generated email is: {data}"

toaster = ToastNotifier()

toaster.show_toast("Email Alias Service", text, icon_path=None, duration=0)
