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
            alt_text='您有什麼問題想要詢問呢?',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='您有什麼問題想要詢問呢?',
                        text='請由下方選出您想詢問的處室！',
                        actions=[
                            MessageTemplateAction(
                                label='教務處',
                                text='教務處'
                            ),
                            MessageTemplateAction(
                                label='學生事務處',
                                text='學生事務處'
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
    # 教務處組別次選單
    elif user_message.find('教務處') != -1:

        res_message = TemplateSendMessage(
            alt_text='教務處',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處組別選擇',
                        text='請由下方選出您想詢問的組別！',
                        actions=[
                            MessageTemplateAction(
                                label='註冊組',
                                text='註冊組'
                            ),
                            MessageTemplateAction(
                                label='課務組',
                                text='課務組'
                            ),
                            MessageTemplateAction(
                                label='英/外語能力診斷輔導中心',
                                text='英/外語能力診斷輔導中心'
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
    # 學務處組別次選單
    elif user_message.find('學生事務處') != -1:

        res_message = TemplateSendMessage(
            alt_text='學生事務處',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學生事務處組別選擇',
                        text='請由下方選出您想詢問的組別！',
                        actions=[
                            MessageTemplateAction(
                                label='軍訓室',
                                text='軍訓室'
                            ),
                            MessageTemplateAction(
                                label='生活輔導組',
                                text='生活輔導組'
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
    # 教務處註冊組問題分類選單
    elif user_message.find('註冊組') != -1:

        res_message = TemplateSendMessage(
            alt_text='註冊組',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組問題分類',
                        text='請由下方選出您想詢問的問題種類！',
                        actions=[
                            MessageTemplateAction(
                                label='註冊 Registration',
                                text='註冊'
                            ),
                            MessageTemplateAction(
                                label='學籍變更 Change of Student Status',
                                text='學籍變更'
                            ),
                            MessageTemplateAction(
                                label='證明文件申請 Application of Documents',
                                text='證明文件申請'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組問題分類',
                        text='請由下方選出您想詢問的問題種類！',
                        actions=[
                            MessageTemplateAction(
                                label='輔系、雙主修及學程 Minor,Double Major and Program',
                                text='輔系、雙主修及學程'
                            ),
                            MessageTemplateAction(
                                label='學分、成績 Credits, Grades',
                                text='學分、成績'
                            ),
                            MessageTemplateAction(
                                label='畢業 Graduation',
                                text='畢業'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組問題分類',
                        text='請由下方選出您想詢問的問題種類！',
                        actions=[
                            MessageTemplateAction(
                                label='其他問題 Other Questions',
                                text='其他問題'
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
    # 教務處註冊組-註冊類問答選單
    elif user_message.find('註冊') != -1:

        res_message = TemplateSendMessage(
            alt_text='註冊',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組-註冊類問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='開學前仍未收到註冊單，如何申請補發？',
                                text='若於開學註冊截止日前仍未收到註冊繳費單，可自行登入資訊服務系統補列印繳費單使用，或親至會計室（至善樓12樓）申請補發。\n資訊服務入口網站：https://sso.wzu.edu.tw/Portal/login.htm'
                            ),
                            MessageTemplateAction(
                                label='我是五專新生，請問新生基本資料表、住宿申請表這兩張表要在哪裡下載呢？',
                                text='「新生基本資料表」與「住宿申請表」皆須由資訊服務入口網登入校務系統，登錄資料後列印，於新生註冊須知均有操作說明。\n資訊服務入口網站：https://sso.wzu.edu.tw/Portal/login.htm'
                            ),
                            MessageTemplateAction(
                                label='我是新生，登入資源服務入口網需要學號，那我要怎麼知道學號呢？',
                                text='學號查詢請由資訊服務入口網登入頁面查詢。\n資訊服務入口網站：https://sso.wzu.edu.tw/Portal/login.htm'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組-註冊類問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='開學註冊後，何時繳回學生證註記註冊章？',
                                text='自105學年度起學生證免蓋註冊章，請學生自行列印學生證正反面影印本並攜帶學生證正本，註冊組查驗後會加蓋"與正本無訛章"或"註冊組單位章"。'
                            ),
                            MessageTemplateAction(
                                label='如何申請繳費證明？',
                                text='如是信用卡或ATM轉帳繳費，可自行登入學校網頁的資訊服務入口網下載列印繳費證明；如是辦理就學貸款，則需親至會計室(至善樓12樓)申請。'
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
    # 教務處註冊組-學籍變更類問答選單
    elif user_message.find('學籍變更') != -1:

        res_message = TemplateSendMessage(
            alt_text='學籍變更',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組-學籍變更類問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='校友更改學籍資料（姓名、身分證字號或出生年月日）需準備哪些文件？',
                                text='暫無資料，請至教務處註冊組洽詢'
                            ),
                            MessageTemplateAction(
                                label='我已經搬家，要更改戶籍地址。我還沒有到戶政機關辦理戶籍更改，但是我想要先更改學校的資料，以方便寄註冊單。請問可以嗎?',
                                text='更改戶籍地需檢附戶籍謄本正本及身分證影本，煩請辦理完相關手續再申請更改。'
                            ),
                            MessageTemplateAction(
                                label='在校生更改學籍資料（姓名、身分證字號或出生年月日）需準備哪些文件？',
                                text='在校生申請變更上述學籍資料，請備妥下列文件，並填寫「文藻外語大學更改學籍資料申請書」，至註冊組辦理。 \n(1) 身分證影本\n(2) 戶籍謄本正本\n(3) 學生證(如需換照片請備2吋照片1張，背面填寫學號及新姓名)\n(4) 200元（換發新學生證費用）'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組-學籍變更類問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='在校生如何變更資料寄送地址、戶籍地址或監護人姓名？',
                                text='在校生如欲變更資料寄送地址、戶籍地址或監護人姓名，請填寫填寫「文藻外語大學更改學籍資料申請書」，並請家長簽名後，交至註冊組辦理，必要時請攜身分證明文件備查。'
                            ),
                            MessageTemplateAction(
                                label='在校生如何更改個人通訊資料或銀行帳號資料？',
                                text='在校生如欲變更個人通訊資料（通訊地址、聯絡電話及手機號碼等）或銀行帳號資料，請直接登錄資訊服務系統修改：登入－教務登錄作業－個人通訊資料及銀行帳號維護。\n資訊服務入口網站：https://sso.wzu.edu.tw/Portal/login.htm'
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
    # 教務處註冊組-證明文件申請類問答選單
    elif user_message.find('證明文件申請') != -1:

        res_message = TemplateSendMessage(
            alt_text='證明文件申請',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組-證明文件申請類問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='我看網站上寫「欲英文學位證書影本，需備有正本查驗」若是要郵寄申請的話，如何辦理？',
                                text='請把學位證書正本+文件申請表+郵政匯票(抬頭:文藻學校財團法人文藻外語大學)+貼足額回郵信封(B4以上)一同寄至註冊組，待我們處理完成再將資料寄回給您查收。'
                            ),
                            MessageTemplateAction(
                                label='遺失學生證如何申請補發？',
                                text='學生證遺失如欲申請補發，請至教務處註冊組網頁-掛失數位學生證，再至成績列印自動化繳費系統機申請補發,持申辦聯至註冊組辦理(如欲更換照片請備2吋照片1張，背面填寫學號及姓名)。'
                            ),
                            MessageTemplateAction(
                                label='校友如何申請成績單或其他各類證明書？',
                                text='校友如欲申請各類證明文件，請攜身分證件親至註冊組填寫「文藻外語大學各類證明文件申請表」，如委託他人代辦，需另附上本人填寫之委託書。\n若以郵寄方式申請，請將下列資料備齊後郵寄至註冊組辦理。\n(1) 各類證明文件申請表(註冊組→表單下載→文件申請→文藻外語大學各類證明文件申請表)\n(2) 文件費用郵政匯票（抬頭：文藻學校財團法人文藻外語大學）\n(3) 足額回郵信封\n其他申請注意事項詳見申請表下方附註說明。'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組-證明文件申請類問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='如何申請成績單或其他證明文件？',
                                text='(1)請攜學生證或其他身分證件親至註冊組填寫「文藻外語大學各類證明文件申請表」，如委託他人代辦，需另附上本人填寫之委託書。\n(2)至成績列印自動化繳費系統機申請列印,部份文件申請後需持申辦聯至註冊組臨櫃辦理。'
                            ),
                            MessageTemplateAction(
                                label='101學年度以後入學學生如何辦理ISIC國際學生證？',
                                text='辦理ISIC國際學生證可透過以下管道申請：\n(1) 「康文文教基金會」網站線上申請。\n(2) 「康文文教基金會」高雄辦事處申請－「鋼友旅行社」（地址：高雄市前金區中華四路282號3樓，電話：07-2158999）。\n(3) 全國各遊學代辦中心皆可代為申請。'
                            ),
                            MessageTemplateAction(
                                label='校友學位（畢業）證書遺失，如何申請補發畢業證明書？',
                                text='申請補發請備妥下列文件，並填寫「文藻外語大學補發中文學位（畢業）證明書申請書」，至註冊組辦理。\n(1)身分證正反面影印本 \n(2) 處理費200元\n(3) 戶籍謄本正本(若有更改姓名)\n若以郵寄方式申請，請將下列文件備齊後掛號郵寄至註冊組辦理。\n(1) 補發中文學位（畢業）證明書申請書\n(2) 身分證正反面影印本\n(3) 戶籍謄本正本(若有更改姓名)\n(4) 處理費200元郵政匯票（抬頭：文藻學校財團法人文藻外語大學）\n(5) 雙掛號46元大型(B4以上)回郵信封'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組-證明文件申請類問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='如果學生證遺失，但暑假期間急著要用，能不能回學校辦個臨時學生證之類的應急用，或者暑假期間有沒有相關的老師可以幫忙辦理呢？',
                                text='暑假期間仍可返校申辦學生證遺失補發，請持身分證明文件於週一至週五上午08:30-12:00；13:10-16:30至教務處註冊組辦理(如欲更換照片請備2吋照片1張，備免填寫學號及姓名)，補發期間可先申請"在學證明書"證明在學生身分。'
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
    # 教務處註冊組-輔系、雙主修及學程類問答選單
    elif user_message.find('輔系、雙主修及學程') != -1:

        res_message = TemplateSendMessage(
            alt_text='輔系、雙主修及學程',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組-輔系、雙主修及學程類問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='請問二技的學生可申請學程嗎？',
                                text='自98學年度第1學期可開始申請學程，申請時間請參考行事曆。\n1.請詳閱修讀輔系、雙主修及學程規定與資格，相關辦法公告於課務組網頁/相關法規。\n2.請依公告時間，上網線上申請。'
                            ),
                            MessageTemplateAction(
                                label='請問修讀輔系雙主修的學生，必修跟選修的學分是分開算，還是只要加起來有修到規定的學分數就好了，而不需要特別去算必選修各幾學分。',
                                text='輔系雙主修應修科目分有必修與選修兩種，需依規定修習方得取得資格，相關資料請參閱課務組網頁科目學分表。\n科目學分表：https://d002.wzu.edu.tw/category/136250'
                            ),
                            MessageTemplateAction(
                                label='請問申請輔系需要的成績單要怎麼向教務處申請？要本人到教務處嗎？',
                                text='本人申請以直接到教務處櫃台或者行政大樓2F的機台申請，但如果非本人要在教務處櫃台申請就需要有"委託書"及代理人的身分證件才能申請，或者代理人亦可直接到行政大樓2F的機台申請(但須知道申請人的基本資料)。'
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
    # 教務處註冊組-學分、成績類問答選單
    elif user_message.find('學分、成績') != -1:

        res_message = TemplateSendMessage(
            alt_text='學分、成績',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組-學分、成績類問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='如果對於期末的成績有疑問的話，請問要怎麼辦呢？',
                                text='依「文藻外語大學學生學期成績複查暨申訴處理要點」：學生對其學期成績有疑問者，應即向任課教師複查。如仍有異議，得於收到成績單後至開學一週內，向教務處註冊組填具「學生複查成績申請單」申請複查成績。'
                            ),
                            MessageTemplateAction(
                                label='我有英文必修課程還沒修過，假如我辦休學，然後在休學期間考托福，成績達到可以抵修免修的分數，那我可以辦復學後直接申請免修嗎？這樣抵完是否就可以領畢業證書？',
                                text='日間部四年制大學部學生英文能力檢定測驗托福達六百分；進修部四年制大學部學生英文能力檢定測驗托福達五百六十分，或本校認可之語文檢定測驗成績等同托福標準者，日間部學生可免修三十六學分之共同必修英文，但需選修其他科目補足該學分。\n所以如果您的英檢成績達可以免修，還是要補修其他學分才可以。'
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
    # 教務處註冊組-畢業類問答選單
    elif user_message.find('畢業') != -1:

        res_message = TemplateSendMessage(
            alt_text='畢業',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組-畢業類問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='如果因為畢業的時候未通過畢業語言檢定門檻(副修的語言檢定門檻)，所以只拿到肄業證書，假如說之後只要有再考過語檢，是不是隨時都能回學校換畢業證書呢？',
                                text='領取肄業（修業）證明書前提須辦理退學手續，退學後則無法再領取學位證書（即畢業證書）。'
                            ),
                            MessageTemplateAction(
                                label='如果考上了研究所可是只有領到結業證書，不知道能不能以考上研究所為由， 申請領畢業證書呢？',
                                text='依「文藻外語大學學則」第42條：學生修業期滿，修畢各系應修之科目與學分數，學業及操行成績均及格且通過各系訂定之語言能力檢定標準，始得畢業。由本校授予學士學位，並發給學士學位證書。'
                            ),
                            MessageTemplateAction(
                                label='請問畢業典禮每班上台授獎的學生，是各班歷年成績排名第一名的學生嗎？ 還是老師另選的品學兼優獎呢？',
                                text='文藻外語大學頒發應屆畢業生學業優良獎實施要點\n二、應屆畢業生學業優良獎每班取前一名，頒發獎狀乙幀加以表揚。\n三、應屆畢業生學業優良第一名之核計方式\n1.四年制學生成績以在校前七個學期計算\n2.二年制學生以在校前三個學期計算\n3.五年制學生以在校前九個學期計算\n四、因未修畢所屬系科應修學分或未通過所屬系科訂定之語言能力檢定標準及其它畢業規定，而延長修業年限者，均不列入評比，但因加修輔系、雙主修、教育學程而延長修業者，不在此限；累計排名為全班第一名如因故需延修或非在學身'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組-畢業類問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='為什麼文藻畢業證書用的紙不是一般獎狀的那種硬紙呢？因為這樣單薄的紙很容易折損，也不像正式的證書。',
                                text='本校學位證書用紙是特選材質，有防偽功能的設計，成本也比一般獎狀高很多，建議您妥善存放於畢業證書夾內。'
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
    # 教務處註冊組-其他問題類問答選單
    elif user_message.find('其他問題') != -1:

        res_message = TemplateSendMessage(
            alt_text='其他問題',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='教務處註冊組-其他問題類問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='日間四技部到底怎樣才有可能會被退學？',
                                text='依照本校學則第二十二條規定，學生有下列情形之一者，應予退學（各相關單位於退學處分前應告知學生）：\n一、逾期未註冊或休學逾期未復學者，視為無意願就學。\n二、經學生獎懲委員會議決議勒令退學者。\n三、日間部學生學期學業成績不及格科目之學分數，達該學期修習學分總數三分之二者；惟身心障礙學生不受此限。\n四、進修部學生學期學業成績不及格科目之學分數，連續兩學期達各該學期修習學分總數三分之二者；惟身心障礙學生不受此限。\n五、延長修業期限屆滿，仍未符合第四十二條畢業條件者。\n六、未經本校同意'
                            ),
                            MessageTemplateAction(
                                label='請問要辦理休學要準備什麼東西，如何辦理？',
                                text='1. 請攜學生證親至註冊組填寫相關表單，持高捷一卡通學生證者，如學生證尚有儲值，請先行至各捷運站辦理退費。\n2. 如未滿二十歲，須至少一位家長陪同。'
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
    # 教務處課務組問題分類選單
    elif user_message.find('課務組') != -1:

        res_message = TemplateSendMessage(
            alt_text='課務組',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='課務組問題分類',
                        text='請由下方選出您想詢問的問題種類！',
                        actions=[
                            MessageTemplateAction(
                                label='選課Q&A',
                                text='選課Q&A'
                            ),
                        ]
                    ),
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, res_message)
        return 0
###############################################################################
    # 教務處英/外語能力診斷輔導中心問答選單
    elif user_message.find('英/外語能力診斷輔導中心') != -1:

        res_message = TemplateSendMessage(
            alt_text='英/外語能力診斷輔導中心',
            template=CarouselTemplate(
                columns=[
                    # -----------------------------------------------------------------------------
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='英/外語能力診斷輔導中心問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='英/外語能力診斷輔導中心(LDCC)在哪裡？',
                                text='露德樓2F & 3F。'
                            ),
                            MessageTemplateAction(
                                label='診斷與諮商有何不同？',
                                text='診斷－初診：教師施行語言學習風格策略之診斷與分析；複診：針對聽、說、讀、寫、發音、文法、單字等進行，為您量身訂作一套語言學習精進計畫。\n諮商－在您實踐個人學習計畫時(包括使用處方籤時)遇到任何問題，皆可尋求老師之協助。'
                            ),
                            MessageTemplateAction(
                                label='什麼是處方籤？一定要有處方籤才可享用服務嗎？',
                                text='處方籤＝老師所開設之學習課程；但大專英檢已達240分以上者，基本上不需處方籤即可使用服務；可依照老師建議之處方籤內容學習，或可自行安排個人學習課程。\n處方籤項目包括：一、教師輔導療程：口語、簡報、詩歌、寫作、閱讀。二、主題式口語練習。三、自學軟體、補充教材。'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='英/外語能力診斷輔導中心問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='使用中心的服務是否皆須預約？',
                                text='是的，所有項目皆請同學線上預約。教師/小老師輔導療程請於七天前完成預約；口語小老師至少須於二天前預約完成，且不提供當場預約。自學軟體等療程，若需當天預約請洽中心人員確認是否尚有名額。'
                            ),
                            MessageTemplateAction(
                                label='我為什麼不能預約中心的服務項目？',
                                text='請先確認您成功註冊Dr. E-Learning多國語診斷諮商平台(包括確認個人基本資料、填寫學習風格與學習策略二份問卷等）。不會操作請看這裡。若依然無法使用，請聯絡中心(電話：(07)342-6031分機7403)。'
                            ),
                            MessageTemplateAction(
                                label='預約的軟體顯示地點為露德樓2F，到了預約時段是否逕自到二樓使用即可？',
                                text='不是的。凡使用中心提供的服務皆請先到三樓(G326)告知中心人員並報到後，方得進入二樓場地使用。預約自學軟體報到的同時，請先向櫃台索取個人資料袋及軟體記錄表，以利紀錄該次使用狀況及進度。'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='英/外語能力診斷輔導中心問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='為什麼我不能預約教師/小老師口語練習或使用自學軟體等項目呢？',
                                text='Dr. E-Learning多國語診斷諮商－英語療程系統，以大學英檢240分作為是否自由開放預約軟體及練口語權限為標準，因此無大學英檢成績或成績低於240分以下的同學，請先預約老師「診斷」，請老師依照個人學習需求開立口語練習及自學軟體處方箋，方得使用這些處方籤服務。'
                            ),
                            MessageTemplateAction(
                                label='口語練習之主題為何？',
                                text='中心軟體Issues in English I &II 共有16個主題、中心製作之口語練習主題Conversation Topics及My ET 主題11類 (其每位學生皆可於教務資訊系統安裝使用)。'
                            ),
                            MessageTemplateAction(
                                label='為什麼部分駐診老師/小老師班表上會在名字後加上-ELCC呢？有什麼特別的意思嗎？',
                                text='加上英文縮寫是為了區別執行地點：\n‧未加者：在英/外語能力診斷輔導中心(露德樓3樓，G326)\n‧加上ELCC：在歐亞能力診斷輔導中心(露德樓1樓)。'
                            ),
                        ]
                    ),
                    # =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='英/外語能力診斷輔導中心問題',
                        text='請由下方選出您想詢問的問題！',
                        actions=[
                            MessageTemplateAction(
                                label='臨時有事想取消當日的預約，看起來好像成功了，卻接到中心人員未出席的通知，怎麼會這樣？',
                                text='同學沒有取消當日預約的權限亦不建議這麼做，若有需要取消當日預約，請電洽或親洽中心人員為您取消。'
                            ),
                            MessageTemplateAction(
                                label='MyET自學網無法登入/帳號密碼錯誤/查無此帳號密碼?',
                                text='伺服器請選擇「台灣」>「高雄市」>「文藻外語大學」\n並輸入資訊服務入口網之學號與密碼方可登入\n若有相關問題請來信至: aa85@mail.wzu.edu.tw 或親洽中心詢問'
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
