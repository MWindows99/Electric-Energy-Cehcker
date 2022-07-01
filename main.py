import requests

request_uri = 'http://agora.ex.nii.ac.jp/earthquake/201103-eastjapan/energy/electrical-japan/info.json'

def get_energy_info(place):
    response = requests.get(request_uri)
    if response.status_code == 200:
        json_data = response.json()
        place_info = {
            'kansai': json_data['kansai']['max_percent']
            'chugoku': json_data['chugoku']['max_percent']
            'tohoku': json_data['tohoku']['max_percent']
            'shikoku': json_data['shikoku']['max_percent']
            'kyushu': json_data['kyushu']['max_percent']
            'chubu': json_data['chubu']['max_percent']
            'tokyo': json_data['tokyo']['max_percent']
            'okinawa': json_data['okinawa']['max_percent']
            'hokkaido': json_data['hokkaido']['max_percent']
            'hokuriku': json_data['hokuriku']['max_percent']
        }
        percentage = place_info.get(place)
        return percentage
    else:
        return False
