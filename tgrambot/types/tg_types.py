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

from typing import Union, List
from pydantic import Field

from .base import TelegramObject


class WebhookInfo(TelegramObject):

    """
    Describes the current status of a webhook.
    """
    
    url: str = Field(default=None)
    has_custom_certificate: bool = Field(default=None)
    pending_update_count: int = Field(default=None)
    ip_address: str = Field(default=None)
    last_error_date: int = Field(default=None)
    last_error_message: str = Field(default=None)
    last_synchronization_error_date: int = Field(default=None)
    max_connections: int = Field(default=None)
    allowed_updates: List[str] = Field(default=None)
    

class User(TelegramObject):

    """
    This object represents a Telegram user or bot.
    """
    
    id: int = Field(default=None)
    is_bot: bool = Field(default=None)
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    username: str = Field(default=None)
    language_code: str = Field(default=None)
    is_premium: bool = Field(default=None)
    added_to_attachment_menu: bool = Field(default=None)
    can_join_groups: bool = Field(default=None)
    can_read_all_group_messages: bool = Field(default=None)
    supports_inline_queries: bool = Field(default=None)
    

class MessageId(TelegramObject):

    """
    This object represents a unique message identifier.
    """
    
    message_id: int = Field(default=None)
    

class MessageEntity(TelegramObject):

    """
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.
    """
    
    type: str = Field(default=None)
    offset: int = Field(default=None)
    length: int = Field(default=None)
    url: str = Field(default=None)
    user: "User" = Field(default=None)
    language: str = Field(default=None)
    

class PhotoSize(TelegramObject):

    """
    This object represents one size of a photo or a file / sticker thumbnail.
    """
    
    file_id: str = Field(default=None)
    file_unique_id: str = Field(default=None)
    width: int = Field(default=None)
    height: int = Field(default=None)
    file_size: int = Field(default=None)
    

class Animation(TelegramObject):

    """
    This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).
    """
    
    file_id: str = Field(default=None)
    file_unique_id: str = Field(default=None)
    width: int = Field(default=None)
    height: int = Field(default=None)
    duration: int = Field(default=None)
    thumb: "PhotoSize" = Field(default=None)
    file_name: str = Field(default=None)
    mime_type: str = Field(default=None)
    file_size: int = Field(default=None)
    

class Audio(TelegramObject):

    """
    This object represents an audio file to be treated as music by the Telegram clients.
    """
    
    file_id: str = Field(default=None)
    file_unique_id: str = Field(default=None)
    duration: int = Field(default=None)
    performer: str = Field(default=None)
    title: str = Field(default=None)
    file_name: str = Field(default=None)
    mime_type: str = Field(default=None)
    file_size: int = Field(default=None)
    thumb: "PhotoSize" = Field(default=None)
    

class Document(TelegramObject):

    """
    This object represents a general file (as opposed to photos, voice messages and audio files).
    """
    
    file_id: str = Field(default=None)
    file_unique_id: str = Field(default=None)
    thumb: "PhotoSize" = Field(default=None)
    file_name: str = Field(default=None)
    mime_type: str = Field(default=None)
    file_size: int = Field(default=None)
    

class Video(TelegramObject):

    """
    This object represents a video file.
    """
    
    file_id: str = Field(default=None)
    file_unique_id: str = Field(default=None)
    width: int = Field(default=None)
    height: int = Field(default=None)
    duration: int = Field(default=None)
    thumb: "PhotoSize" = Field(default=None)
    file_name: str = Field(default=None)
    mime_type: str = Field(default=None)
    file_size: int = Field(default=None)
    

class VideoNote(TelegramObject):

    """
    This object represents a video message (available in Telegram apps as of v.4.0).
    """
    
    file_id: str = Field(default=None)
    file_unique_id: str = Field(default=None)
    length: int = Field(default=None)
    duration: int = Field(default=None)
    thumb: "PhotoSize" = Field(default=None)
    file_size: int = Field(default=None)
    

class Voice(TelegramObject):

    """
    This object represents a voice note.
    """
    
    file_id: str = Field(default=None)
    file_unique_id: str = Field(default=None)
    duration: int = Field(default=None)
    mime_type: str = Field(default=None)
    file_size: int = Field(default=None)
    

class Contact(TelegramObject):

    """
    This object represents a phone contact.
    """
    
    phone_number: str = Field(default=None)
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    user_id: int = Field(default=None)
    vcard: str = Field(default=None)
    

class Dice(TelegramObject):

    """
    This object represents an animated emoji that displays a random value.
    """
    
    emoji: str = Field(default=None)
    value: int = Field(default=None)
    

class PollOption(TelegramObject):

    """
    This object contains information about one answer option in a poll.
    """
    
    text: str = Field(default=None)
    voter_count: int = Field(default=None)
    

class PollAnswer(TelegramObject):

    """
    This object represents an answer of a user in a non-anonymous poll.
    """
    
    poll_id: str = Field(default=None)
    user: "User" = Field(default=None)
    option_ids: List[int] = Field(default=None)
    

class Poll(TelegramObject):

    """
    This object contains information about a poll.
    """
    
    id: str = Field(default=None)
    question: str = Field(default=None)
    options: List["PollOption"] = Field(default=None)
    total_voter_count: int = Field(default=None)
    is_closed: bool = Field(default=None)
    is_anonymous: bool = Field(default=None)
    type: str = Field(default=None)
    allows_multiple_answers: bool = Field(default=None)
    correct_option_id: int = Field(default=None)
    explanation: str = Field(default=None)
    explanation_entities: List["MessageEntity"] = Field(default=None)
    open_period: int = Field(default=None)
    close_date: int = Field(default=None)
    

class Location(TelegramObject):

    """
    This object represents a point on the map.
    """
    
    longitude: int = Field(default=None)
    latitude: int = Field(default=None)
    horizontal_accuracy: int = Field(default=None)
    live_period: int = Field(default=None)
    heading: int = Field(default=None)
    proximity_alert_radius: int = Field(default=None)
    

