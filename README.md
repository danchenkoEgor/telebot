1) Скачать репозиторий 

2) Открыть терминал и запустить docker 

3) Зайти в папку с файлами и ввести команду:

```sh
docker build
```

4) После построения образа ввести команду:

```sh
docker images 
```

5) Найти последний построенный образ и ввести команду:

```sh
docker run -d -p 80:80 <IMAGE ID>
```
	
6) Для приостановки образа: 
* Узнать в каком контейнере запущен образ:
```sh
docker ps
```

* Ввести команду:
	
```sh
docker stop <CONTAINER ID>
```