# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:05:00 2020

@author: peishuo
"""

import os
import json
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import QA_Col
import random

app = Flask(__name__)


line_bot_api = LineBotApi(
    'hhl6WLNzN1yGeFCORGSYI6R01pVb5sqk/kU8h/T/upnYkfc6zwtvORa7udac8um0E6sSNScQriZTxSZF3qYoh4ge+OqafdaH4Nbl2IKCD7Np8bw4KeBUQhm8eMWNe7o8u0lDAMA8TWRylU+AsGCHRQdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('f72b22612a5bd49d398ada8e74cb0ab5')

line_bot_api.push_message('U0aeb28721a45f9e371e60c9b2b6babbe', TextSendMessage(
    text='系統測試中，若您覺得訊息干擾到您，您可以將聊天室設為靜音，謝謝喔！'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

######################處理LINE USER 傳來得訊息 ###############################


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user id when reply

    profile = line_bot_api.get_profile(event.source.user_id)
    nameid = profile.display_name  # 使用者名稱
    uid = profile.user_id  # 使用者ID
    user_message = str(event.message.text)

    # user_message='圖文訊息'
    if user_message.find('圖文訊息') != -1:

        res_message = TemplateSendMessage(
            alt_text='圖文訊息',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='文字訊息',
                                text='文字訊息'
                            ),
                            MessageTemplateAction(
                                label='圖片訊息',
                                text='圖片訊息'
                            ),
                            MessageTemplateAction(
                                label='影片訊息',
                                text='影片訊息'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='音訊訊息',
                                text='音訊訊息'
                            ),
                            MessageTemplateAction(
                                label='位置訊息',
                                text='位置訊息'
                            ),
                            MessageTemplateAction(
                                label='貼圖訊息',
                                text='貼圖訊息'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='按鈕介面訊息',
                                text='按鈕介面訊息'
                            ),
                            MessageTemplateAction(
                                label='確認介面訊息',
                                text='確認介面訊息'
                            ),
                            MessageTemplateAction(
                                label='輪播模板訊息',
                                text='輪播模板訊息'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='輪播圖模板訊息',
                                text='輪播圖模板訊息'
                            ),
                            URITemplateAction(
                                label='Line官方說明文件',
                                uri='https://developers.line.biz/zh-hant/docs/messaging-api/message-types/#common-features'
                            ),
                            MessageTemplateAction(
                                label='其他',
                                text='教材尚在開發中'
                            ),
                        ]
                    ),
                    # =============================================================================
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)
        return 0

###############################################################################
        # user_message='文字訊息'
    elif user_message.find('文字訊息') != -1:  # 判斷用戶使否傳來"文字訊息"關鍵字，若為是則觸發本區段。

        res_message = TextSendMessage(
            text='歡迎使用文藻E點通，您選擇的是文字測試訊息，您目前看到的是【文字訊息】的回覆方式。')
        line_bot_api.reply_message(event.reply_token, res_message)
        return 0

###############################################################################
    elif user_message.find('圖片訊息') != -1:  # 判斷用戶使否傳來"圖片訊息"關鍵字，若為是則觸發本區段。

        res_message = ImageSendMessage(
            original_content_url='https://cdn2.ettoday.net/images/3053/3053944.jpg',
            preview_image_url='https://cdn2.ettoday.net/images/3053/3053944.jpg'
        )
        line_bot_api.reply_message(event.reply_token, res_message)
        return 0

###############################################################################
        # user_message='影片訊息'
    elif user_message.find('影片訊息') != -1:  # 判斷用戶使否傳來"影片訊息"關鍵字，若為是則觸發本區段。

        res_message = VideoSendMessage(
            original_content_url='https://r5---sn-npoe7n7r.googlevideo.com/videoplayback?expire=1612879931&ei=20MiYIfkBIyWiwTEhrSQBQ&ip=144.202.56.145&id=o-ANCIwAp79OWJyLwTkkaRuKvMzGSf6gsljTB-wPAcLNh5&itag=22&source=youtube&requiressl=yes&vprv=1&mime=video%2Fmp4&ns=6LcWIDtZWbxjYUXS1Dod_vIF&ratebypass=yes&dur=328.423&lmt=1572331630804319&fvip=5&c=WEB&txp=2216222&n=fRjt_f_oTJeD95i&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAMXkWqUW9UIIMrcCJZ8dh_xZ7nWpUlNVWd4sdw2JHME4AiAKGxqLL5z6kL30RkfuW-mCUVIwWmqG1nPPOo0_PbecxA%3D%3D&redirect_counter=1&cm2rm=sn-vgqe7s76&req_id=3b1b213d3dba3ee&cms_redirect=yes&mh=ww&mip=182.234.79.223&mm=34&mn=sn-npoe7n7r&ms=ltu&mt=1612858827&mv=m&mvi=5&pl=18&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRAIgXT3f533nuXNJnQlehCh9ePDKFQtHpmkoWKAN1IzsJsgCIBtOmjBzv9DrdIWDtPjsHRSZXLCFcjAZN1zQSqWOHGEM',
            preview_image_url='https://lh3.googleusercontent.com/pw/ACtC-3fmvQXV2wh96fqQjSJ5KZXRUjprXHH9zG2EVFLuExV-Uxl1sN2AQ76RIN8Cy6A0COCT4FvQg9YRzqNujWkrxwA3kgGLcAOtsupqBi0JCqx4HUQuMqR8KMJ6CRQ7FBSJ3JLHfYv04V_BFmQAMFQIrWgvsg=w958-h539'
        )

        line_bot_api.reply_message(event.reply_token, res_message)
        return 0

###############################################################################
        # user_message='音訊訊息'
    elif user_message.find('音訊訊息') != -1:  # 判斷用戶使否傳來"音訊訊息"關鍵字，若為是則觸發本區段。

        res_message = message = AudioSendMessage(
            original_content_url='https://r5---sn-npoe7n7r.googlevideo.com/videoplayback?expire=1612879931&ei=20MiYIfkBIyWiwTEhrSQBQ&ip=144.202.56.145&id=o-ANCIwAp79OWJyLwTkkaRuKvMzGSf6gsljTB-wPAcLNh5&itag=140&source=youtube&requiressl=yes&vprv=1&mime=audio%2Fmp4&ns=vL6EbYMqRar6wkILnGFdM6sF&gir=yes&clen=5315836&otfp=1&dur=328.423&lmt=1572331593044296&fvip=5&keepalive=yes&c=WEB&txp=2211222&n=jinyYfcO0NUsfzO&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cotfp%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAL1zzZOOX4qwpMs5f8cTrPvw7OLcoFlrx7IoNt4qKE_jAiA7W2Xce4BnGqfOPsuzNGEVGudGIMhqHBb5d40qsKMjdQ%3D%3D&ratebypass=yes&redirect_counter=1&cm2rm=sn-vgqe7s76&req_id=a0e283de1a31a3ee&cms_redirect=yes&mh=ww&mip=182.234.79.223&mm=34&mn=sn-npoe7n7r&ms=ltu&mt=1612858105&mv=m&mvi=5&pl=18&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIhANHX1USrlIJC8IXts4LcHkOClswgQoSKtfv-bBU76R7VAiB8SAfZxTgonssKfxUs6FL8O8Q5wn5cnL2r_OSUuKtjRQ%3D%3D',
            duration=328000
        )

        line_bot_api.reply_message(event.reply_token, res_message)
        return 0

###############################################################################
        # user_message='位置訊息'
    elif user_message.find('位置訊息') != -1:  # 判斷用戶使否傳來"位置訊息"關鍵字，若為是則觸發本區段。

        res_message = LocationSendMessage(
            title='文藻外語大學',
            address='80793高雄市三民區民族一路900號',
            latitude=22.6704067,
            longitude=120.3191348
        )

        line_bot_api.reply_message(event.reply_token, res_message)
        return 0

###############################################################################
        # user_message='貼圖訊息'
    elif user_message.find('貼圖訊息') != -1:  # 判斷用戶使否傳來"貼圖訊息"關鍵字，若為是則觸發本區段。

        res_message = StickerSendMessage(
            package_id='11539',
            sticker_id='52114116'
        )

        line_bot_api.reply_message(event.reply_token, res_message)
        return 0

###############################################################################
        # user_message='按鈕介面訊息'
    elif user_message.find('按鈕介面訊息') != -1:  # 判斷用戶使否傳來"按鈕介面訊息"關鍵字，若為是則觸發本區段。

        res_message = TemplateSendMessage(
            alt_text='按鈕介面訊息',
            template=ButtonsTemplate(
                thumbnail_image_url='https://imgs.gvm.com.tw/upload/gallery/20210126/77456_01.png',
                title='按鈕介面訊息',
                text='此種訊息可以設定1~4個按鈕選項，並可以設定一張1.51:1尺寸的圖片。',
                actions=[
                    MessageTemplateAction(
                        label='測試訊息',
                        text='您剛剛點擊了【測試訊息】'
                    ),
                    URITemplateAction(
                        label='文藻首頁',
                        uri='https://a001.wzu.edu.tw/'
                    )
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)

        return 0

###############################################################################
        # user_message='確認介面訊息'
    elif user_message.find('確認介面訊息') != -1:  # 判斷用戶使否傳來"確認介面訊息"關鍵字，若為是則觸發本區段。

        res_message = TemplateSendMessage(
            alt_text='本訊息為【確認介面訊息】',
            template=ConfirmTemplate(
                text='您是否確認要離開本次對話？',
                actions=[
                    MessageTemplateAction(
                        label='是',
                        text='我要離開對話'
                    ),
                    MessageTemplateAction(
                        label='否',
                        text='圖文訊息'
                    )
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)

        return 0

###############################################################################
        # user_message='輪播模板訊息'
    elif user_message.find('輪播模板訊息') != -1:  # 判斷用戶使否傳來"輪播模板訊息"關鍵字，若為是則觸發本區段。

        res_message = TemplateSendMessage(
            alt_text='本訊息為【輪播模板訊息】',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://www.nups.ntnu.edu.tw/upfiles/univ-expo/%E5%8D%97%E9%83%A8/%E9%AB%98%E9%9B%84%E5%B8%82/%E6%8A%80%E5%B0%88%E6%A0%A1%E9%99%A2/%E6%96%87%E8%97%BB/%E6%96%87%E8%97%BB-pic04.jpg',
                        title='測試輪播模板訊息-1',
                        text='您可以在此輸入您要描述的文字。',
                        actions=[
                            MessageTemplateAction(
                                label='測試按鈕-1',
                                text='您剛剛點擊了【測試按鈕-1】'
                            ),
                            MessageTemplateAction(
                                label='測試按鈕-2',
                                text='您剛剛點擊了【測試按鈕-2】'
                            ),
                            URITemplateAction(
                                label='網頁示範-校務資訊系統',
                                uri='https://sso.wzu.edu.tw/Portal/login.htm'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.nups.ntnu.edu.tw/upfiles/univ-expo/%E5%8D%97%E9%83%A8/%E9%AB%98%E9%9B%84%E5%B8%82/%E6%8A%80%E5%B0%88%E6%A0%A1%E9%99%A2/%E6%96%87%E8%97%BB/%E6%96%87%E8%97%BB-pic02.jpg',
                        title='測試輪播模板訊息-2',
                        text='您可以在此輸入您要描述的文字。',
                        actions=[
                            MessageTemplateAction(
                                label='測試按鈕-3',
                                text='您剛剛點擊了【測試按鈕-3】'
                            ),
                            URITemplateAction(
                                label='網頁示範-雲端學園',
                                uri='https://elearning2.wzu.edu.tw/home.php'
                            ),
                            MessageTemplateAction(
                                label='測試按鈕-4',
                                text='您剛剛點擊了【測試按鈕-4】'
                            )
                        ]
                    )
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)

        return 0

###############################################################################
        # user_message='輪播圖模板訊息'
    elif user_message.find('輪播圖模板訊息') != -1:  # 判斷用戶使否傳來"輪播圖模板訊息"關鍵字，若為是則觸發本區段。

        res_message = TemplateSendMessage(
            alt_text='本訊息為【輪播圖模板訊息】',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://www.nups.ntnu.edu.tw/upfiles/univ-expo/%E5%8D%97%E9%83%A8/%E9%AB%98%E9%9B%84%E5%B8%82/%E6%8A%80%E5%B0%88%E6%A0%A1%E9%99%A2/%E6%96%87%E8%97%BB/%E6%96%87%E8%97%BB-pic04.jpg',
                        action=PostbackTemplateAction(
                            label='輪播圖一',
                            text='輪播圖一：您可以在此輸入您要描述的文字。',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://www.nups.ntnu.edu.tw/upfiles/univ-expo/%E5%8D%97%E9%83%A8/%E9%AB%98%E9%9B%84%E5%B8%82/%E6%8A%80%E5%B0%88%E6%A0%A1%E9%99%A2/%E6%96%87%E8%97%BB/%E6%96%87%E8%97%BB-pic02.jpg',
                        action=PostbackTemplateAction(
                            label='輪播圖二',
                            text='輪播圖二：您可以在此輸入您要描述的文字。',
                            data='action=buy&itemid=2'
                        )
                    )
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)

        return 0

###############################################################################
        # user_message='相關網頁->學術單位'
    # 判斷用戶使否傳來"相關網頁->學術單位"關鍵字，若為是則觸發本區段。
    elif user_message.find('相關網頁->學術單位') != -1:

        res_message = TemplateSendMessage(
            alt_text='相關網頁->學術單位',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='英國語文系',
                                uri='http://c021.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='翻譯系',
                                uri='http://c033.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='國際事務系',
                                uri='http://c030.wzu.edu.tw/'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='國際企業管理系',
                                uri='http://c031.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='英語教學中心',
                                uri='http://c043.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='法國語文系',
                                uri='http://c022.wzu.edu.tw/'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='德國語文系',
                                uri='http://c023.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='西班牙語文系',
                                uri='http://c024.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='日本語文系',
                                uri='http://c025.wzu.edu.tw/'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='外語教學系',
                                uri='http://c036.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='應用華語文系',
                                uri='http://c026.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='傳播藝術系',
                                uri='http://c032.wzu.edu.tw/'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='數位內容應用與管理系',
                                uri='http://c028.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='師資培育中心',
                                uri='http://c035.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='通識教育中心',
                                uri='http://c034.wzu.edu.tw/'
                            ),
                        ]
                    ),
                    # =============================================================================
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)
        return 0

###############################################################################
        # user_message='相關網頁->行政單位'
    # 判斷用戶使否傳來"相關網頁->行政單位"關鍵字，若為是則觸發本區段。
    elif user_message.find('相關網頁->行政單位') != -1:

        res_message = TemplateSendMessage(
            alt_text='相關網頁->行政單位',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='校長室',
                                uri='https://c001.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='副校長室',
                                uri='https://c002.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='秘書室',
                                uri='https://c008.wzu.edu.tw/'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='教務處',
                                uri='https://c003.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='學生事務處',
                                uri='https://c004.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='研究發展處',
                                uri='https://c016.wzu.edu.tw/'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='總務處',
                                uri='https://c005.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='國際暨兩岸合作處',
                                uri='https://c015.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='進修部',
                                uri='https://c007.wzu.edu.tw/'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='推廣部',
                                uri='https://c049.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='會計室',
                                uri='https://c010.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='人事室',
                                uri='https://c009.wzu.edu.tw/'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='圖書館',
                                uri='https://lib.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='資訊與教學科技中心',
                                uri='https://c013.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='教師發展中心',
                                uri='https://c014.wzu.edu.tw/'
                            ),
                        ]
                    ),
                    # =============================================================================
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)
        return 0

###############################################################################
        # user_message='相關網頁->常用網頁'
    # 判斷用戶使否傳來"相關網頁->常用網頁"關鍵字，若為是則觸發本區段。
    elif user_message.find('相關網頁->常用網頁') != -1:

        res_message = TemplateSendMessage(
            alt_text='相關網頁->常用網頁',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='常用網頁',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='校網首頁',
                                uri='https://a001.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='圖書館',
                                uri='https://lib.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='資訊服務入口網',
                                uri='https://sso.wzu.edu.tw/Portal/login.htm'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='常用網頁',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='雲端學園',
                                uri='http://elearning2.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='網路選課系統',
                                uri='https://info.wzu.edu.tw/choice/'
                            ),
                            URITemplateAction(
                                label='活動管理系統',
                                uri='http://ma.wzu.edu.tw/bin/home.php'
                            ),
                        ]
                    ),
                    # =============================================================================
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)
        return 0

###############################################################################
        # user_message='相關網頁'
    elif user_message.find('相關網頁') != -1:  # 判斷用戶使否傳來"相關網頁"關鍵字，若為是則觸發本區段。

        res_message = TemplateSendMessage(
            alt_text='相關網頁',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='請選擇您想查找的頁面',
                        text='請由下方選項中選出子分類！',
                        actions=[
                            MessageTemplateAction(
                                label='學術單位',
                                text='相關網頁->學術單位'
                            ),
                            MessageTemplateAction(
                                label='行政單位',
                                text='相關網頁->行政單位'
                            ),
                            MessageTemplateAction(
                                label='常用網頁',
                                text='相關網頁->常用網頁'
                            )
                        ]
                    ),
                    # =============================================================================
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)
        return 0

###############################################################################
    elif user_message.find('輪播圖') != -1:

        return 0
###############################################################################
    elif user_message.find('您剛剛點擊了') != -1:

        return 0
###############################################################################
    elif user_message.find('教材尚在開發中') != -1:

        return 0
###############################################################################
    elif user_message.find('我要離開對話') != -1:
        response = '好的，期待您下次的呼喚，再見！'
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(response))

        return 0


###############################################################################
# QAsection start
###############################################################################
    # QA主選單
    elif user_message.find('QA') != -1:

        res_message = TemplateSendMessage(
            alt_text='歡迎光臨 Zao Coffee',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3eSgOf643kIOlRZNxwC4_uzxig16p8eLQZepeRwluGRk-nMOpyqgaV-bQLgwMQCLAcr7PEepULqnXvgfR224HDXWZ0GgTjyIVrfoUEIFV-LfbWugGQHBgI5mQHHSDKJ9cD0GZYo9SwSNuTKLBoUM3Zu=w1262-h881-no?authuser=0',
                        title='請問有什麼地方可以為您服務的嗎?',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='關於藻咖啡',
                                text='關於藻咖啡'
                            ),
                            MessageTemplateAction(
                                label='看看菜單',
                                text='看看菜單'
                            ),
                            MessageTemplateAction(
                                label='立即訂位',
                                text='立即訂位'
                            ),                            
                        ]
                    ),
                    # =============================================================================
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)
        return 0
        
###############################################################################
    # 關於藻咖啡次選單
    elif user_message.find('關於藻咖啡') != -1:

        res_message = TemplateSendMessage(
            alt_text='關於藻咖啡',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3dJczDs5FyidldjRQnyJLIRr2P6iuT1598rAOdKrg_9vks2pTHBcsQviEBDH8-mGcm_boFRV_g-H2lZbTtXoJRrnDX9FKwEW29WjrpsOvn9-bF_wuyPoOIkFZG6DwB00uuaL0KvfJI1eoogQR7mqF1F=w1322-h881-no?authuser=0',
                        title='藻咖啡',
                        text='提供舒適的環境、安心食材。',
                        actions=[
                            MessageTemplateAction(
                                label='店內環境',
                                text='店內環境'
                            ),
                            MessageTemplateAction(
                                label='看看菜單',
                                text='看看菜單'
                            ),
                        ]
                    ),
                    # =============================================================================
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)
        return 0
        
###############################################################################
    # 店內環境 圖+標題
    elif user_message.find('店內環境') != -1:

        res_message = TemplateSendMessage(
            alt_text='店內環境',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3cDzKbCPSDJ_ZCajYL49Hrj7DDNveYDptOGh_GiKKyvVlhOqG5uTsHNURZjAYY7KH7TikO9xWizPEvEmXzoG7CqsW2zfcBXy9CujNrFqnWRkMneLrA2jHoPinweGcEcrsdONf3uAA4FfXGOWvpTImtE=w1322-h881-no?authuser=0',
                        title='寬敞桌面',
                        text='內用區提供許多插座，讓你可以悠閒的喝杯咖啡做自己的事情',
                        actions=[
                            MessageTemplateAction(
                                label='',
                                text=''
                            ),
                        ]                        
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3cIM5qNLW47CuySyVxAiY37Uuc2KDTybTOHXg3bh4mE3ekNiJ9tvTuyzp96j8FQLr08r6iyUdW8gnyF6wD_bDfhl_-EDcsMfpbjusWZ0tK_rPV4s86N1iWTCsmn0rmfv-Cj-PMG_Ay5IbypRjXvmhJV=w1175-h881-no?authuser=0',
                        title='溫馨氣氛',
                        text='精心設計的內部裝潢給妳溫馨的氣氛度過一整天。',
                        actions=[
                            MessageTemplateAction(
                                label='',
                                text=''
                            ),
                        ]                            
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3fkAZpb2VtIn3pQLuqhvgQeELdFW4nZ3sNH7YKhCHuNPQGcVoGWZHc2jQ0vDr_2_kqAXnbTlwengVVdBYgcT-Tyf_TcYjiM1-9KHI9aTbVKKGgXMHaxDuAfM92RHmhT5zy_rq9cilgHFo3pN8oBmQuS=w1334-h882-no?authuser=0',
                        title='簡潔環境',
                        text='簡化生活上的繁瑣，帶給你不同看待生活的方式',
                        actions=[
                            MessageTemplateAction(
                                label='',
                                text=''
                            ),
                        ]                            
                    ),             
                    # =============================================================================
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)

        return 0

###############################################################################
    # 看看菜單 圖+選擇
    elif user_message.find('看看菜單') != -1:

        res_message = TemplateSendMessage(
            alt_text='看看菜單',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3erhuBjVXhel4y6yA1C1D0IjgJcdpnmGzXgcSn6fDneB45ReYFEHZEVS3QDd7-gdS2veVVcG8nR3bzCirJ4f0ixCsS1rvSFj0un8zmLayttpZcDADx0D0u0fPzCnLHzQ0BbuWRmZMU4xCAq-vxpXmrV=w1102-h881-no?authuser=0',
                        title='咖啡類',
                        text='精品手工咖啡',
                        actions=[
                            MessageTemplateAction(
                                label='看看咖啡菜單',
                                text='看看咖啡菜單'
                            ),
                        ]                        
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3cRdI4bWrWn9OWla6J_aV0Em5bkfHZRDPJW01fCzYqN9HxbXkuVNLst3qfWbep2gvrl0yTtD83iNzlIN6XD8HntwnjKgm5aNgvBiMr9Ez-xXByNSOD4mxzNS0eTg-GP5V2ckrEtpaGrhWqMbf2uOrVy=w1419-h881-no?authuser=0',
                        title='果汁類',
                        text='果汁特調',
                        actions=[
                            MessageTemplateAction(
                                label='看看果汁菜單',
                                text='看看果汁菜單'
                            ),
                        ]                        
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3fs_gKwwubXrSxZX2PL-fO8s250hWd0GUz626v1fx4mp3DNQTZZHv3oukP3RGQ0RnUQISUatjcSy0jfhPor10aJ6zm3dC8iCAwNno00PyljXJ4CuKrs-U0DhTnv-dn_4FYi8MVGt7HqSBG-_4AoHUGg=w1541-h881-no?authuser=0',
                        title='甜點類',
                        text='下午茶輕食',
                        actions=[
                            MessageTemplateAction(
                                label='看看甜點菜單',
                                text='看看甜點菜單'
                            ),
                        ]                        
                    ),                                    
                    # =============================================================================
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)

        return 0

###############################################################################
    # 看看咖啡菜單 圖+標題
    elif user_message.find('看看咖啡菜單') != -1:

        res_message = TemplateSendMessage(
            alt_text='看看咖啡菜單',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3cH60McsBbJympAfwSisoSwoU7w1c0EYKgg1_8HF5qM7K8VopQPFoKjqQiZ7Y_OXuMKC4M0lvB2RrcgBELTtWcKNRb1iREPk0fhRnbY9-aTHc67u4fpMclfWCHNcAZYWhrskDgcoz1_dWLRz-lMimrU=w1322-h881-no?authuser=0',
                        title='美式黑咖啡',
                        text='冰/熱 NT$ 110',
                        actions=[
                            MessageTemplateAction(
                                label='',
                                text=''
                            ),
                        ]   
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3fE6LowEQ1H-2PvIYslUpMvxny5ESML890w29Egc66AnXKURoPBuZO7lN7qUAJ-DmJrb22OnYCM9G3g0Cvz7s-p75yXL4x8n7LYp68mVidYIB64E_6dIrWaU0N0WqIS554fIMu7gWaubymv3pK6WEWI=w1322-h882-no?authuser=0',
                        title='拿鐵咖啡',
                        text='冰/熱 NT$ 140',
                        actions=[
                            MessageTemplateAction(
                                label='',
                                text=''
                            ),
                        ]   
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3c9tBJdawbOtyfAKEKfZj0NCy49E-Lb88ZmF0Y_NqrrZL_JLYnELa4fvds52W1AgYlI0pBCvJglrH__ewOq88I0HJQGdEU0-IYjqepeVxf6XUgWFLu8gpoX6mIQObE2oE2ZS-0DsO7cjE3LcRMZxPQo=w1226-h881-no?authuser=0',
                        title='焦糖瑪奇朵',
                        text='冰/熱 NT$ 160',
                        actions=[
                            MessageTemplateAction(
                                label='',
                                text=''
                            ),
                        ]   
                    ),                                      
                    # =============================================================================
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)

        return 0
        
###############################################################################
    # 看看果汁菜單 圖+標題
    elif user_message.find('看看果汁菜單') != -1:

        res_message = TemplateSendMessage(
            alt_text='看看果汁菜單',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3cRbnNSKT0cNwjJFvKTs69Vyjnhd6UshI8yUmvmcgiJoLBSFkqbu642xG_lzg6y8SsHnBSgTrEJZqJGCq_bCcEi6egFWGraM4j7XarQMMWUfC9f5hlh2uVx1CFaIonQiR5jo4ZPHvP4rnndi42Dsr6l=w1322-h881-no?authuser=0',
                        title='鮮草莓牛奶',
                        text='冰 NT$ 120',
                        actions=[
                            MessageTemplateAction(
                                label='',
                                text=''
                            ),
                        ]   
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3fyNH7AxPFSRwPL3ODeHltevTW0JVMQIS4EXYjh2_7WrC6SEGtcD0-zO3Fe9fw1u1rfg1LkXHrJijQQ84qahHUx2MIt5c-fjScTJzTnfoKKyjlpUfYEaiQ9Bbax3wfwp6qdqCYtKD1u_2pdZI-KunVK=w1322-h882-no?authuser=0',
                        title='蘋果蘇打',
                        text='冰 NT$ 100',
                        actions=[
                            MessageTemplateAction(
                                label='',
                                text=''
                            ),
                        ]   
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3egd4uanIt6MeVyviSOnpQBG70yFOHz1nwK2qojtnHQYIDv2I1NMyKkK5BGtHRfA2anySvEzIwKOUKHJpWkJXez1NkvITZMxzp7hpJ1i6HNuOBEJHQ1lRhsXvtJ3t_T8wYN8cyz5loke7j163K_miT4=w1322-h881-no?authuser=0',
                        title='葡萄香檳',
                        text='冰 NT$ 140',
                        actions=[
                            MessageTemplateAction(
                                label='',
                                text=''
                            ),
                        ]   
                    ),                                      
                    # =============================================================================
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)

        return 0

###############################################################################
    # 看看甜點菜單 圖+標題
    elif user_message.find('看看甜點菜單') != -1:

        res_message = TemplateSendMessage(
            alt_text='看看甜點菜單',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3cGz84PikMg1eds-6rUlWIOonBiuxJQ1tYYdUNkhvhFcZo4a0bGjU_qw19XClEk-gLAoZ8UVoOQRwQyicgHiWvquoych899nCNClJWwzSpNgFpnX1uHb1eRSsGFwc9UeyR-45rCVYJMsi2-HnkFeK40=w1322-h881-no?authuser=0',
                        title='重乳酪蛋糕',
                        text='NT$ 80',
                        actions=[
                            MessageTemplateAction(
                                label='',
                                text=''
                            ),
                        ]   
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3doRdXaRT0U9rTm7OkCLmud1FLZbtozMheA9_-bj-YTk9qoXrlrKo6qqJvfFyDBaRdh6rjR7MnpfL4mBAAvhTv34sH--O2Jl8x_Wl9ZHhbsLpQvqZe4NzhntcufD4zFyJtbCx_U6Hz1u277WAQBmmU3=w1326-h882-no?authuser=0',
                        title='布朗尼',
                        text='NT$ 60',
                        actions=[
                            MessageTemplateAction(
                                label='',
                                text=''
                            ),
                        ]   
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.googleusercontent.com/pw/ACtC-3fPJaC-esphfrLd3p3GVbd_JGuP5mqgfrKQOGtKmRm-OihMdux8NdDD_qRZPe8etvAimXwS1lDQJjIwW2tGqM6DGpcp8zptai2r-tfZFMAcJO8k285nJbWWrMgRT5LpT7uEm4TtzXh9P3VBiAKOkby9=w1175-h881-no?authuser=0',
                        title='莓果鬆餅',
                        text='NT$ 100',
                        actions=[
                            MessageTemplateAction(
                                label='',
                                text=''
                            ),
                        ]   
                    ),                                      
                    # =============================================================================
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)

        return 0

###############################################################################
# QAsection end
###############################################################################


###############################################################################
    else:
        response = '我不太了解您的意思，建議您透過選單與我互動唷！'
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(response))
        return 0

    # user_id = event.source.user_id
    # print("user_id =", user_id)

    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text))


###############################################################################

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 27017))
    app.run(host='0.0.0.0', port=port)
if __name__ == "__main__":
    app.run()
