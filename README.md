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
&#8594; merge env variables from both "colud_api" and "evento" to the single .env file and place it in the same directory as docker-copmose.yml
</br></br>
```
docker-copmose up
```