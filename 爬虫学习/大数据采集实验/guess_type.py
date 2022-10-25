import filetype

def get_type(file_path):
    kind = filetype.guess(file_path)
    if kind is None:
        print('Cannot guess file type!')
        return
    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)

get_type(r"F:\BaiduNetdiskDownload\2022.6.amv")