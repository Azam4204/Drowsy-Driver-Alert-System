import requests
import json

def send_telegram_message(message,
                          chat_id,
                          api_key,
                          proxy_username = None,
                          proxy_password = None,
		  proxy_url: str = None):
    responses = {}

    proxies = None
    if proxy_url is not None:
        proxies = {
            'https': f'http://{username}:{password}@{proxy_url}',
            'http': f'http://{username}:{password}@{proxy_url}'
        }
        headers = {'Content-Type': 'application/json',
                   'Proxy-Authorization': 'Basic base64'}
        data_dict = {'chat_id': chat_id,
                     'text': message,
                     'parse_mode': 'HTML',
                     'disable_notification': True}
        data = json.dumps(data_dict)
    else:
        
        url = f'https://api.telegram.org/bot{api_key}/sendMessage'
        response = requests.post(url, json = {'chat_id':chat_id,'text':message})

    return response

msg = ""
chatid = "888925166"
api_to_get_updates = "https://api.telegram.org/bot5532916864:AAEhdpRfnzCshxTBNYqINZ31mDOTxvBXB6k/getUpdates"
apiKey = "5532916864:AAEhdpRfnzCshxTBNYqINZ31mDOTxvBXB6k"
send_telegram_message(msg,chatid,apiKey)