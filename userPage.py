from defines import getCreds, makeApiCall

def getUserPages( params ):
    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base'] + 'me/accounts'

    return makeApiCall(url, endpointParams, params['debug'])


params = getCreds()
params['debug'] = 'no'
response = getUserPages( params )

print("\n---- FACEBOOK PAGE INFO ----\n")
print("Page name: ")
print(response['json_data']['data'][0]['name'])
print("Page category: ")
print(response['json_data']['data'][0]['category'])
print("Page Id: ")
print(response['json_data']['data'][0]['id'])
