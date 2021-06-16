from defines import getCreds, makeApiCall

def getUserMedia( params ):
    endpointParams = dict()
    endpointParams['fields'] = 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username'
    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base'] + params['instagram_account_id'] + '/media'

    return makeApiCall( url, endpointParams, params['debug'] )

params = getCreds()
params['debug'] = 'yes'
response = getUserMedia(params)
