import shodan
def keyInformation(shodanApi):
    try:
        info = shodanApi.info()
        for inf in info:
            print('%s: %s' %(inf, info [inf]))
    except shodan.APIError as e:
        print('Error: %s' % e)

def shodanTest():
    try:
        shodanKeyString = input("API-KEY")
        shodanAPI = shodan.Shodan(shodanKeyString)
        print("Info de la API")
        query = input('Introduce la busqueda que quieres realizar, p.e apache: ')
        results = shodanAPI.search(query)
        print('Número total de resultados: {}'.format(results['total']))
        #Obtención de por ejemplo 5 resultados por consulta
        for result in list(results['matches'])[1:5]:
            print('IP: %s' % result['ip_str'])
            print(result['data'])

    except shodan.APIError as e:
        print('Error: %s' % e)
if __name__ == "__main__":
    shodanTest()