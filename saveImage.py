import urllib.request as ur

#pagina inicial
resource = ur.urlopen("http://www.imagebam.com/image/90a1bd345588084")
for i in range(175):
    htmltoparse = resource.read().decode()
    start = htmltoparse.find("<img class=\"image\" id=\"")
    first = htmltoparse.find("src", start)
    last = htmltoparse.find("\"", first+5)

    download = ur.urlopen(htmltoparse[first+5:last])
    nome = str(i+1)
    nome = (nome.rjust(3, "0"))
    output = open(nome+".jpg","wb")
    output.write(download.read())
    output.close()
    print("Baixando o arquivo " + nome + ".jpg")

    start = htmltoparse.find("class=\"btn btn-default\" title=\"Next\"")
    nexturl = "http://www.imagebam.com" + htmltoparse[start-24:start-2]
    resource = ur.urlopen(nexturl)
print("Finalizado!")

