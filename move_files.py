import os
import shutil

def copy_selected_files(source_dir, destination_dir, filenames):
    """
    copies specific files from source_dir to destination_dir
    """

    # ensure destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    for filename in filenames:
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)

        if os.path.exists(source_path):
            try:
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {filename}")
            except Exception as e:
                print(f"Error copying {filename}: {e}")
        else:
            print(f"File not found: {filename}")


if __name__ == "__main__":
    source_directory = r"D:\\UConn grad"
    destination_directory = r"E:\\grad pics"

    files = '''04416
    04421
    04453
    04580
    04603
    04624
    04638
    04646
    04651
    04710
    04752
    04779
    04786
    04812
    04840
    04846
    04853
    04864
    04885
    04891
    04894
    04898
    04911
    04919
    05094
    05097
    05117
    05120
    05184
    05210
    05246
    05249
    05251
    05255
    05257
    05259
    05269
    05263
    05266
    05274
    05277
    05356
    05360
    05370
    05382
    05398
    05417
    05434
    05443
    05452
    05457
    05515
    05523
    05749
    05759
    05766
    05771
    05780
    05807
    05855
    05867
    05900
    05904
    05907
    05910
    05927
    05989
    06025
    06060
    06062
    06064
    06071
    06087
    06136
    06138
    06152
    06165
    06186
    06194
    06240
    06243
    06247
    06251
    06261
    06268
    06282
    06286'''

    files = files.split()
    for i in range(len(files)):
        files[i] = 'DSC' + files[i] + '.ARW'

    files_to_copy = files

    copy_selected_files(source_directory, destination_directory, files_to_copy)