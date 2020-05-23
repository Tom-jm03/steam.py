# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_parental.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class ParentalApp(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    is_allowed: bool = betterproto.bool_field(2)


@dataclass
class ParentalSettings(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    applist_base_id: int = betterproto.uint32_field(2)
    applist_base_description: str = betterproto.string_field(3)
    applist_base: List["ParentalApp"] = betterproto.message_field(4)
    applist_custom: List["ParentalApp"] = betterproto.message_field(5)
    passwordhashtype: int = betterproto.uint32_field(6)
    salt: bytes = betterproto.bytes_field(7)
    passwordhash: bytes = betterproto.bytes_field(8)
    is_enabled: bool = betterproto.bool_field(9)
    enabled_features: int = betterproto.uint32_field(10)
    recovery_email: str = betterproto.string_field(11)
    is_site_license_lock: bool = betterproto.bool_field(12)


@dataclass
class CParental_EnableParentalSettings_Request(betterproto.Message):
    password: str = betterproto.string_field(1)
    settings: "ParentalSettings" = betterproto.message_field(2)
    sessionid: str = betterproto.string_field(3)
    enablecode: int = betterproto.uint32_field(4)
    steamid: float = betterproto.fixed64_field(10)


@dataclass
class CParental_EnableParentalSettings_Response(betterproto.Message):
    pass


@dataclass
class CParental_DisableParentalSettings_Request(betterproto.Message):
    password: str = betterproto.string_field(1)
    steamid: float = betterproto.fixed64_field(10)


@dataclass
class CParental_DisableParentalSettings_Response(betterproto.Message):
    pass


@dataclass
class CParental_GetParentalSettings_Request(betterproto.Message):
    steamid: float = betterproto.fixed64_field(10)


@dataclass
class CParental_GetParentalSettings_Response(betterproto.Message):
    settings: "ParentalSettings" = betterproto.message_field(1)


@dataclass
class CParental_GetSignedParentalSettings_Request(betterproto.Message):
    priority: int = betterproto.uint32_field(1)


@dataclass
class CParental_GetSignedParentalSettings_Response(betterproto.Message):
    serialized_settings: bytes = betterproto.bytes_field(1)
    signature: bytes = betterproto.bytes_field(2)


@dataclass
class CParental_SetParentalSettings_Request(betterproto.Message):
    password: str = betterproto.string_field(1)
    settings: "ParentalSettings" = betterproto.message_field(2)
    new_password: str = betterproto.string_field(3)
    sessionid: str = betterproto.string_field(4)
    steamid: float = betterproto.fixed64_field(10)


@dataclass
class CParental_SetParentalSettings_Response(betterproto.Message):
    pass


@dataclass
class CParental_ValidateToken_Request(betterproto.Message):
    unlock_token: str = betterproto.string_field(1)


@dataclass
class CParental_ValidateToken_Response(betterproto.Message):
    pass


@dataclass
class CParental_ValidatePassword_Request(betterproto.Message):
    password: str = betterproto.string_field(1)
    session: str = betterproto.string_field(2)
    send_unlock_on_success: bool = betterproto.bool_field(3)


@dataclass
class CParental_ValidatePassword_Response(betterproto.Message):
    token: str = betterproto.string_field(1)


@dataclass
class CParental_LockClient_Request(betterproto.Message):
    session: str = betterproto.string_field(1)


@dataclass
class CParental_LockClient_Response(betterproto.Message):
    pass


@dataclass
class CParental_RequestRecoveryCode_Request(betterproto.Message):
    pass


@dataclass
class CParental_RequestRecoveryCode_Response(betterproto.Message):
    pass


@dataclass
class CParental_DisableWithRecoveryCode_Request(betterproto.Message):
    recovery_code: int = betterproto.uint32_field(1)
    steamid: float = betterproto.fixed64_field(10)


@dataclass
class CParental_DisableWithRecoveryCode_Response(betterproto.Message):
    pass


@dataclass
class CParental_ParentalSettingsChange_Notification(betterproto.Message):
    serialized_settings: bytes = betterproto.bytes_field(1)
    signature: bytes = betterproto.bytes_field(2)
    password: str = betterproto.string_field(3)
    sessionid: str = betterproto.string_field(4)


@dataclass
class CParental_ParentalUnlock_Notification(betterproto.Message):
    password: str = betterproto.string_field(1)
    sessionid: str = betterproto.string_field(2)


@dataclass
class CParental_ParentalLock_Notification(betterproto.Message):
    sessionid: str = betterproto.string_field(1)
