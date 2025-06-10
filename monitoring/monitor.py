import requests
import time
import logging

logging.basicConfig(
    filename='monitor.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

SERVICES = {
    'Frontend': 'http://frontend',
    'Backend': 'http://backend/api/products',
    'Order Service': 'http://orders/orders'
}

def check_service(name, url):
    try:
        response = requests.get(url if name != 'Order Service' else url.replace('/orders', ''), timeout=3)
        return response.status_code == 200
    except:
        return False

while True:
    status = {}
    for name, url in SERVICES.items():
        is_ok = check_service(name, url)
        status[name] = 'OK' if is_ok else 'DOWN'
        if not is_ok:
            logging.error(f'{name} is DOWN')
    
    print('\n' + '='*20)
    for name, stat in status.items():
        print(f'{name}: {stat}')
    print('='*20 + '\n')
    
    time.sleep(5)