#pfv não baixar videos do bluezão
import webbrowser

url = input('Coloque o link do video que vocẽ quer baixar ilegalmente aqui : ')

url =url [:12]+'ss'+url[12:]
webbrowser.open(url)
