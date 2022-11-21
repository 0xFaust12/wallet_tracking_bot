from blocknative.stream import Stream
import json
import datetime
import requests

TELEGRAM_TOKEN = '5769561073:AAEXINtPg02Qq9tD2TPWwL2Yi_Y8ZJSMPVU'

global_filters = [{
    'status': 'confirmed',
    'type': 2,
    'network': 'main'
}]

stream = Stream('f459b609-66e4-440f-9f4a-a08db79b115c', global_filters=global_filters)


def get_group_ids() -> list:
    """

    :return:
    """
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates'

    data = requests.post(url).json()['result']

    group_list = []

    for update in data:
        try:
            group_list.append(update['message']['chat']['id'])
        except KeyError:
            pass

    return list(set(group_list))


def tel_send_message(chat_id, input_json: json):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': input_json
    }

    r = requests.post(url, json=payload)

    return r


async def txn_handler(txn, unsubscribe):
    # This will only get called with transactions that have status of 'confirmed'
    # This is due to the global filter above

    # get list of chat ids here:
    for _id in get_group_ids():
        tel_send_message(chat_id=_id, input_json=json.dumps(txn))

        print(json.dumps(txn, indent=4))


if __name__ == '__main__':

    moin3au_address = '0x6611fe71c233e4e7510b2795c242c9a57790b376'
    shaw_address = '0x6f4a2d3a4f47f9c647d86c929755593911ee91ec'
    ben_nolan_address = '0x2d891ed45c4c3eab978513df4b92a35cf131d2e2'
    ape_123_address = '0xcc7c335f3365ae3f7e4e8c9535dc92780a4add9d'
    smart_influencer_address = '0xef6d69922bc2d038cb508086846524f8011c4a74'
    three_dg_address = '0xc480fb0ebea2591470f571436926785be5ebcd22'
    otis_address = '0x3612b2e93b49f6c797066ca8c38b7f522b32c7cb'
    shilpixels_address = '0xc24f574d6853f6f6a31c19d468a8c1b3f31c0e54'
    zonked_address = '0xebf02c6e12c3ee119abba161c40bfeead0a06b15'
    keyboard_money_address = '0xe1d29d0a39962a9a8d2a297ebe82e166f8b8ec18'
    pdx_address = '0xb53349160e38739b37e4bbfcf950ed26e26fcb41'
    pranksy_address = '0xd387a6e4e84a6c86bd90c158c6028a58cc8ac459'

    # Global filter will apply to all of these subscriptions
    stream.subscribe_address(moin3au_address, txn_handler)
    stream.subscribe_address(shaw_address, txn_handler)
    stream.subscribe_address(ben_nolan_address, txn_handler)
    stream.subscribe_address(ape_123_address, txn_handler)
    stream.subscribe_address(smart_influencer_address, txn_handler)
    stream.subscribe_address(three_dg_address, txn_handler)
    stream.subscribe_address(otis_address, txn_handler)
    stream.subscribe_address(shilpixels_address, txn_handler)
    stream.subscribe_address(zonked_address, txn_handler)
    stream.subscribe_address(keyboard_money_address, txn_handler)
    stream.subscribe_address(pdx_address, txn_handler)
    stream.subscribe_address(pranksy_address, txn_handler)

    # Start the websocket connection and start receiving events!
    stream.connect()