class Venue(TelegramObject):

    """
    This object represents a venue.
    """
    
    location: "Location" = Field(default=None)
    title: str = Field(default=None)
    address: str = Field(default=None)
    foursquare_id: str = Field(default=None)
    foursquare_type: str = Field(default=None)
    google_place_id: str = Field(default=None)
    google_place_type: str = Field(default=None)
    

class WebAppData(TelegramObject):

    """
    Describes data sent from a Web App to the bot.
    """
    
    data: str = Field(default=None)
    button_text: str = Field(default=None)
    

class ProximityAlertTriggered(TelegramObject):

    """
    This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.
    """
    
    traveler: "User" = Field(default=None)
    watcher: "User" = Field(default=None)
    distance: int = Field(default=None)
    

class MessageAutoDeleteTimerChanged(TelegramObject):

    """
    This object represents a service message about a change in auto-delete timer settings.
    """
    
    message_auto_delete_time: int = Field(default=None)
    

class VideoChatScheduled(TelegramObject):

    """
    This object represents a service message about a video chat scheduled in the chat.
    """
    
    start_date: int = Field(default=None)
    

class VideoChatStarted(TelegramObject):

    """
    This object represents a service message about a video chat started in the chat. Currently holds no information.
    """
    
    pass
    

class VideoChatEnded(TelegramObject):

    """
    This object represents a service message about a video chat ended in the chat.
    """
    
    duration: int = Field(default=None)
    

class VideoChatParticipantsInvited(TelegramObject):

    """
    This object represents a service message about new members invited to a video chat.
    """
    
    users: List["User"] = Field(default=None)
    

class UserProfilePhotos(TelegramObject):

    """
    This object represent a user's profile pictures.
    """
    
    total_count: int = Field(default=None)
    photos: List[List["PhotoSize"]] = Field(default=None)
    

class File(TelegramObject):

    """
    This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.
    """
    
    file_id: str = Field(default=None)
    file_unique_id: str = Field(default=None)
    file_size: int = Field(default=None)
    file_path: str = Field(default=None)
    

class WebAppInfo(TelegramObject):

    """
    Describes a Web App.
    """
    
    url: str = Field(default=None)
    

class KeyboardButtonPollType(TelegramObject):

    """
    This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.
    """
    
    type: str = Field(default=None)
    
    def __init__(self, type: str = None):
        super(KeyboardButtonPollType, self).__init__(type=type)


class ReplyKeyboardRemove(TelegramObject):

    """
    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).
    """
    
    remove_keyboard: bool = Field(default=None)
    selective: bool = Field(default=None)
    
    def __init__(self, remove_keyboard: bool, selective: bool = None):
        super(ReplyKeyboardRemove, self).__init__(remove_keyboard=remove_keyboard, selective=selective)


class LoginUrl(TelegramObject):

    """
    This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:
    Telegram apps support these buttons as of version 5.7.
    """
    
    url: str = Field(default=None)
    forward_text: str = Field(default=None)
    bot_username: str = Field(default=None)
    request_write_access: bool = Field(default=None)
    
    def __init__(self, url: str, forward_text: str = None, bot_username: str = None, request_write_access: bool = None):
        super(LoginUrl, self).__init__(url=url, forward_text=forward_text, bot_username=bot_username, request_write_access=request_write_access)


class ForceReply(TelegramObject):

    """
    Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.
    """
    
    force_reply: bool = Field(default=None)
    input_field_placeholder: str = Field(default=None)
    selective: bool = Field(default=None)
    
    def __init__(self, force_reply: bool, input_field_placeholder: str = None, selective: bool = None):
        super(ForceReply, self).__init__(force_reply=force_reply, input_field_placeholder=input_field_placeholder, selective=selective)


class ChatPhoto(TelegramObject):

    """
    This object represents a chat photo.
    """
    
    small_file_id: str = Field(default=None)
    small_file_unique_id: str = Field(default=None)
    big_file_id: str = Field(default=None)
    big_file_unique_id: str = Field(default=None)
    

class ChatInviteLink(TelegramObject):

    """
    Represents an invite link for a chat.
    """
    
    invite_link: str = Field(default=None)
    creator: "User" = Field(default=None)
    creates_join_request: bool = Field(default=None)
    is_primary: bool = Field(default=None)
    is_revoked: bool = Field(default=None)
    name: str = Field(default=None)
    expire_date: int = Field(default=None)
    member_limit: int = Field(default=None)
    pending_join_request_count: int = Field(default=None)
    

class ChatAdministratorRights(TelegramObject):

    """
    Represents the rights of an administrator in a chat.
    """
    
    is_anonymous: bool = Field(default=None)
    can_manage_chat: bool = Field(default=None)
    can_delete_messages: bool = Field(default=None)
    can_manage_video_chats: bool = Field(default=None)
    can_restrict_members: bool = Field(default=None)
    can_promote_members: bool = Field(default=None)
    can_change_info: bool = Field(default=None)
    can_invite_users: bool = Field(default=None)
    can_post_messages: bool = Field(default=None)
    can_edit_messages: bool = Field(default=None)
    can_pin_messages: bool = Field(default=None)
    

class ChatMember(TelegramObject):

    """
    This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:
    - ChatMemberOwner
    - ChatMemberAdministrator
    - ChatMemberMember
    - ChatMemberRestricted
    - ChatMemberLeft
    - ChatMemberBanned
    """
    
    pass
    

class ChatMemberOwner(ChatMember):

    """
    Represents a chat member that owns the chat and has all administrator privileges.
    """
    
    status: str = Field(default=None)
    user: "User" = Field(default=None)
    is_anonymous: bool = Field(default=None)
    custom_title: str = Field(default=None)
    

