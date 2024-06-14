import os
import shutil

def organiseDire(path):
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path,file)):
            continue
        file_name,file_extension = os.path.splitext(file)
        directory = file_extension[1:]

        if not directory:
            directory="Other"
        new_dir = os.path.join(path,directory)
        os.makedirs(new_dir,exist_ok=True)
        shutil.copyfile(src=os.path.join(path,file),dst=os.path.join(new_dir,file))
        print(f"moved {file} at this {new_dir}")

def main():
    path = r"C:/Users/GautamRaj/Downloads/"
    organiseDire(path)


if __name__ == "__main__":
    main()