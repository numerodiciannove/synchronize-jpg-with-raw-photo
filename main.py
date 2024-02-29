import os
import shutil
import tkinter as tk
from tkinter import filedialog

JPG_TYPE = [
    "tif",
    "tiff",
    "ico",
    "cur",
    "bmp",
    "webp",
    "png",
    "jpg",
    "jpeg",
    "jfif",
    "pjpeg",
    "pjp",
    "gif",
    "avif",
    "apng"
]
JPG_DIR = ""
RAW_TYPE = [
    "3fr",
    "ari",
    "arw",
    "bay",
    "braw",
    "crw",
    "cr2",
    "cr3",
    "cap",
    "data",
    "dcs",
    "dcr",
    "dng",
    "drf",
    "eip",
    "erf",
    "fff",
    "gpr",
    "iiq",
    "k25",
    "kdc",
    "mdc",
    "mef",
    "mos",
    "mrw",
    "nef",
    "nrw",
    "obm",
    "orf",
    "pef",
    "ptx",
    "pxn",
    "r3d",
    "raf",
    "raw",
    "rwl",
    "rw2",
    "rwz",
    "sr2",
    "srf",
    "srw",
    "tif",
    "x3f"
]
RAW_DIR = ""
OUTPUT_DIR = ""


def synchronize_jpg_with_raw():
    global JPG_DIR, RAW_DIR, OUTPUT_DIR

    no_raw_version = []
    for jpg_type in JPG_TYPE:
        jpg_files = [f for f in os.listdir(JPG_DIR) if
                     f.lower().endswith("." + jpg_type)]
        for jpg_file in jpg_files:
            raw_found = False
            for raw_type in RAW_TYPE:
                raw_file = jpg_file[:-len(jpg_type)] + raw_type
                if os.path.exists(os.path.join(RAW_DIR, raw_file)):
                    print(
                        f"RAW-version for {jpg_file} "
                        f"exists. Copying RAW-version to directory.")
                    shutil.copy(os.path.join(RAW_DIR, raw_file), OUTPUT_DIR)
                    raw_found = True
                    break
            if not raw_found:
                print(f"No RAW-version found for {jpg_file}.")
                no_raw_version.append(jpg_file)

    with open(os.path.join(OUTPUT_DIR, "no_raw_version.txt"), "w") as file:
        for jpg_file in no_raw_version:
            file.write(jpg_file + "\n")

    if no_raw_version:
        return no_raw_version
    else:
        print("All files were copied")


def browse_button(dir_variable):
    dir_name = filedialog.askdirectory()
    dir_variable.delete(0, tk.END)
    dir_variable.insert(0, dir_name)


def run_synchronization():
    global JPG_DIR, RAW_DIR, OUTPUT_DIR
    JPG_DIR = jpg_dir_entry.get()
    RAW_DIR = raw_dir_entry.get()
    OUTPUT_DIR = output_dir_entry.get()
    synchronize_jpg_with_raw()
    status_label.config(text="Synchronization completed.")


root = tk.Tk()
root.title("JPG and RAW Synchronizer")

tk.Label(root, text="JPG Directory:").grid(row=0, column=0, sticky="e")
jpg_dir_entry = tk.Entry(root)
jpg_dir_entry.grid(row=0, column=1)
tk.Button(root, text="Browse",
          command=lambda: browse_button(jpg_dir_entry)).grid(row=0, column=2)

tk.Label(root, text="RAW Directory:").grid(row=1, column=0, sticky="e")
raw_dir_entry = tk.Entry(root)
raw_dir_entry.grid(row=1, column=1)
tk.Button(root, text="Browse",
          command=lambda: browse_button(raw_dir_entry)).grid(row=1, column=2)

tk.Label(root, text="Output Directory:").grid(row=2, column=0, sticky="e")
output_dir_entry = tk.Entry(root)
output_dir_entry.grid(row=2, column=1)
tk.Button(root, text="Browse",
          command=lambda: browse_button(output_dir_entry)).grid(row=2,
                                                                column=2)

run_button = tk.Button(root, text="Run", command=run_synchronization)
run_button.grid(row=3, column=1)

status_label = tk.Label(root, text="")
status_label.grid(row=4, column=0, columnspan=3)

root.mainloop()
