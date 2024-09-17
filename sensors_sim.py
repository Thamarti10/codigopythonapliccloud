import time
import random
import requests

def simulate_interaction():
    product_id = random.randint(1, 10)  # Simula um ID de produto
    client_id = random.randint(1, 5)  # Simula um ID de cliente
    quantity = random.randint(1, 3)  # Simula uma quantidade comprada

    sale_data = {
        'client_id': client_id,
        'product_id': product_id,
        'quantity': quantity
    }

    response = requests.post('http://localhost:5000/register_sale', json=sale_data)

    if response.status_code == 201:
        print('Venda simulada com sucesso.')
    else:
        print(f'Erro ao simular venda: {response.json()}')

if __name__ == '__main__':
    while True:
        simulate_interaction()
        time.sleep(5)  # Simula interações a cada 5 segundos