class ChatMemberAdministrator(ChatMember):

    """
    Represents a chat member that has some additional privileges.
    """
    
    status: str = Field(default=None)
    user: "User" = Field(default=None)
    can_be_edited: bool = Field(default=None)
    is_anonymous: bool = Field(default=None)
    can_manage_chat: bool = Field(default=None)
    can_delete_messages: bool = Field(default=None)
    can_manage_video_chats: bool = Field(default=None)
    can_restrict_members: bool = Field(default=None)
    can_promote_members: bool = Field(default=None)
    can_change_info: bool = Field(default=None)
    can_invite_users: bool = Field(default=None)
    can_post_messages: bool = Field(default=None)
    can_edit_messages: bool = Field(default=None)
    can_pin_messages: bool = Field(default=None)
    custom_title: str = Field(default=None)
    

class ChatMemberMember(ChatMember):

    """
    Represents a chat member that has no additional privileges or restrictions.
    """
    
    status: str = Field(default=None)
    user: "User" = Field(default=None)
    

class ChatMemberRestricted(ChatMember):

    """
    Represents a chat member that is under certain restrictions in the chat. Supergroups only.
    """
    
    status: str = Field(default=None)
    user: "User" = Field(default=None)
    is_member: bool = Field(default=None)
    can_change_info: bool = Field(default=None)
    can_invite_users: bool = Field(default=None)
    can_pin_messages: bool = Field(default=None)
    can_send_messages: bool = Field(default=None)
    can_send_media_messages: bool = Field(default=None)
    can_send_polls: bool = Field(default=None)
    can_send_other_messages: bool = Field(default=None)
    can_add_web_page_previews: bool = Field(default=None)
    until_date: int = Field(default=None)
    

class ChatMemberLeft(ChatMember):

    """
    Represents a chat member that isn't currently a member of the chat, but may join it themselves.
    """
    
    status: str = Field(default=None)
    user: "User" = Field(default=None)
    

class ChatMemberBanned(ChatMember):

    """
    Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.
    """
    
    status: str = Field(default=None)
    user: "User" = Field(default=None)
    until_date: int = Field(default=None)
    

class ChatMemberUpdated(TelegramObject):

    """
    This object represents changes in the status of a chat member.
    """
    
    chat: "Chat" = Field(default=None)
    from_user: "User" = Field(alias="from", default=None)
    date: int = Field(default=None)
    old_chat_member: "ChatMember" = Field(default=None)
    new_chat_member: "ChatMember" = Field(default=None)
    invite_link: "ChatInviteLink" = Field(default=None)
    

class ChatJoinRequest(TelegramObject):

    """
    Represents a join request sent to a chat.
    """
    
    chat: "Chat" = Field(default=None)
    from_user: "User" = Field(alias="from", default=None)
    date: int = Field(default=None)
    bio: str = Field(default=None)
    invite_link: "ChatInviteLink" = Field(default=None)
    

class ChatPermissions(TelegramObject):

    """
    Describes actions that a non-administrator user is allowed to take in a chat.
    """
    
    can_send_messages: bool = Field(default=None)
    can_send_media_messages: bool = Field(default=None)
    can_send_polls: bool = Field(default=None)
    can_send_other_messages: bool = Field(default=None)
    can_add_web_page_previews: bool = Field(default=None)
    can_change_info: bool = Field(default=None)
    can_invite_users: bool = Field(default=None)
    can_pin_messages: bool = Field(default=None)
    

class ChatLocation(TelegramObject):

    """
    Represents a location to which a chat is connected.
    """
    
    location: "Location" = Field(default=None)
    address: str = Field(default=None)
    

class BotCommand(TelegramObject):

    """
    This object represents a bot command.
    """
    
    command: str = Field(default=None)
    description: str = Field(default=None)
    

class BotCommandScope(TelegramObject):

    """
    This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:
    - BotCommandScopeDefault
    - BotCommandScopeAllPrivateChats
    - BotCommandScopeAllGroupChats
    - BotCommandScopeAllChatAdministrators
    - BotCommandScopeChat
    - BotCommandScopeChatAdministrators
    - BotCommandScopeChatMember
    """
    
    pass
    

class BotCommandScopeDefault(BotCommandScope):

    """
    Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.
    """
    
    type: str = Field(default=None)
    

class BotCommandScopeAllPrivateChats(BotCommandScope):

    """
    Represents the scope of bot commands, covering all private chats.
    """
    
    type: str = Field(default=None)
    

class BotCommandScopeAllGroupChats(BotCommandScope):

    """
    Represents the scope of bot commands, covering all group and supergroup chats.
    """
    
    type: str = Field(default=None)
    

class BotCommandScopeAllChatAdministrators(BotCommandScope):

    """
    Represents the scope of bot commands, covering all group and supergroup chat administrators.
    """
    
    type: str = Field(default=None)
    

class BotCommandScopeChat(BotCommandScope):

    """
    Represents the scope of bot commands, covering a specific chat.
    """
    
    type: str = Field(default=None)
    chat_id: Union[int, str] = Field(default=None)
    

class BotCommandScopeChatAdministrators(BotCommandScope):

    """
    Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.
    """
    
    type: str = Field(default=None)
    chat_id: Union[int, str] = Field(default=None)
    

class BotCommandScopeChatMember(BotCommandScope):

    """
    Represents the scope of bot commands, covering a specific member of a group or supergroup chat.
    """
    
    type: str = Field(default=None)
    chat_id: Union[int, str] = Field(default=None)
    user_id: int = Field(default=None)
    

class MenuButton(TelegramObject):

    """
    This object describes the bot's menu button in a private chat. It should be one of
    - MenuButtonCommands
    - MenuButtonWebApp
    - MenuButtonDefault
    If a menu button other than MenuButtonDefault is set for a private chat, then it is applied in the chat. Otherwise the default menu button is applied. By default, the menu button opens the list of bot commands.
    """
    
    pass
    

