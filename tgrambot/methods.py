# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#       This is an auto-generated file!       #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


# TGramBot - Partially Auto-generated Telegram Bot Api Library Python
# Copyright (C) 2022  Anand <anandpskerala@gmail.com>

# TGramBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# TGramBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import tgrambot
from typing import List, Union
from tgrambot.types import (
    Update,
    InputFile,
    WebhookInfo,
    User,
    MessageEntity,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    Message,
    MessageId,
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
    UserProfilePhotos,
    File,
    ChatPermissions,
    ChatInviteLink,
    Chat,
    ChatMember,
    BotCommand,
    BotCommandScope,
    MenuButton,
    ChatAdministratorRights,
    InputMedia,
    Poll,
    StickerSet,
    MaskPosition,
    InlineQueryResult,
    SentWebAppMessage,
    LabeledPrice,
    ShippingOption,
    PassportElementError,
    GameHighScore
)


class Methods:
    def __init__(self, bot: "tgrambot.Bot"):
        self._bot = bot

    async def get_updates(self, offset: int = None, limit: int = None, timeout: int = None, allowed_updates: List[str] = None):
        """
        Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.

        Source : https://core.telegram.org/bots/api#getupdates
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'getUpdates'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return [Update(**r) for r in result]

    async def set_webhook(self, url: str, certificate: InputFile = None, ip_address: str = None, max_connections: int = None, allowed_updates: List[str] = None, drop_pending_updates: bool = None, secret_token: str = None):
        """
        Use this method to specify a URL and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified URL, containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns True on success.
        If you'd like to make sure that the webhook was set by you, you can specify secret data in the parameter secret_token. If specified, the request will contain a header "X-Telegram-Bot-Api-Secret-Token" with the secret token as content.

        Source : https://core.telegram.org/bots/api#setwebhook
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        if self._bot.attach_file(payload, 'certificate', certificate) is not None:
            files.update(self._bot.attach_file(payload, 'certificate', certificate))
        method = 'setWebhook'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def delete_webhook(self, drop_pending_updates: bool = None):
        """
        Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success.

        Source : https://core.telegram.org/bots/api#deletewebhook
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'deleteWebhook'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def get_webhook_info(self):
        """
        Use this method to get current webhook status. Requires no parameters. On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty.

        Source : https://core.telegram.org/bots/api#getwebhookinfo
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'getWebhookInfo'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return WebhookInfo(**result)

    async def get_me(self):
        """
        A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object.

        Source : https://core.telegram.org/bots/api#getme
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'getMe'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return User(**result)

    async def log_out(self):
        """
        Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters.

        Source : https://core.telegram.org/bots/api#logout
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'logOut'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def close(self):
        """
        Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters.

        Source : https://core.telegram.org/bots/api#close
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'close'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def send_message(self, chat_id: Union[int, str], text: str, parse_mode: str = None, entities: List[MessageEntity] = None, disable_web_page_preview: bool = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        Use this method to send text messages. On success, the sent Message is returned.

        Source : https://core.telegram.org/bots/api#sendmessage
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'sendMessage'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def forward_message(self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int, disable_notification: bool = None, protect_content: bool = None):
        """
        Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent Message is returned.

        Source : https://core.telegram.org/bots/api#forwardmessage
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'forwardMessage'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def copy_message(self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int, caption: str = None, parse_mode: str = None, caption_entities: List[MessageEntity] = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        Use this method to copy messages of any kind. Service messages and invoice messages can't be copied. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success.

        Source : https://core.telegram.org/bots/api#copymessage
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'copyMessage'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return MessageId(**result)

    async def send_photo(self, chat_id: Union[int, str], photo: Union[InputFile, str], caption: str = None, parse_mode: str = None, caption_entities: List[MessageEntity] = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        Use this method to send photos. On success, the sent Message is returned.

        Source : https://core.telegram.org/bots/api#sendphoto
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        if self._bot.attach_file(payload, 'photo', photo) is not None:
            files.update(self._bot.attach_file(payload, 'photo', photo))
        method = 'sendPhoto'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def send_audio(self, chat_id: Union[int, str], audio: Union[InputFile, str], caption: str = None, parse_mode: str = None, caption_entities: List[MessageEntity] = None, duration: int = None, performer: str = None, title: str = None, thumb: Union[InputFile, str] = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
        For sending voice messages, use the sendVoice method instead.

        Source : https://core.telegram.org/bots/api#sendaudio
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        if self._bot.attach_file(payload, 'audio', audio) is not None:
            files.update(self._bot.attach_file(payload, 'audio', audio))
        if self._bot.attach_file(payload, 'thumb', thumb) is not None:
            files.update(self._bot.attach_file(payload, 'thumb', thumb))
        method = 'sendAudio'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def send_document(self, chat_id: Union[int, str], document: Union[InputFile, str], thumb: Union[InputFile, str] = None, caption: str = None, parse_mode: str = None, caption_entities: List[MessageEntity] = None, disable_content_type_detection: bool = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

        Source : https://core.telegram.org/bots/api#senddocument
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        if self._bot.attach_file(payload, 'document', document) is not None:
            files.update(self._bot.attach_file(payload, 'document', document))
        if self._bot.attach_file(payload, 'thumb', thumb) is not None:
            files.update(self._bot.attach_file(payload, 'thumb', thumb))
        method = 'sendDocument'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def send_video(self, chat_id: Union[int, str], video: Union[InputFile, str], duration: int = None, width: int = None, height: int = None, thumb: Union[InputFile, str] = None, caption: str = None, parse_mode: str = None, caption_entities: List[MessageEntity] = None, supports_streaming: bool = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

        Source : https://core.telegram.org/bots/api#sendvideo
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        if self._bot.attach_file(payload, 'video', video) is not None:
            files.update(self._bot.attach_file(payload, 'video', video))
        if self._bot.attach_file(payload, 'thumb', thumb) is not None:
            files.update(self._bot.attach_file(payload, 'thumb', thumb))
        method = 'sendVideo'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def send_animation(self, chat_id: Union[int, str], animation: Union[InputFile, str], duration: int = None, width: int = None, height: int = None, thumb: Union[InputFile, str] = None, caption: str = None, parse_mode: str = None, caption_entities: List[MessageEntity] = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

        Source : https://core.telegram.org/bots/api#sendanimation
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        if self._bot.attach_file(payload, 'animation', animation) is not None:
            files.update(self._bot.attach_file(payload, 'animation', animation))
        if self._bot.attach_file(payload, 'thumb', thumb) is not None:
            files.update(self._bot.attach_file(payload, 'thumb', thumb))
        method = 'sendAnimation'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def send_voice(self, chat_id: Union[int, str], voice: Union[InputFile, str], caption: str = None, parse_mode: str = None, caption_entities: List[MessageEntity] = None, duration: int = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

        Source : https://core.telegram.org/bots/api#sendvoice
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        if self._bot.attach_file(payload, 'voice', voice) is not None:
            files.update(self._bot.attach_file(payload, 'voice', voice))
        method = 'sendVoice'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def send_video_note(self, chat_id: Union[int, str], video_note: Union[InputFile, str], duration: int = None, length: int = None, thumb: Union[InputFile, str] = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        As of v.4.0, Telegram clients support rounded square MPEG4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned.

        Source : https://core.telegram.org/bots/api#sendvideonote
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        if self._bot.attach_file(payload, 'video_note', video_note) is not None:
            files.update(self._bot.attach_file(payload, 'video_note', video_note))
        if self._bot.attach_file(payload, 'thumb', thumb) is not None:
            files.update(self._bot.attach_file(payload, 'thumb', thumb))
        method = 'sendVideoNote'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def send_media_group(self, chat_id: Union[int, str], media: Union[List[InputMediaAudio], List[InputMediaDocument], List[InputMediaPhoto], List[InputMediaVideo]], disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None):
        """
        Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned.

        Source : https://core.telegram.org/bots/api#sendmediagroup
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'sendMediaGroup'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return [Message(**r) for r in result]

    async def send_location(self, chat_id: Union[int, str], latitude: int, longitude: int, horizontal_accuracy: int = None, live_period: int = None, heading: int = None, proximity_alert_radius: int = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        Use this method to send point on the map. On success, the sent Message is returned.

        Source : https://core.telegram.org/bots/api#sendlocation
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'sendLocation'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def edit_message_live_location(self, latitude: int, longitude: int, chat_id: Union[int, str] = None, message_id: int = None, inline_message_id: str = None, horizontal_accuracy: int = None, heading: int = None, proximity_alert_radius: int = None, reply_markup: InlineKeyboardMarkup = None):
        """
        Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Source : https://core.telegram.org/bots/api#editmessagelivelocation
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'editMessageLiveLocation'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def stop_message_live_location(self, chat_id: Union[int, str] = None, message_id: int = None, inline_message_id: str = None, reply_markup: InlineKeyboardMarkup = None):
        """
        Use this method to stop updating a live location message before live_period expires. On success, if the message is not an inline message, the edited Message is returned, otherwise True is returned.

        Source : https://core.telegram.org/bots/api#stopmessagelivelocation
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'stopMessageLiveLocation'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def send_venue(self, chat_id: Union[int, str], latitude: int, longitude: int, title: str, address: str, foursquare_id: str = None, foursquare_type: str = None, google_place_id: str = None, google_place_type: str = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        Use this method to send information about a venue. On success, the sent Message is returned.

        Source : https://core.telegram.org/bots/api#sendvenue
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'sendVenue'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def send_contact(self, chat_id: Union[int, str], phone_number: str, first_name: str, last_name: str = None, vcard: str = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        Use this method to send phone contacts. On success, the sent Message is returned.

        Source : https://core.telegram.org/bots/api#sendcontact
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'sendContact'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def send_poll(self, chat_id: Union[int, str], question: str, options: List[str], is_anonymous: bool = None, type: str = None, allows_multiple_answers: bool = None, correct_option_id: int = None, explanation: str = None, explanation_parse_mode: str = None, explanation_entities: List[MessageEntity] = None, open_period: int = None, close_date: int = None, is_closed: bool = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        Use this method to send a native poll. On success, the sent Message is returned.

        Source : https://core.telegram.org/bots/api#sendpoll
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'sendPoll'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def send_dice(self, chat_id: Union[int, str], emoji: str = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned.

        Source : https://core.telegram.org/bots/api#senddice
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'sendDice'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def send_chat_action(self, chat_id: Union[int, str], action: str):
        """
        Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success.
        We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.

        Source : https://core.telegram.org/bots/api#sendchataction
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'sendChatAction'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def get_user_profile_photos(self, user_id: int, offset: int = None, limit: int = None):
        """
        Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.

        Source : https://core.telegram.org/bots/api#getuserprofilephotos
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'getUserProfilePhotos'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return UserProfilePhotos(**result)

    async def get_file(self, file_id: str):
        """
        Use this method to get basic information about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a File object is returned. The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again.
        Note: This function may not preserve the original file name and MIME type. You should save the file's MIME type and name (if available) when the File object is received.

        Source : https://core.telegram.org/bots/api#getfile
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'getFile'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return File(**result)

    async def ban_chat_member(self, chat_id: Union[int, str], user_id: int, until_date: int = None, revoke_messages: bool = None):
        """
        Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

        Source : https://core.telegram.org/bots/api#banchatmember
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'banChatMember'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def unban_chat_member(self, chat_id: Union[int, str], user_id: int, only_if_banned: bool = None):
        """
        Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success.

        Source : https://core.telegram.org/bots/api#unbanchatmember
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'unbanChatMember'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def restrict_chat_member(self, chat_id: Union[int, str], user_id: int, permissions: ChatPermissions, until_date: int = None):
        """
        Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user. Returns True on success.

        Source : https://core.telegram.org/bots/api#restrictchatmember
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'restrictChatMember'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def promote_chat_member(self, chat_id: Union[int, str], user_id: int, is_anonymous: bool = None, can_manage_chat: bool = None, can_post_messages: bool = None, can_edit_messages: bool = None, can_delete_messages: bool = None, can_manage_video_chats: bool = None, can_restrict_members: bool = None, can_promote_members: bool = None, can_change_info: bool = None, can_invite_users: bool = None, can_pin_messages: bool = None):
        """
        Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user. Returns True on success.

        Source : https://core.telegram.org/bots/api#promotechatmember
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'promoteChatMember'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def set_chat_administrator_custom_title(self, chat_id: Union[int, str], user_id: int, custom_title: str):
        """
        Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success.

        Source : https://core.telegram.org/bots/api#setchatadministratorcustomtitle
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'setChatAdministratorCustomTitle'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def ban_chat_sender_chat(self, chat_id: Union[int, str], sender_chat_id: int):
        """
        Use this method to ban a channel chat in a supergroup or a channel. Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of their channels. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns True on success.

        Source : https://core.telegram.org/bots/api#banchatsenderchat
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'banChatSenderChat'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def unban_chat_sender_chat(self, chat_id: Union[int, str], sender_chat_id: int):
        """
        Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns True on success.

        Source : https://core.telegram.org/bots/api#unbanchatsenderchat
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'unbanChatSenderChat'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def set_chat_permissions(self, chat_id: Union[int, str], permissions: ChatPermissions):
        """
        Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members administrator rights. Returns True on success.

        Source : https://core.telegram.org/bots/api#setchatpermissions
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'setChatPermissions'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def export_chat_invite_link(self, chat_id: Union[int, str]):
        """
        Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as String on success.

        Source : https://core.telegram.org/bots/api#exportchatinvitelink
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'exportChatInviteLink'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def create_chat_invite_link(self, chat_id: Union[int, str], name: str = None, expire_date: int = None, member_limit: int = None, creates_join_request: bool = None):
        """
        Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object.

        Source : https://core.telegram.org/bots/api#createchatinvitelink
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'createChatInviteLink'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return ChatInviteLink(**result)

    async def edit_chat_invite_link(self, chat_id: Union[int, str], invite_link: str, name: str = None, expire_date: int = None, member_limit: int = None, creates_join_request: bool = None):
        """
        Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a ChatInviteLink object.

        Source : https://core.telegram.org/bots/api#editchatinvitelink
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'editChatInviteLink'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return ChatInviteLink(**result)

    async def revoke_chat_invite_link(self, chat_id: Union[int, str], invite_link: str):
        """
        Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object.

        Source : https://core.telegram.org/bots/api#revokechatinvitelink
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'revokeChatInviteLink'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return ChatInviteLink(**result)

    async def approve_chat_join_request(self, chat_id: Union[int, str], user_id: int):
        """
        Use this method to approve a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success.

        Source : https://core.telegram.org/bots/api#approvechatjoinrequest
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'approveChatJoinRequest'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def decline_chat_join_request(self, chat_id: Union[int, str], user_id: int):
        """
        Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success.

        Source : https://core.telegram.org/bots/api#declinechatjoinrequest
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'declineChatJoinRequest'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def set_chat_photo(self, chat_id: Union[int, str], photo: InputFile):
        """
        Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

        Source : https://core.telegram.org/bots/api#setchatphoto
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        if self._bot.attach_file(payload, 'photo', photo) is not None:
            files.update(self._bot.attach_file(payload, 'photo', photo))
        method = 'setChatPhoto'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def delete_chat_photo(self, chat_id: Union[int, str]):
        """
        Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

        Source : https://core.telegram.org/bots/api#deletechatphoto
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'deleteChatPhoto'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def set_chat_title(self, chat_id: Union[int, str], title: str):
        """
        Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

        Source : https://core.telegram.org/bots/api#setchattitle
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'setChatTitle'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def set_chat_description(self, chat_id: Union[int, str], description: str = None):
        """
        Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

        Source : https://core.telegram.org/bots/api#setchatdescription
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'setChatDescription'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def pin_chat_message(self, chat_id: Union[int, str], message_id: int, disable_notification: bool = None):
        """
        Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.

        Source : https://core.telegram.org/bots/api#pinchatmessage
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'pinChatMessage'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def unpin_chat_message(self, chat_id: Union[int, str], message_id: int = None):
        """
        Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.

        Source : https://core.telegram.org/bots/api#unpinchatmessage
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'unpinChatMessage'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def unpin_all_chat_messages(self, chat_id: Union[int, str]):
        """
        Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.

        Source : https://core.telegram.org/bots/api#unpinallchatmessages
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'unpinAllChatMessages'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def leave_chat(self, chat_id: Union[int, str]):
        """
        Use this method for your bot to leave a group, supergroup or channel. Returns True on success.

        Source : https://core.telegram.org/bots/api#leavechat
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'leaveChat'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def get_chat(self, chat_id: Union[int, str]):
        """
        Use this method to get up to date information about the chat (current name of the user for one-on-one conversations, current username of a user, group or channel, etc.). Returns a Chat object on success.

        Source : https://core.telegram.org/bots/api#getchat
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'getChat'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Chat(**result)

    async def get_chat_administrators(self, chat_id: Union[int, str]):
        """
        Use this method to get a list of administrators in a chat. On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned.

        Source : https://core.telegram.org/bots/api#getchatadministrators
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'getChatAdministrators'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return [ChatMember(**r) for r in result]

    async def get_chat_member_count(self, chat_id: Union[int, str]):
        """
        Use this method to get the number of members in a chat. Returns Int on success.

        Source : https://core.telegram.org/bots/api#getchatmembercount
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'getChatMemberCount'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def get_chat_member(self, chat_id: Union[int, str], user_id: int):
        """
        Use this method to get information about a member of a chat. Returns a ChatMember object on success.

        Source : https://core.telegram.org/bots/api#getchatmember
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'getChatMember'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return ChatMember(**result)

    async def set_chat_sticker_set(self, chat_id: Union[int, str], sticker_set_name: str):
        """
        Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.

        Source : https://core.telegram.org/bots/api#setchatstickerset
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'setChatStickerSet'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def delete_chat_sticker_set(self, chat_id: Union[int, str]):
        """
        Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.

        Source : https://core.telegram.org/bots/api#deletechatstickerset
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'deleteChatStickerSet'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def answer_callback_query(self, callback_query_id: str, text: str = None, show_alert: bool = None, url: str = None, cache_time: int = None):
        """
        Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned.

        Source : https://core.telegram.org/bots/api#answercallbackquery
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'answerCallbackQuery'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def set_my_commands(self, commands: List[BotCommand], scope: BotCommandScope = None, language_code: str = None):
        """
        Use this method to change the list of the bot's commands. See https://core.telegram.org/bots#commands for more details about bot commands. Returns True on success.

        Source : https://core.telegram.org/bots/api#setmycommands
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'setMyCommands'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def delete_my_commands(self, scope: BotCommandScope = None, language_code: str = None):
        """
        Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, higher level commands will be shown to affected users. Returns True on success.

        Source : https://core.telegram.org/bots/api#deletemycommands
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'deleteMyCommands'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def get_my_commands(self, scope: BotCommandScope = None, language_code: str = None):
        """
        Use this method to get the current list of the bot's commands for the given scope and user language. Returns Array of BotCommand on success. If commands aren't set, an empty list is returned.

        Source : https://core.telegram.org/bots/api#getmycommands
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'getMyCommands'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return [BotCommand(**r) for r in result]

    async def set_chat_menu_button(self, chat_id: int = None, menu_button: MenuButton = None):
        """
        Use this method to change the bot's menu button in a private chat, or the default menu button. Returns True on success.

        Source : https://core.telegram.org/bots/api#setchatmenubutton
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'setChatMenuButton'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def get_chat_menu_button(self, chat_id: int = None):
        """
        Use this method to get the current value of the bot's menu button in a private chat, or the default menu button. Returns MenuButton on success.

        Source : https://core.telegram.org/bots/api#getchatmenubutton
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'getChatMenuButton'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return MenuButton(**result)

    async def set_my_default_administrator_rights(self, rights: ChatAdministratorRights = None, for_channels: bool = None):
        """
        Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels. These rights will be suggested to users, but they are are free to modify the list before adding the bot. Returns True on success.

        Source : https://core.telegram.org/bots/api#setmydefaultadministratorrights
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'setMyDefaultAdministratorRights'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def get_my_default_administrator_rights(self, for_channels: bool = None):
        """
        Use this method to get the current default administrator rights of the bot. Returns ChatAdministratorRights on success.

        Source : https://core.telegram.org/bots/api#getmydefaultadministratorrights
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'getMyDefaultAdministratorRights'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return ChatAdministratorRights(**result)

    async def edit_message_text(self, text: str, chat_id: Union[int, str] = None, message_id: int = None, inline_message_id: str = None, parse_mode: str = None, entities: List[MessageEntity] = None, disable_web_page_preview: bool = None, reply_markup: InlineKeyboardMarkup = None):
        """
        Use this method to edit text and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Source : https://core.telegram.org/bots/api#editmessagetext
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'editMessageText'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def edit_message_caption(self, chat_id: Union[int, str] = None, message_id: int = None, inline_message_id: str = None, caption: str = None, parse_mode: str = None, caption_entities: List[MessageEntity] = None, reply_markup: InlineKeyboardMarkup = None):
        """
        Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Source : https://core.telegram.org/bots/api#editmessagecaption
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'editMessageCaption'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def edit_message_media(self, media: InputMedia, chat_id: Union[int, str] = None, message_id: int = None, inline_message_id: str = None, reply_markup: InlineKeyboardMarkup = None):
        """
        Use this method to edit animation, audio, document, photo, or video messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Source : https://core.telegram.org/bots/api#editmessagemedia
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'editMessageMedia'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def edit_message_reply_markup(self, chat_id: Union[int, str] = None, message_id: int = None, inline_message_id: str = None, reply_markup: InlineKeyboardMarkup = None):
        """
        Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Source : https://core.telegram.org/bots/api#editmessagereplymarkup
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'editMessageReplyMarkup'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def stop_poll(self, chat_id: Union[int, str], message_id: int, reply_markup: InlineKeyboardMarkup = None):
        """
        Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.

        Source : https://core.telegram.org/bots/api#stoppoll
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'stopPoll'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Poll(**result)

    async def delete_message(self, chat_id: Union[int, str], message_id: int):
        """
        Use this method to delete a message, including service messages, with the following limitations:
        - A message can only be deleted if it was sent less than 48 hours ago.
        - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
        - Bots can delete outgoing messages in private chats, groups, and supergroups.
        - Bots can delete incoming messages in private chats.
        - Bots granted can_post_messages permissions can delete outgoing messages in channels.
        - If the bot is an administrator of a group, it can delete any message there.
        - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.
        Returns True on success.

        Source : https://core.telegram.org/bots/api#deletemessage
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'deleteMessage'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def send_sticker(self, chat_id: Union[int, str], sticker: Union[InputFile, str], disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        """
        Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers. On success, the sent Message is returned.

        Source : https://core.telegram.org/bots/api#sendsticker
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        if self._bot.attach_file(payload, 'sticker', sticker) is not None:
            files.update(self._bot.attach_file(payload, 'sticker', sticker))
        method = 'sendSticker'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def get_sticker_set(self, name: str):
        """
        Use this method to get a sticker set. On success, a StickerSet object is returned.

        Source : https://core.telegram.org/bots/api#getstickerset
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'getStickerSet'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return StickerSet(**result)

    async def upload_sticker_file(self, user_id: int, png_sticker: InputFile):
        """
        Use this method to upload a .PNG file with a sticker for later use in createNewStickerSet and addStickerToSet methods (can be used multiple times). Returns the uploaded File on success.

        Source : https://core.telegram.org/bots/api#uploadstickerfile
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        if self._bot.attach_file(payload, 'png_sticker', png_sticker) is not None:
            files.update(self._bot.attach_file(payload, 'png_sticker', png_sticker))
        method = 'uploadStickerFile'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return File(**result)

    async def create_new_sticker_set(self, user_id: int, name: str, title: str, emojis: str, png_sticker: Union[InputFile, str] = None, tgs_sticker: InputFile = None, webm_sticker: InputFile = None, contains_masks: bool = None, mask_position: MaskPosition = None):
        """
        Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. You must use exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Returns True on success.

        Source : https://core.telegram.org/bots/api#createnewstickerset
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        if self._bot.attach_file(payload, 'png_sticker', png_sticker) is not None:
            files.update(self._bot.attach_file(payload, 'png_sticker', png_sticker))
        if self._bot.attach_file(payload, 'tgs_sticker', tgs_sticker) is not None:
            files.update(self._bot.attach_file(payload, 'tgs_sticker', tgs_sticker))
        if self._bot.attach_file(payload, 'webm_sticker', webm_sticker) is not None:
            files.update(self._bot.attach_file(payload, 'webm_sticker', webm_sticker))
        method = 'createNewStickerSet'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def add_sticker_to_set(self, user_id: int, name: str, emojis: str, png_sticker: Union[InputFile, str] = None, tgs_sticker: InputFile = None, webm_sticker: InputFile = None, mask_position: MaskPosition = None):
        """
        Use this method to add a new sticker to a set created by the bot. You must use exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Animated stickers can be added to animated sticker sets and only to them. Animated sticker sets can have up to 50 stickers. Static sticker sets can have up to 120 stickers. Returns True on success.

        Source : https://core.telegram.org/bots/api#addstickertoset
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        if self._bot.attach_file(payload, 'png_sticker', png_sticker) is not None:
            files.update(self._bot.attach_file(payload, 'png_sticker', png_sticker))
        if self._bot.attach_file(payload, 'tgs_sticker', tgs_sticker) is not None:
            files.update(self._bot.attach_file(payload, 'tgs_sticker', tgs_sticker))
        if self._bot.attach_file(payload, 'webm_sticker', webm_sticker) is not None:
            files.update(self._bot.attach_file(payload, 'webm_sticker', webm_sticker))
        method = 'addStickerToSet'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def set_sticker_position_in_set(self, sticker: str, position: int):
        """
        Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success.

        Source : https://core.telegram.org/bots/api#setstickerpositioninset
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'setStickerPositionInSet'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def delete_sticker_from_set(self, sticker: str):
        """
        Use this method to delete a sticker from a set created by the bot. Returns True on success.

        Source : https://core.telegram.org/bots/api#deletestickerfromset
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'deleteStickerFromSet'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def set_sticker_set_thumb(self, name: str, user_id: int, thumb: Union[InputFile, str] = None):
        """
        Use this method to set the thumbnail of a sticker set. Animated thumbnails can be set for animated sticker sets only. Video thumbnails can be set only for video sticker sets only. Returns True on success.

        Source : https://core.telegram.org/bots/api#setstickersetthumb
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        if self._bot.attach_file(payload, 'thumb', thumb) is not None:
            files.update(self._bot.attach_file(payload, 'thumb', thumb))
        method = 'setStickerSetThumb'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def answer_inline_query(self, inline_query_id: str, results: List[InlineQueryResult], cache_time: int = None, is_personal: bool = None, next_offset: str = None, switch_pm_text: str = None, switch_pm_parameter: str = None):
        """
        Use this method to send answers to an inline query. On success, True is returned.
        No more than 50 results per query are allowed.

        Source : https://core.telegram.org/bots/api#answerinlinequery
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'answerInlineQuery'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def answer_web_app_query(self, web_app_query_id: str, result: InlineQueryResult):
        """
        Use this method to set the result of an interaction with a Web App and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a SentWebAppMessage object is returned.

        Source : https://core.telegram.org/bots/api#answerwebappquery
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'answerWebAppQuery'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return SentWebAppMessage(**result)

    async def send_invoice(self, chat_id: Union[int, str], title: str, description: str, payload: str, provider_token: str, currency: str, prices: List[LabeledPrice], max_tip_amount: int = None, suggested_tip_amounts: List[int] = None, start_parameter: str = None, provider_data: str = None, photo_url: str = None, photo_size: int = None, photo_width: int = None, photo_height: int = None, need_name: bool = None, need_phone_number: bool = None, need_email: bool = None, need_shipping_address: bool = None, send_phone_number_to_provider: bool = None, send_email_to_provider: bool = None, is_flexible: bool = None, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup = None):
        """
        Use this method to send invoices. On success, the sent Message is returned.

        Source : https://core.telegram.org/bots/api#sendinvoice
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'sendInvoice'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def create_invoice_link(self, title: str, description: str, payload: str, provider_token: str, currency: str, prices: List[LabeledPrice], max_tip_amount: int = None, suggested_tip_amounts: List[int] = None, provider_data: str = None, photo_url: str = None, photo_size: int = None, photo_width: int = None, photo_height: int = None, need_name: bool = None, need_phone_number: bool = None, need_email: bool = None, need_shipping_address: bool = None, send_phone_number_to_provider: bool = None, send_email_to_provider: bool = None, is_flexible: bool = None):
        """
        Use this method to create a link for an invoice. Returns the created invoice link as String on success.

        Source : https://core.telegram.org/bots/api#createinvoicelink
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'createInvoiceLink'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def answer_shipping_query(self, shipping_query_id: str, ok: bool, shipping_options: List[ShippingOption] = None, error_message: str = None):
        """
        If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned.

        Source : https://core.telegram.org/bots/api#answershippingquery
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'answerShippingQuery'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def answer_pre_checkout_query(self, pre_checkout_query_id: str, ok: bool, error_message: str = None):
        """
        Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query. Use this method to respond to such pre-checkout queries. On success, True is returned. Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.

        Source : https://core.telegram.org/bots/api#answerprecheckoutquery
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'answerPreCheckoutQuery'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def set_passport_data_errors(self, user_id: int, errors: List[PassportElementError]):
        """
        Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns True on success.
        Use this if the data submitted by the user doesn't satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues.

        Source : https://core.telegram.org/bots/api#setpassportdataerrors
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'setPassportDataErrors'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return result

    async def send_game(self, chat_id: int, game_short_name: str, disable_notification: bool = None, protect_content: bool = None, reply_to_message_id: int = None, allow_sending_without_reply: bool = None, reply_markup: InlineKeyboardMarkup = None):
        """
        Use this method to send a game. On success, the sent Message is returned.

        Source : https://core.telegram.org/bots/api#sendgame
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'sendGame'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def set_game_score(self, user_id: int, score: int, force: bool = None, disable_edit_message: bool = None, chat_id: int = None, message_id: int = None, inline_message_id: str = None):
        """
        Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the Message is returned, otherwise True is returned. Returns an error, if the new score is not greater than the user's current score in the chat and force is False.

        Source : https://core.telegram.org/bots/api#setgamescore
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'setGameScore'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return Message(**result)

    async def get_game_high_scores(self, user_id: int, chat_id: int = None, message_id: int = None, inline_message_id: str = None):
        """
        Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. On success, returns an Array of GameHighScore objects.

        Source : https://core.telegram.org/bots/api#getgamehighscores
        """
        payload = self._bot.generate_payload(**locals())
        files = {}
        
        method = 'getGameHighScores'
        url = self._bot.get_api_url(method)
        result = await self._bot.aio_post(url, payload, files)
        return [GameHighScore(**r) for r in result]

