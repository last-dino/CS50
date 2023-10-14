# name = "." + input("File name: ").strip().lower()
# the last submission is incorrect, because in the case the file name is 'gif' without any extension, it will return image/gif
name = input("File name: ").strip().lower()
if "." in name:
    filename, extension = name.rsplit(".", 1)
else:
    filename, extension = name, None


match extension:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")