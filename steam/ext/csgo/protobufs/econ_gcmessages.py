# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: econ_gcmessages.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto


@dataclass(eq=False, repr=False)
class CMsgGcGiftedItems(betterproto.Message):
    accountid: int = betterproto.uint32_field(1)
    giftdefindex: int = betterproto.uint32_field(2)
    max_gifts_possible: int = betterproto.uint32_field(3)
    num_eligible_recipients: int = betterproto.uint32_field(4)
    recipients_accountids: List[int] = betterproto.uint32_field(5)


@dataclass(eq=False, repr=False)
class CMsgApplyAutograph(betterproto.Message):
    autograph_item_id: int = betterproto.uint64_field(1)
    item_item_id: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class CMsgCasketItem(betterproto.Message):
    casket_item_id: int = betterproto.uint64_field(1)
    item_item_id: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class CMsgGcUserTrackTimePlayedConsecutively(betterproto.Message):
    state: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcItemCustomizationNotification(betterproto.Message):
    item_id: List[int] = betterproto.uint64_field(1)
    request: int = betterproto.uint32_field(2)