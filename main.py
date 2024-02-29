import os
import shutil

JPG_TYPE = ".jpg"
JPG_DIR = r"C:\Users\numer\Desktop\test\jpg"

RAW_TYPE = ".NEF"
RAW_DIR = r"C:\Users\numer\Desktop\test\raw"

OUTPUT_DIR = r"C:\Users\numer\Desktop\test\sorted"


def synchronize_jpg_with_raw(jpg_directory, raw_directory, output_directory):
    no_raw_version = []
    jpg_files = [f for f in os.listdir(jpg_directory) if
                 f.lower().endswith(JPG_TYPE)]

    for jpg_file in jpg_files:
        raw_file = jpg_file[:-len(JPG_TYPE)] + RAW_TYPE
        if os.path.exists(os.path.join(raw_directory, raw_file)):
            print(
                f"RAW-version for {jpg_file} exists. "
                f"Copying RAW-version to directory."
            )
            shutil.copy(
                os.path.join(raw_directory, raw_file), output_directory
            )
        else:
            print(f"No RAW-version found for {jpg_file}.")
            no_raw_version.append(jpg_file)

    with open(
            os.path.join(output_directory, "no_raw_version.txt"), "w"
    ) as file:
        for jpg_file in no_raw_version:
            file.write(jpg_file + "\n")

    return no_raw_version


copied_raw_files = synchronize_jpg_with_raw(JPG_DIR, RAW_DIR, OUTPUT_DIR)
print("Copied RAW files:", copied_raw_files)
