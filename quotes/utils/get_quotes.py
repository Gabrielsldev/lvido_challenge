import requests
import pandas as pd

from datetime import datetime


def get_quote():
    '''
    Gets today's quote from IMA-B 5
    '''

    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0"
    }

    # today = datetime.today().strftime('%d/%m/%Y')
    today = '26/08/2022'

    # URL for get request
    URL = f'https://www.anbima.com.br/pt_br/anbima/jsonima/acionar?dataInicio={today}&dataFim={today}'

    get_req = requests.get(URL, headers = headers)

    imab5_data = get_req.json()['IMA-B 5']

    df_imab5_data = pd.json_normalize(imab5_data)

    quote_imab5 = df_imab5_data['numero_indice'][0][-1]

    api_return = {"quote":quote_imab5, "date":today}

    return api_return