import os
import shutil
from glob import glob

JPG_TYPE = ".jpg"
JPG_DIR = r"C:\Users\numer\Desktop\test\jpg"

RAW_TYPE = ".NEF"
RAW_DIR = r"C:\Users\numer\Desktop\test\raw"

OUTPUT_DIR = r"C:\Users\numer\Desktop\test\sorted"


def synchronize_jpg_with_raw(jpg_directory, raw_directory, output_directory):
    no_raw_version = []

    jpg_files = glob(os.path.join(jpg_directory, f"*{JPG_TYPE}"))

    for jpg_file in jpg_files:
        jpg_filename = os.path.basename(jpg_file)
        raw_filename = os.path.splitext(jpg_filename)[0] + RAW_TYPE
        raw_file_path = os.path.join(raw_directory, raw_filename)

        if os.path.exists(raw_file_path):
            print(
                f"RAW-version for {jpg_filename} exists. "
                f"Copying RAW-version to directory."
            )
            shutil.copy(raw_file_path, output_directory)
        else:
            print(f"No RAW-version found for {jpg_filename}.")
            no_raw_version.append(jpg_filename)

    with open(
            os.path.join(output_directory, "no_raw_version.txt"), "w"
    ) as file:
        file.write("\n".join(no_raw_version))

    if no_raw_version:
        print("Some files were not copied, check 'no_raw_version.txt'")
    else:
        print("All files were copied")

    return no_raw_version


copied_raw_files = synchronize_jpg_with_raw(JPG_DIR, RAW_DIR, OUTPUT_DIR)
