def get_image_path(instance,filename):
    folder_path = f"images/{instance.destination.destination_name}"
    file_path = f"{folder_path/filename}"
    return file_path
