#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys

url = 'https://discordapp.com/api/webhooks/586787055854419981/Dw35phuMwnCM4iVtOBW3QNusDdFtNP2-UpjFvpgpVl5S3Eetv_hMdfpBkKxQOTpuNPcB' #ここにWebhook用に取得したURLを入れる

if len(sys.argv) > 1:
    payload = {'content': sys.argv[1]}
    result = requests.post(url, data=payload)

#    if result.status_code != requests.codes.no_content:
        # 投稿に失敗したときの処理...