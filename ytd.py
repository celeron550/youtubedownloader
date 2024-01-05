from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable
from os import rename
def baixar(link):
    global ext
    try:
        if ext == '1':
            stream = link.streams.get_highest_resolution()
            stream.download(output_path="./downloads/")
            print('Baixado.')
        elif ext == '2':
            stream = link.streams.get_lowest_resolution()
            stream.download(output_path="./downloads/",)
            print('Baixado.')
        elif ext == '3':
            stream = link.streams.get_audio_only()
            stream.download(output_path="./downloads/",)
            print('Baixado.')
            print('convertendo...')
            nome_arquivo = str(link.title).replace(".","")
            nome_arquivo = nome_arquivo.replace(",","")
            nome_arquivo = nome_arquivo.replace("/","")
            nome_arquivo = nome_arquivo.replace("'","")
            titulo = str(link.title).replace("/","")
            file_path = f'./downloads/{nome_arquivo}.mp4'
            rename(file_path, f'./downloads/{titulo}.mp3/')
            print('concluído') 
        else:
            print('Resposta inválida, tente novamente')
            ext = input('Selecione como deseja baixar\n[1]Resolução mais alta\n[2]Resolução mais baixa\n[3]Apenas áudio\n -> ')
    except VideoUnavailable:
        print('Vídeo indisponível :( ')
        

link = input('Digite o link: ')
if link.count('playlist') == 1:
    link = Playlist(link)
    ext = input('Selecione como deseja baixar\n[1]Resolução mais alta\n[2]Resolução mais baixa\n[3]Apenas áudio\n -> ') 
    for video in link.videos:
        baixar(video)
else:
    link=YouTube(link)
    ext = input('Selecione como deseja baixar\n[1]Resolução mais alta\n[2]Resolução mais baixa\n[3]Apenas áudio\n -> ') 
    baixar(link)





