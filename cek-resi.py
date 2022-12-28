import json
import requests 

def cek_resi_sicepat(resi):
    url = 'https://content-main-api-production.sicepat.com/public/check-awb/%20' + resi

    r = requests.get(url)

    if r.status_code != 200:
        print(f'Resi {resi} not found!')
        return

    data = json.loads(r.content)
    track_history = data['sicepat']['result']['track_history']

    for tracked in track_history:
        datetime = tracked['date_time']
        status = tracked['status']
        city = tracked['city']
        print(f'Datetime : {datetime}')
        print(f'Status   : {status}')
        print(f'City     : {city}')
        print('------------------------------------------------------------------')
    print('Done :)')

if __name__ == '__main__':
    resi = str(input('Input resi : '))
    cek_resi_sicepat(resi) 
