import os
import sys

abs_path = os.path.dirname(__file__)
rel_path = "../.env/lib64/python3.12/site-packages"
sys.path.append(os.path.join(abs_path, rel_path))
from dotenv import load_dotenv


def is_image_exists_in_gns3_folder(gns3_folder_path: str, image_name: str) -> bool:
    is_file_in_folder = os.path.isfile(gns3_folder_path + image_name)
    if is_file_in_folder:
        decision = "y"
        decision = input(
            f"Do you want to delete the old image {image_name} from the GNS3 folder? [y/n]: "
        )
        if decision == "y":
            delete_image_in_gns3_folder(gns3_folder_path, image_name)
        else:
            print("End the script by a user decision.")
            exit()
    return is_file_in_folder


def delete_image_in_gns3_folder(gns3_folder_path: str, image_name: str):
    cmd = f"rm {gns3_folder_path}{image_name}"
    os.system(cmd)


def copy_image_from_vm_folder_to_gns3_folder(
    image_path: str, gns3_folder_path: str, image_name: str
):
    cmd = f"cp {image_path}{image_name} {gns3_folder_path}"
    os.system(cmd)


def change_image_mod(permissions: str, gns3_folder_path: str, image_name: str):
    cmd = f"chmod {permissions} {gns3_folder_path}{image_name}"
    os.system(cmd)


def change_image_owner(owner: str, gns3_folder_path: str, image_name: str):
    cmd = f"chown {owner} {gns3_folder_path}{image_name}"
    os.system(cmd)


load_dotenv()

gns3_images_path = os.getenv("GNS3_FOLDER_PATH")
vm_images_path = os.getenv("VM_IMAGE_PATH")
owner = os.getenv("OWNER")
permissions = os.getenv("PERMISSIONS")
vm_image_name = sys.argv[1]


print("->[1] Check does the file exist in the GNS3 folder...")
is_image_exists_in_gns3_folder(gns3_images_path, vm_image_name)
print("Done, success.")
print(f"->[2] Copy the image {vm_image_name} to the` GNS3 folder...")
copy_image_from_vm_folder_to_gns3_folder(
    vm_images_path, gns3_images_path, vm_image_name
)
print("Done, success.")
print(f"->[3] Set the premissions to the image {vm_image_name}...")
change_image_mod(permissions, gns3_images_path, vm_image_name)
print("Done, success.")
print(f"->[4] Set the owner to  the image {vm_image_name}...")
change_image_owner(owner, gns3_images_path, vm_image_name)
print("All steps done, success.")
