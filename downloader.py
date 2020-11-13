import os
import pafy

def check_path():
    path = os.getcwd()
    path_to_download = path + '\\Download'
    if not os.path.exists(path_to_download):
        os.mkdir(path_to_download)
    return path_to_download

def download(url, choose, path):

    v = pafy.new(url)

    avaible_stremas = {}
    count = 1

    streams = None

    if choose == 1:
        streams = v.streams
    elif choose == 2:
        streams = v.audiostreams

    
    for i in streams:
        avaible_stremas[count] = i
        print(f'{count} - {i}')
        count += 1

    st = int(input('Введите качество - '))

    streams[st - 1].download(path)
    
    string = v.title + '.' + ((str(streams[st - 1])).split('@'))[0].split(':')[1]
    print(f'{string} - downloaded')

while True:
    path = check_path()
    url = input('Введите url: ')
    choose = int(input('Скачать видео-1 или аудио-2: '))
    download(url, choose, path)
