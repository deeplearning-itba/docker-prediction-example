# Build y push

flask run --host=0.0.0.0

## Desde la carpeta container

docker build --tag us-central1-docker.pkg.dev/infoxel-ml-ops/ml-ops-w2v/models-w2v:latest .

Probarlo:
docker run -i -t -p 5000:5000 us-central1-docker.pkg.dev/infoxel-ml-ops/ml-ops-w2v/models-w2v:latest 


Pushearlo:
docker push us-central1-docker.pkg.dev/infoxel-ml-ops/ml-ops-w2v/models-w2v:latest



https://cloud.google.com/artifact-registry/docs/docker/quickstart

docker tag models-w2v:latest us-central1-docker.pkg.dev/infoxel-ml-ops/ml-ops-w2v/models-w2v:latest

docker push us-central1-docker.pkg.dev/infoxel-ml-ops/ml-ops-w2v/models-w2v:latest

# Testearlo
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"instances": ["hola","chau","si"]}' \
  http://localhost:5000/api/v1/w2v


curl --request GET http://localhost:5000/ 