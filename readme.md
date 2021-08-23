# Recomendaciones para trabajar

## LOCAL
### Crear entorno

conda create -n spacy-test python=3.7
conda activate spacy-test
pip install -r requirements.txt

### Correr app
cd app

flask run --host=0.0.0.0

### Testear API
curl --request GET http://localhost:5000/ 

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"instances": ["hola", "chau", "si "]}' \
  http://localhost:5000/api/v1/w2v

control+C para cortar la APP

## DOCKER

### Crear y correr docker
Desde la carpeta donde esta el Dockerfile ejecutar:

docker build --tag jganzabal/docker-test:v1 .

docker images

correrlo:
docker run -i -t -p 5000:5000 jganzabal/docker-test:v1

### Testear API
curl --request GET http://localhost:5000/ 

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"instances": ["hola", "chau", "si "]}' \
  http://localhost:5000/api/v1/w2v


### Pushearlo:
docker push jganzabal/docker-test:v1