class MenuButtonCommands(MenuButton):

    """
    Represents a menu button, which opens the bot's list of commands.
    """
    
    type: str = Field(default=None)
    

class MenuButtonWebApp(MenuButton):

    """
    Represents a menu button, which launches a Web App.
    """
    
    type: str = Field(default=None)
    text: str = Field(default=None)
    web_app: "WebAppInfo" = Field(default=None)
    

class MenuButtonDefault(MenuButton):

    """
    Describes that no specific value for the menu button was set.
    """
    
    type: str = Field(default=None)
    

class ResponseParameters(TelegramObject):

    """
    Describes why a request was unsuccessful.
    """
    
    migrate_to_chat_id: int = Field(default=None)
    retry_after: int = Field(default=None)
    

class InputMedia(TelegramObject):

    """
    This object represents the content of a media message to be sent. It should be one of
    - InputMediaAnimation
    - InputMediaDocument
    - InputMediaAudio
    - InputMediaPhoto
    - InputMediaVideo
    """
    
    pass
    

class InputMediaPhoto(InputMedia):

    """
    Represents a photo to be sent.
    """
    
    type: str = Field(default=None)
    media: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    

class InputFile(TelegramObject):

    """
    This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.
    """
    
    pass
    

class StickerSet(TelegramObject):

    """
    This object represents a sticker set.
    """
    
    name: str = Field(default=None)
    title: str = Field(default=None)
    is_animated: bool = Field(default=None)
    is_video: bool = Field(default=None)
    contains_masks: bool = Field(default=None)
    stickers: List["Sticker"] = Field(default=None)
    thumb: "PhotoSize" = Field(default=None)
    

class MaskPosition(TelegramObject):

    """
    This object describes the position on faces where a mask should be placed by default.
    """
    
    point: str = Field(default=None)
    x_shift: int = Field(default=None)
    y_shift: int = Field(default=None)
    scale: int = Field(default=None)
    

class InlineQuery(TelegramObject):

    """
    This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.
    """
    
    id: str = Field(default=None)
    from_user: "User" = Field(alias="from", default=None)
    query: str = Field(default=None)
    offset: str = Field(default=None)
    chat_type: str = Field(default=None)
    location: "Location" = Field(default=None)
    

class InlineQueryResult(TelegramObject):

    """
    This object represents one result of an inline query. Telegram clients currently support results of the following 20 types:
    - InlineQueryResultCachedAudio
    - InlineQueryResultCachedDocument
    - InlineQueryResultCachedGif
    - InlineQueryResultCachedMpeg4Gif
    - InlineQueryResultCachedPhoto
    - InlineQueryResultCachedSticker
    - InlineQueryResultCachedVideo
    - InlineQueryResultCachedVoice
    - InlineQueryResultArticle
    - InlineQueryResultAudio
    - InlineQueryResultContact
    - InlineQueryResultGame
    - InlineQueryResultDocument
    - InlineQueryResultGif
    - InlineQueryResultLocation
    - InlineQueryResultMpeg4Gif
    - InlineQueryResultPhoto
    - InlineQueryResultVenue
    - InlineQueryResultVideo
    - InlineQueryResultVoice
    Note: All URLs passed in inline query results will be available to end users and therefore must be assumed to be public.
    """
    
    pass
    

