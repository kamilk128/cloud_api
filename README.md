# cloud api

```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

.env.example -> .env + password
</br>
http://localhost:8000/docs

# docker compose

&#8594; expose docker-compose.yml to the parent directory with the "[colud_api](https://github.com/kamilk128/cloud_api)" and "[evento](https://github.com/KRQPLY/evento/tree/cloud-develop)" repositories
</br></br>
&#8594; merge env variables from both "colud_api" and "evento" to the single .env file and place it in the same directory as docker-compose.yml
</br></br>

```
docker-compose up
```

# kubernetes

&#8594; https://minikube.sigs.k8s.io/docs/start/

```
minikube start
```

alternative:

```
minikube start --driver docker
```

&#8594; download local docker images to minikube (docker images were created in the previous section "cloud_api" and "evento_frontend"):

```
minikube image load cloud_api
minikube image load evento_frontend
```

&#8594; before creating secret from the .env file, remove all spaces from it!!

&#8594; api:

```
kubectl create secret generic mysecrets --from-env-file=.env
kubectl apply -f api-pod.yaml
kubectl apply -f api-service.yaml
```

&#8594; evento frontend:

```
kubectl create secret generic mysecrets-frontend --from-env-file=.env
kubectl apply -f evento-pod.yaml
kubectl apply -f evento-service.yaml
```

should work on nodePort under:

```
minikube ip
```

if not:

```
kubectl port-forward service/api-service 8000:8000
kubectl port-forward service/evento-service 8080:8080
```

alternative (random port):

```
minikube service api-service
minikube service evento-service
```
