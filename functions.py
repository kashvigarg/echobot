def check_size(file_size):
    file_size_in_mb = file_size / 1048576
    if (file_size_in_mb) > 25:
        return file_size_in_mb, False
    else :
        return file_size_in_mb, True