class InlineQueryResultGame(InlineQueryResult):

    """
    Represents a Game.
    Note: This will only work in Telegram versions released after October 1, 2016. Older clients will not display any inline results if a game result is among them.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    game_short_name: str = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    

class InputMessageContent(TelegramObject):

    """
    This object represents the content of a message to be sent as a result of an inline query. Telegram clients currently support the following 5 types:
    - InputTextMessageContent
    - InputLocationMessageContent
    - InputVenueMessageContent
    - InputContactMessageContent
    - InputInvoiceMessageContent
    """
    
    pass
    

class InputTextMessageContent(InputMessageContent):

    """
    Represents the content of a text message to be sent as the result of an inline query.
    """
    
    message_text: str = Field(default=None)
    parse_mode: str = Field(default=None)
    entities: List["MessageEntity"] = Field(default=None)
    disable_web_page_preview: bool = Field(default=None)
    

class InputLocationMessageContent(InputMessageContent):

    """
    Represents the content of a location message to be sent as the result of an inline query.
    """
    
    latitude: int = Field(default=None)
    longitude: int = Field(default=None)
    horizontal_accuracy: int = Field(default=None)
    live_period: int = Field(default=None)
    heading: int = Field(default=None)
    proximity_alert_radius: int = Field(default=None)
    

class InputVenueMessageContent(InputMessageContent):

    """
    Represents the content of a venue message to be sent as the result of an inline query.
    """
    
    latitude: int = Field(default=None)
    longitude: int = Field(default=None)
    title: str = Field(default=None)
    address: str = Field(default=None)
    foursquare_id: str = Field(default=None)
    foursquare_type: str = Field(default=None)
    google_place_id: str = Field(default=None)
    google_place_type: str = Field(default=None)
    

class InputContactMessageContent(InputMessageContent):

    """
    Represents the content of a contact message to be sent as the result of an inline query.
    """
    
    phone_number: str = Field(default=None)
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    vcard: str = Field(default=None)
    

class ChosenInlineResult(TelegramObject):

    """
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.
    Note: It is necessary to enable inline feedback via @BotFather in order to receive these objects in updates.
    """
    
    result_id: str = Field(default=None)
    from_user: "User" = Field(alias="from", default=None)
    location: "Location" = Field(default=None)
    inline_message_id: str = Field(default=None)
    query: str = Field(default=None)
    

class SentWebAppMessage(TelegramObject):

    """
    Describes an inline message sent by a Web App on behalf of a user.
    """
    
    inline_message_id: str = Field(default=None)
    

class LabeledPrice(TelegramObject):

    """
    This object represents a portion of the price for goods or services.
    """
    
    label: str = Field(default=None)
    amount: int = Field(default=None)
    

class Invoice(TelegramObject):

    """
    This object contains basic information about an invoice.
    """
    
    title: str = Field(default=None)
    description: str = Field(default=None)
    start_parameter: str = Field(default=None)
    currency: str = Field(default=None)
    total_amount: int = Field(default=None)
    

class ShippingAddress(TelegramObject):

    """
    This object represents a shipping address.
    """
    
    country_code: str = Field(default=None)
    state: str = Field(default=None)
    city: str = Field(default=None)
    street_line1: str = Field(default=None)
    street_line2: str = Field(default=None)
    post_code: str = Field(default=None)
    

class OrderInfo(TelegramObject):

    """
    This object represents information about an order.
    """
    
    name: str = Field(default=None)
    phone_number: str = Field(default=None)
    email: str = Field(default=None)
    shipping_address: "ShippingAddress" = Field(default=None)
    

class ShippingOption(TelegramObject):

    """
    This object represents one shipping option.
    """
    
    id: str = Field(default=None)
    title: str = Field(default=None)
    prices: List["LabeledPrice"] = Field(default=None)
    

class SuccessfulPayment(TelegramObject):

    """
    This object contains basic information about a successful payment.
    """
    
    currency: str = Field(default=None)
    total_amount: int = Field(default=None)
    invoice_payload: str = Field(default=None)
    shipping_option_id: str = Field(default=None)
    order_info: "OrderInfo" = Field(default=None)
    telegram_payment_charge_id: str = Field(default=None)
    provider_payment_charge_id: str = Field(default=None)
    

class ShippingQuery(TelegramObject):

    """
    This object contains information about an incoming shipping query.
    """
    
    id: str = Field(default=None)
    from_user: "User" = Field(alias="from", default=None)
    invoice_payload: str = Field(default=None)
    shipping_address: "ShippingAddress" = Field(default=None)
    

class PreCheckoutQuery(TelegramObject):

    """
    This object contains information about an incoming pre-checkout query.
    """
    
    id: str = Field(default=None)
    from_user: "User" = Field(alias="from", default=None)
    currency: str = Field(default=None)
    total_amount: int = Field(default=None)
    invoice_payload: str = Field(default=None)
    shipping_option_id: str = Field(default=None)
    order_info: "OrderInfo" = Field(default=None)
    

class PassportFile(TelegramObject):

    """
    This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.
    """
    
    file_id: str = Field(default=None)
    file_unique_id: str = Field(default=None)
    file_size: int = Field(default=None)
    file_date: int = Field(default=None)
    

class EncryptedPassportElement(TelegramObject):

    """
    Describes documents or other Telegram Passport elements shared with the bot by the user.
    """
    
    type: str = Field(default=None)
    data: str = Field(default=None)
    phone_number: str = Field(default=None)
    email: str = Field(default=None)
    files: List["PassportFile"] = Field(default=None)
    front_side: "PassportFile" = Field(default=None)
    reverse_side: "PassportFile" = Field(default=None)
    selfie: "PassportFile" = Field(default=None)
    translation: List["PassportFile"] = Field(default=None)
    hash: str = Field(default=None)
    

class EncryptedCredentials(TelegramObject):

    """
    Describes data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.
    """
    
    data: str = Field(default=None)
    hash: str = Field(default=None)
    secret: str = Field(default=None)
    

class PassportElementError(TelegramObject):

    """
    This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:
    - PassportElementErrorDataField
    - PassportElementErrorFrontSide
    - PassportElementErrorReverseSide
    - PassportElementErrorSelfie
    - PassportElementErrorFile
    - PassportElementErrorFiles
    - PassportElementErrorTranslationFile
    - PassportElementErrorTranslationFiles
    - PassportElementErrorUnspecified
    """
    
    pass
    

class PassportElementErrorDataField(PassportElementError):

    """
    Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.
    """
    
    source: str = Field(default=None)
    type: str = Field(default=None)
    field_name: str = Field(default=None)
    data_hash: str = Field(default=None)
    message: str = Field(default=None)
    

class PassportElementErrorFrontSide(PassportElementError):

    """
    Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.
    """
    
    source: str = Field(default=None)
    type: str = Field(default=None)
    file_hash: str = Field(default=None)
    message: str = Field(default=None)
    

class PassportElementErrorReverseSide(PassportElementError):

    """
    Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.
    """
    
    source: str = Field(default=None)
    type: str = Field(default=None)
    file_hash: str = Field(default=None)
    message: str = Field(default=None)
    

class PassportElementErrorSelfie(PassportElementError):

    """
    Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.
    """
    
    source: str = Field(default=None)
    type: str = Field(default=None)
    file_hash: str = Field(default=None)
    message: str = Field(default=None)
    

class PassportElementErrorFile(PassportElementError):

    """
    Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.
    """
    
    source: str = Field(default=None)
    type: str = Field(default=None)
    file_hash: str = Field(default=None)
    message: str = Field(default=None)
    

class PassportElementErrorFiles(PassportElementError):

    """
    Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.
    """
    
    source: str = Field(default=None)
    type: str = Field(default=None)
    file_hashes: List[str] = Field(default=None)
    message: str = Field(default=None)
    

class PassportElementErrorTranslationFile(PassportElementError):

    """
    Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.
    """
    
    source: str = Field(default=None)
    type: str = Field(default=None)
    file_hash: str = Field(default=None)
    message: str = Field(default=None)
    

class PassportElementErrorTranslationFiles(PassportElementError):

    """
    Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.
    """
    
    source: str = Field(default=None)
    type: str = Field(default=None)
    file_hashes: List[str] = Field(default=None)
    message: str = Field(default=None)
    

class PassportElementErrorUnspecified(PassportElementError):

    """
    Represents an issue in an unspecified place. The error is considered resolved when new data is added.
    """
    
    source: str = Field(default=None)
    type: str = Field(default=None)
    element_hash: str = Field(default=None)
    message: str = Field(default=None)
    

class Game(TelegramObject):

    """
    This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.
    """
    
    title: str = Field(default=None)
    description: str = Field(default=None)
    photo: List["PhotoSize"] = Field(default=None)
    text: str = Field(default=None)
    text_entities: List["MessageEntity"] = Field(default=None)
    animation: "Animation" = Field(default=None)
    

class CallbackGame(TelegramObject):

    """
    A placeholder, currently holds no information. Use BotFather to set up your game.
    """
    
    pass
    

class GameHighScore(TelegramObject):

    """
    This object represents one row of the high scores table for a game.
    """
    
    position: int = Field(default=None)
    user: "User" = Field(default=None)
    score: int = Field(default=None)
    

class PassportData(TelegramObject):

    """
    Describes Telegram Passport data shared with the bot by the user.
    """
    
    data: List["EncryptedPassportElement"] = Field(default=None)
    credentials: "EncryptedCredentials" = Field(default=None)
    

class InputInvoiceMessageContent(InputMessageContent):

    """
    Represents the content of an invoice message to be sent as the result of an inline query.
    """
    
    title: str = Field(default=None)
    description: str = Field(default=None)
    payload: str = Field(default=None)
    provider_token: str = Field(default=None)
    currency: str = Field(default=None)
    prices: List["LabeledPrice"] = Field(default=None)
    max_tip_amount: int = Field(default=None)
    suggested_tip_amounts: List[int] = Field(default=None)
    provider_data: str = Field(default=None)
    photo_url: str = Field(default=None)
    photo_size: int = Field(default=None)
    photo_width: int = Field(default=None)
    photo_height: int = Field(default=None)
    need_name: bool = Field(default=None)
    need_phone_number: bool = Field(default=None)
    need_email: bool = Field(default=None)
    need_shipping_address: bool = Field(default=None)
    send_phone_number_to_provider: bool = Field(default=None)
    send_email_to_provider: bool = Field(default=None)
    is_flexible: bool = Field(default=None)
    

class InlineQueryResultCachedAudio(InlineQueryResult):

    """
    Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    audio_file_id: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    

