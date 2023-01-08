import httpx

base_currency = input('digite a moeda base: ').upper()
currency = input('Digite a moeda desejada: ').upper()

#Busca valores em api pública
response = httpx.get(
    url = f'https://api.exchangerate.host/lastest?base={base_currency}'
).json()
currency_data = response['rates']

print(f'1 {base_currency} vale {currency_data.get(currency)} {currency}')
