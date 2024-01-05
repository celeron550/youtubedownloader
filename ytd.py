from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable
from os import rename

def baixar(url):
    global link,pl,ext
    
    try:
        if ext == '1':
            stream = link.streams.get_highest_resolution()
            stream.download(output_path="./downloads/")
        elif ext == '2':
            stream = link.streams.get_lowest_resolution()
            stream.download(output_path="./downloads/")
        elif ext == '3':
            stream = link.streams.get_audio_only()
            stream.download(output_path="./downloads/")
            print('convertendo...')
            file_path = f'./downloads/{link.title}.mp4'
            rename(file_path, f'{link.title}.mp3')

            
        
        
        print('Baixado.')
    except VideoUnavailable:
        print(f'Vídeo indisponível:{link.title}')


    

isplaylist = input("é playlist \n[1] Sim [2] Não : ")
if isplaylist == '1':
    pl = Playlist(input('Link da playlist: '))
    ext = input('Selecione como deseja baixar:\n[1]Resolução mais alta\n[2]Resolução mais baixa\n[3]Apenas áudio\n -> ')
    for link in pl.videos:
        print(f'Baixando Vídeo {link.title}')
        baixar(pl)

elif isplaylist == '2': 
    link = YouTube(input('Link do Vídeo: '),
        use_oauth=False,
        allow_oauth_cache=True) 
    ext = input('Selecione como deseja baixar\n[1]Resolução mais alta\n[2]Resolução mais baixa\n[3]Apenas áudio\n -> ') 
    print(f'Baixando Vídeo: {link.title}')
    baixar(link)
    
    
else:
    print('Resposta inválida, tente novamente') 
    isplaylist = input("é playlist \n[1] Sim [2] Não : ")