class InlineQueryResultCachedVoice(InlineQueryResult):

    """
    Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    voice_file_id: str = Field(default=None)
    title: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    

class InlineQueryResultCachedVideo(InlineQueryResult):

    """
    Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    video_file_id: str = Field(default=None)
    title: str = Field(default=None)
    description: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    

class InlineQueryResultCachedDocument(InlineQueryResult):

    """
    Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    title: str = Field(default=None)
    document_file_id: str = Field(default=None)
    description: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    

class InlineQueryResultCachedSticker(InlineQueryResult):

    """
    Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
    Note: This will only work in Telegram versions released after 9 April, 2016 for static stickers and after 06 July, 2019 for animated stickers. Older clients will ignore them.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    sticker_file_id: str = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    

class InlineQueryResultCachedMpeg4Gif(InlineQueryResult):

    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    mpeg4_file_id: str = Field(default=None)
    title: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    

class InlineQueryResultCachedGif(InlineQueryResult):

    """
    Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    gif_file_id: str = Field(default=None)
    title: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    

class InlineQueryResultCachedPhoto(InlineQueryResult):

    """
    Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    photo_file_id: str = Field(default=None)
    title: str = Field(default=None)
    description: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    

class InlineQueryResultContact(InlineQueryResult):

    """
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    phone_number: str = Field(default=None)
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    vcard: str = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    thumb_url: str = Field(default=None)
    thumb_width: int = Field(default=None)
    thumb_height: int = Field(default=None)
    

class InlineQueryResultVenue(InlineQueryResult):

    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    latitude: int = Field(default=None)
    longitude: int = Field(default=None)
    title: str = Field(default=None)
    address: str = Field(default=None)
    foursquare_id: str = Field(default=None)
    foursquare_type: str = Field(default=None)
    google_place_id: str = Field(default=None)
    google_place_type: str = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    thumb_url: str = Field(default=None)
    thumb_width: int = Field(default=None)
    thumb_height: int = Field(default=None)
    

class InlineQueryResultLocation(InlineQueryResult):

    """
    Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    latitude: int = Field(default=None)
    longitude: int = Field(default=None)
    title: str = Field(default=None)
    horizontal_accuracy: int = Field(default=None)
    live_period: int = Field(default=None)
    heading: int = Field(default=None)
    proximity_alert_radius: int = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    thumb_url: str = Field(default=None)
    thumb_width: int = Field(default=None)
    thumb_height: int = Field(default=None)
    

class InlineQueryResultDocument(InlineQueryResult):

    """
    Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    title: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    document_url: str = Field(default=None)
    mime_type: str = Field(default=None)
    description: str = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    thumb_url: str = Field(default=None)
    thumb_width: int = Field(default=None)
    thumb_height: int = Field(default=None)
    

class InlineQueryResultVoice(InlineQueryResult):

    """
    Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    voice_url: str = Field(default=None)
    title: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    voice_duration: int = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    

class InlineQueryResultAudio(InlineQueryResult):

    """
    Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    audio_url: str = Field(default=None)
    title: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    performer: str = Field(default=None)
    audio_duration: int = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    

class InlineQueryResultVideo(InlineQueryResult):

    """
    Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    video_url: str = Field(default=None)
    mime_type: str = Field(default=None)
    thumb_url: str = Field(default=None)
    title: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    video_width: int = Field(default=None)
    video_height: int = Field(default=None)
    video_duration: int = Field(default=None)
    description: str = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    

class InlineQueryResultMpeg4Gif(InlineQueryResult):

    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    mpeg4_url: str = Field(default=None)
    mpeg4_width: int = Field(default=None)
    mpeg4_height: int = Field(default=None)
    mpeg4_duration: int = Field(default=None)
    thumb_url: str = Field(default=None)
    thumb_mime_type: str = Field(default=None)
    title: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    

