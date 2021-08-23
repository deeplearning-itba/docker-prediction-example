# Recomendaciones para trabajar

## LOCAL
### Crear entorno
```bash
conda create -n spacy-test python=3.7
conda activate spacy-test
pip install -r requirements.txt
```

### Correr app

```bash
cd app
flask run --host=0.0.0.0
```

### Testear API

```bash
curl --request GET http://localhost:5000/ 

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"instances": ["hola", "chau", "si "]}' \
  http://localhost:5000/api/v1/w2v
```

control+C para cortar la APP

## DOCKER

### Crear y correr docker
Desde la carpeta donde esta el Dockerfile ejecutar:

```bash
docker build --tag jganzabal/docker-test:v1 .

docker images
```

correrlo:

```bash
docker run -i -t -p 5000:5000 jganzabal/docker-test:v1
```

### Testear API
```bash
curl --request GET http://localhost:5000/ 

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"instances": ["hola", "chau", "si "]}' \
  http://localhost:5000/api/v1/w2v
```

### Pushearlo:
```bash
docker push jganzabal/docker-test:v1
```

Debería por bajarse ahora con 
```bash
docker pull jganzabal/docker-test
```


# UWSGI
Si quiere profundizar

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04

