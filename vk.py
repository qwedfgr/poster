import requests


def get_auth_params(token, group_id):
    version = 5.92
    params = {
        'access_token': token,
        'group_id': group_id,
        'v': version
    }
    return params


def post_image_and_text(image_path, text, token, group_id):
    auth_params = get_auth_params(token, group_id)
    upload_photo_params = upload_photo(auth_params, image_path)
    photo_params = save_wall_photo(auth_params, upload_photo_params)
    photo_id = get_photo_id(photo_params['response'][0])
    wall_post(auth_params, photo_id, text)


def wall_post(auth_params, photo_id, comment):
    url = 'https://api.vk.com/method/wall.post'
    params = auth_params
    params.update({
        'attachments': photo_id,
        'owner_id': '-{group_id}'.format(**params),
        'from_group': 1,
        'message': comment
    })
    response = requests.post(url=url, params=params)
    check_response(response)
    return response.json()


def get_photo_id(photo_params):
    return 'photo{owner_id}_{id}'.format(**photo_params)


def get_upload_url(auth_params):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    response = requests.get(url=url, params=auth_params)
    check_response(response)
    return response.json()['response']['upload_url']


def upload_photo(auth_params, image_path):
    api_host = get_upload_url(auth_params)
    params = auth_params
    with open(image_path, 'rb') as file:
        files = {'photo': file}
        response = requests.post(url=api_host, files=files, params=params)
        check_response(response)
    return response.json()


def save_wall_photo(auth_params, upload_photo_params):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = dict(auth_params, **upload_photo_params)
    response = requests.post(url=url, params=params)
    check_response(response)
    return response.json()


def check_response(response):
    response.raise_for_status()

    json_data = response.json()
    if 'error' in json_data:
        raise requests.exceptions.HTTPError(json_data['error'])