class InlineQueryResultGif(InlineQueryResult):

    """
    Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    gif_url: str = Field(default=None)
    gif_width: int = Field(default=None)
    gif_height: int = Field(default=None)
    gif_duration: int = Field(default=None)
    thumb_url: str = Field(default=None)
    thumb_mime_type: str = Field(default=None)
    title: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    

class InlineQueryResultPhoto(InlineQueryResult):

    """
    Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    photo_url: str = Field(default=None)
    thumb_url: str = Field(default=None)
    photo_width: int = Field(default=None)
    photo_height: int = Field(default=None)
    title: str = Field(default=None)
    description: str = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    

class InlineQueryResultArticle(InlineQueryResult):

    """
    Represents a link to an article or web page.
    """
    
    type: str = Field(default=None)
    id: str = Field(default=None)
    title: str = Field(default=None)
    input_message_content: "InputMessageContent" = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    url: str = Field(default=None)
    hide_url: bool = Field(default=None)
    description: str = Field(default=None)
    thumb_url: str = Field(default=None)
    thumb_width: int = Field(default=None)
    thumb_height: int = Field(default=None)
    

class Sticker(TelegramObject):

    """
    This object represents a sticker.
    """
    
    file_id: str = Field(default=None)
    file_unique_id: str = Field(default=None)
    width: int = Field(default=None)
    height: int = Field(default=None)
    is_animated: bool = Field(default=None)
    is_video: bool = Field(default=None)
    thumb: "PhotoSize" = Field(default=None)
    emoji: str = Field(default=None)
    set_name: str = Field(default=None)
    premium_animation: "File" = Field(default=None)
    mask_position: "MaskPosition" = Field(default=None)
    file_size: int = Field(default=None)
    

class InputMediaDocument(InputMedia):

    """
    Represents a general file to be sent.
    """
    
    type: str = Field(default=None)
    media: str = Field(default=None)
    thumb: Union["InputFile", str] = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    disable_content_type_detection: bool = Field(default=None)
    

class InputMediaAudio(InputMedia):

    """
    Represents an audio file to be treated as music to be sent.
    """
    
    type: str = Field(default=None)
    media: str = Field(default=None)
    thumb: Union["InputFile", str] = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    duration: int = Field(default=None)
    performer: str = Field(default=None)
    title: str = Field(default=None)
    

class InputMediaAnimation(InputMedia):

    """
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.
    """
    
    type: str = Field(default=None)
    media: str = Field(default=None)
    thumb: Union["InputFile", str] = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    width: int = Field(default=None)
    height: int = Field(default=None)
    duration: int = Field(default=None)
    

class InputMediaVideo(InputMedia):

    """
    Represents a video to be sent.
    """
    
    type: str = Field(default=None)
    media: str = Field(default=None)
    thumb: Union["InputFile", str] = Field(default=None)
    caption: str = Field(default=None)
    parse_mode: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    width: int = Field(default=None)
    height: int = Field(default=None)
    duration: int = Field(default=None)
    supports_streaming: bool = Field(default=None)
    

class InlineKeyboardButton(TelegramObject):

    """
    This object represents one button of an inline keyboard. You must use exactly one of the optional fields.
    """
    
    text: str = Field(default=None)
    url: str = Field(default=None)
    callback_data: str = Field(default=None)
    web_app: "WebAppInfo" = Field(default=None)
    login_url: "LoginUrl" = Field(default=None)
    switch_inline_query: str = Field(default=None)
    switch_inline_query_current_chat: str = Field(default=None)
    callback_game: "CallbackGame" = Field(default=None)
    pay: bool = Field(default=None)
    
    def __init__(self, text: str, url: str = "", callback_data: str = None, web_app: "WebAppInfo" = None, login_url: "LoginUrl" = None, switch_inline_query: str = None, switch_inline_query_current_chat: str = None, callback_game: "CallbackGame" = None, pay: bool = None):
        super(InlineKeyboardButton, self).__init__(text=text, url=url, callback_data=callback_data, web_app=web_app, login_url=login_url, switch_inline_query=switch_inline_query, switch_inline_query_current_chat=switch_inline_query_current_chat, callback_game=callback_game, pay=pay)


class InlineKeyboardMarkup(TelegramObject):

    """
    This object represents an inline keyboard that appears right next to the message it belongs to.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.
    """
    
    inline_keyboard: List[List["InlineKeyboardButton"]] = Field(default=None)
    
    def __init__(self, inline_keyboard: List[List["InlineKeyboardButton"]]):
        super(InlineKeyboardMarkup, self).__init__(inline_keyboard=inline_keyboard)


class KeyboardButton(TelegramObject):

    """
    This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields web_app, request_contact, request_location, and request_poll are mutually exclusive.
    Note: request_contact and request_location options will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.
    Note: request_poll option will only work in Telegram versions released after 23 January, 2020. Older clients will display unsupported message.
    Note: web_app option will only work in Telegram versions released after 16 April, 2022. Older clients will display unsupported message.
    """
    
    text: str = Field(default=None)
    request_contact: bool = Field(default=None)
    request_location: bool = Field(default=None)
    request_poll: "KeyboardButtonPollType" = Field(default=None)
    web_app: "WebAppInfo" = Field(default=None)
    
    def __init__(self, text: str, request_contact: bool = None, request_location: bool = None, request_poll: "KeyboardButtonPollType" = None, web_app: "WebAppInfo" = None):
        super(KeyboardButton, self).__init__(text=text, request_contact=request_contact, request_location=request_location, request_poll=request_poll, web_app=web_app)


class ReplyKeyboardMarkup(TelegramObject):

    """
    This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).
    """
    
    keyboard: List[List["KeyboardButton"]] = Field(default=None)
    resize_keyboard: bool = Field(default=None)
    one_time_keyboard: bool = Field(default=None)
    input_field_placeholder: str = Field(default=None)
    selective: bool = Field(default=None)
    
    def __init__(self, keyboard: List[List["KeyboardButton"]], resize_keyboard: bool = None, one_time_keyboard: bool = None, input_field_placeholder: str = None, selective: bool = None):
        super(ReplyKeyboardMarkup, self).__init__(keyboard=keyboard, resize_keyboard=resize_keyboard, one_time_keyboard=one_time_keyboard, input_field_placeholder=input_field_placeholder, selective=selective)


