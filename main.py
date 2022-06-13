import PySimpleGUI as sg
from pytube import YouTube


def executar_download(link, path):
    video = YouTube(link)
    video.streams.get_highest_resolution().download(output_path=path)


layout = [[sg.Text('Informe a URL do vídeo: '), sg.InputText()],
          [sg.Text('Salvar na pasta: '), sg.InputText(), sg.FolderBrowse()],
          [sg.Button('Baixar'), sg.Button('Cancelar')]]

janela = sg.Window('YoutubeVideoDownloader', layout)

while True:
    event, values = janela.read()
    if event == 'Cancelar' or event == sg.WIN_CLOSED:
        break
    elif event == 'Baixar':
        executar_download(values[0], values[1])
        sg.popup_ok('O vídeo foi baixado com sucesso!')

janela.close()
