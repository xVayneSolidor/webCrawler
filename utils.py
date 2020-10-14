import os

#Este util maneja la parte de los archivos que contendran las URLs y el archivo que tendra los resultados de la busqueda
#Ademas este archivo results funciona para que no se busquen de nuevo las paginas ya visitadas

#Se crea el directorio para que se guarden los archivos de los URLs
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)

#Se crean los archivos que se van a buscar y se ira guardando en el archivo de resultados
#El archivo pool contiene las paginas web a las que se haran scrapping
#results.txt va guardando estas paginas para que no se busquen de nuevo
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'urlpool.txt')
    crawled = os.path.join(project_name,"results.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#Se crea un nuevo archivo
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)

#Se llena el archivo que se creo
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

#Remueve los contenidos de un archivo
def delete_file_contents(path):
    open(path, 'w').close()

#Lee el archivo y va poniendo cada item en una linea
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

#Se itera cada linea del archivo
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")