class Chat(TelegramObject):

    """
    This object represents a chat.
    """
    
    id: int = Field(default=None)
    type: str = Field(default=None)
    title: str = Field(default=None)
    username: str = Field(default=None)
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    photo: "ChatPhoto" = Field(default=None)
    bio: str = Field(default=None)
    has_private_forwards: bool = Field(default=None)
    join_to_send_messages: bool = Field(default=None)
    join_by_request: bool = Field(default=None)
    description: str = Field(default=None)
    invite_link: str = Field(default=None)
    pinned_message: "Message" = Field(default=None)
    permissions: "ChatPermissions" = Field(default=None)
    slow_mode_delay: int = Field(default=None)
    message_auto_delete_time: int = Field(default=None)
    has_protected_content: bool = Field(default=None)
    sticker_set_name: str = Field(default=None)
    can_set_sticker_set: bool = Field(default=None)
    linked_chat_id: int = Field(default=None)
    location: "ChatLocation" = Field(default=None)
    

class Message(TelegramObject):

    """
    This object represents a message.
    """
    
    message_id: int = Field(default=None)
    from_user: "User" = Field(alias="from", default=None)
    sender_chat: "Chat" = Field(default=None)
    date: int = Field(default=None)
    chat: "Chat" = Field(default=None)
    forward_from: "User" = Field(default=None)
    forward_from_chat: "Chat" = Field(default=None)
    forward_from_message_id: int = Field(default=None)
    forward_signature: str = Field(default=None)
    forward_sender_name: str = Field(default=None)
    forward_date: int = Field(default=None)
    is_automatic_forward: bool = Field(default=None)
    reply_to_message: "Message" = Field(default=None)
    via_bot: "User" = Field(default=None)
    edit_date: int = Field(default=None)
    has_protected_content: bool = Field(default=None)
    media_group_id: str = Field(default=None)
    author_signature: str = Field(default=None)
    text: str = Field(default=None)
    entities: List["MessageEntity"] = Field(default=None)
    animation: "Animation" = Field(default=None)
    audio: "Audio" = Field(default=None)
    document: "Document" = Field(default=None)
    photo: List["PhotoSize"] = Field(default=None)
    sticker: "Sticker" = Field(default=None)
    video: "Video" = Field(default=None)
    video_note: "VideoNote" = Field(default=None)
    voice: "Voice" = Field(default=None)
    caption: str = Field(default=None)
    caption_entities: List["MessageEntity"] = Field(default=None)
    contact: "Contact" = Field(default=None)
    dice: "Dice" = Field(default=None)
    game: "Game" = Field(default=None)
    poll: "Poll" = Field(default=None)
    venue: "Venue" = Field(default=None)
    location: "Location" = Field(default=None)
    new_chat_members: List["User"] = Field(default=None)
    left_chat_member: "User" = Field(default=None)
    new_chat_title: str = Field(default=None)
    new_chat_photo: List["PhotoSize"] = Field(default=None)
    delete_chat_photo: bool = Field(default=None)
    group_chat_created: bool = Field(default=None)
    supergroup_chat_created: bool = Field(default=None)
    channel_chat_created: bool = Field(default=None)
    message_auto_delete_timer_changed: "MessageAutoDeleteTimerChanged" = Field(default=None)
    migrate_to_chat_id: int = Field(default=None)
    migrate_from_chat_id: int = Field(default=None)
    pinned_message: "Message" = Field(default=None)
    invoice: "Invoice" = Field(default=None)
    successful_payment: "SuccessfulPayment" = Field(default=None)
    connected_website: str = Field(default=None)
    passport_data: "PassportData" = Field(default=None)
    proximity_alert_triggered: "ProximityAlertTriggered" = Field(default=None)
    video_chat_scheduled: "VideoChatScheduled" = Field(default=None)
    video_chat_started: "VideoChatStarted" = Field(default=None)
    video_chat_ended: "VideoChatEnded" = Field(default=None)
    video_chat_participants_invited: "VideoChatParticipantsInvited" = Field(default=None)
    web_app_data: "WebAppData" = Field(default=None)
    reply_markup: "InlineKeyboardMarkup" = Field(default=None)
    

class CallbackQuery(TelegramObject):

    """
    This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.
    """
    
    id: str = Field(default=None)
    from_user: "User" = Field(alias="from", default=None)
    message: "Message" = Field(default=None)
    inline_message_id: str = Field(default=None)
    chat_instance: str = Field(default=None)
    data: str = Field(default=None)
    game_short_name: str = Field(default=None)
    

class Update(TelegramObject):

    """
    This object represents an incoming update.
    At most one of the optional parameters can be present in any given update.
    """
    
    update_id: int = Field(default=None)
    message: "Message" = Field(default=None)
    edited_message: "Message" = Field(default=None)
    channel_post: "Message" = Field(default=None)
    edited_channel_post: "Message" = Field(default=None)
    inline_query: "InlineQuery" = Field(default=None)
    chosen_inline_result: "ChosenInlineResult" = Field(default=None)
    callback_query: "CallbackQuery" = Field(default=None)
    shipping_query: "ShippingQuery" = Field(default=None)
    pre_checkout_query: "PreCheckoutQuery" = Field(default=None)
    poll: "Poll" = Field(default=None)
    poll_answer: "PollAnswer" = Field(default=None)
    my_chat_member: "ChatMemberUpdated" = Field(default=None)
    chat_member: "ChatMemberUpdated" = Field(default=None)
    chat_join_request: "ChatJoinRequest" = Field(default=None)
    

