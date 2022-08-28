# ANBIMA IMAB-5 API
###### Developed by Gabriel Sobreira Lopes
---

The goal is to build an API endpoint and scrapper to get Anbima's IMA-B 5 index.

The API will receive a GET request at `/api/v1/cota` and the output must be the day's date and the current value of the index.

```
[
  {
    "quote": 4955.994716,
    "date": "2022-08-19"
  }
]
```

> Data source: [Anbima IMA-B 5](https://www.anbima.com.br/pt_br/informar/precos-e-indices/indices/ima.htm#Laminas)

---
## Stack used:
- Python 3, Django, Docker.
- `Requests` and `Pandas` were used for scrapping and data handling.
---

## Instructions:
- Clone the repository to the desired directory.
- Run `sudo docker-compose up` and the application will start.
- Access the API endpoint locally: [API endpoint](http://localhost:8000/api/v1/cota)
  - Url: `localhost:8000/api/v1/cota`
- The tests can be found at `quotes/tests.py`.
  - To run the tests, run `python tests.py` inside the `quotes` folder.
---