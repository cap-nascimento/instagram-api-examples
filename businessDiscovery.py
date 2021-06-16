from defines import getCreds, makeApiCall

def getAccountInfo( params ):
    endpointParams = dict()
    endpointParams['fields'] = 'business_discovery.username('+ params['ig_username'] +'){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}'
    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base'] + params['instagram_account_id']

    return makeApiCall( url, endpointParams, params['debug'] )

params = getCreds()
params['debug'] = 'yes'
response = getAccountInfo( params )
