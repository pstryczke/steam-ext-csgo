# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: base_gcmessages.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto


class EgcBaseProtoObjectTypes(betterproto.Enum):
    PartyInvite = 1001
    LobbyInvite = 1002


class GcBannedWordType(betterproto.Enum):
    DisableWord = 0
    EnableWord = 1


class CMsgGameServerInfoServerType(betterproto.Enum):
    Unspecified = 0
    Game = 1
    Proxy = 2


@dataclass(eq=False, repr=False)
class CgcStorePurchaseInitLineItem(betterproto.Message):
    item_def_id: int = betterproto.uint32_field(1)
    quantity: int = betterproto.uint32_field(2)
    cost_in_local_currency: int = betterproto.uint32_field(3)
    purchase_type: int = betterproto.uint32_field(4)


@dataclass(eq=False, repr=False)
class CMsgGcStorePurchaseInit(betterproto.Message):
    country: str = betterproto.string_field(1)
    language: int = betterproto.int32_field(2)
    currency: int = betterproto.int32_field(3)
    line_items: List["CgcStorePurchaseInitLineItem"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class CMsgGcStorePurchaseInitResponse(betterproto.Message):
    result: int = betterproto.int32_field(1)
    txn_id: int = betterproto.uint64_field(2)
    url: str = betterproto.string_field(3)
    item_ids: List[int] = betterproto.uint64_field(4)


@dataclass(eq=False, repr=False)
class CsoPartyInvite(betterproto.Message):
    group_id: int = betterproto.uint64_field(1)
    sender_id: int = betterproto.fixed64_field(2)
    sender_name: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class CsoLobbyInvite(betterproto.Message):
    group_id: int = betterproto.uint64_field(1)
    sender_id: int = betterproto.fixed64_field(2)
    sender_name: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class CMsgSystemBroadcast(betterproto.Message):
    message: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class CMsgInviteToParty(betterproto.Message):
    steam_id: int = betterproto.fixed64_field(1)
    client_version: int = betterproto.uint32_field(2)
    team_invite: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class CMsgInvitationCreated(betterproto.Message):
    group_id: int = betterproto.uint64_field(1)
    steam_id: int = betterproto.fixed64_field(2)


@dataclass(eq=False, repr=False)
class CMsgPartyInviteResponse(betterproto.Message):
    party_id: int = betterproto.uint64_field(1)
    accept: bool = betterproto.bool_field(2)
    client_version: int = betterproto.uint32_field(3)
    team_invite: int = betterproto.uint32_field(4)


@dataclass(eq=False, repr=False)
class CMsgKickFromParty(betterproto.Message):
    steam_id: int = betterproto.fixed64_field(1)


@dataclass(eq=False, repr=False)
class CMsgLeaveParty(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CMsgServerAvailable(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CMsgLanServerAvailable(betterproto.Message):
    lobby_id: int = betterproto.fixed64_field(1)


@dataclass(eq=False, repr=False)
class CsoEconGameAccountClient(betterproto.Message):
    additional_backpack_slots: int = betterproto.uint32_field(1)
    bonus_xp_timestamp_refresh: int = betterproto.fixed32_field(12)
    bonus_xp_usedflags: int = betterproto.uint32_field(13)
    elevated_state: int = betterproto.uint32_field(14)
    elevated_timestamp: int = betterproto.uint32_field(15)


@dataclass(eq=False, repr=False)
class CsoItemCriteriaCondition(betterproto.Message):
    op: int = betterproto.int32_field(1)
    field: str = betterproto.string_field(2)
    required: bool = betterproto.bool_field(3)
    float_value: float = betterproto.float_field(4)
    string_value: str = betterproto.string_field(5)


@dataclass(eq=False, repr=False)
class CsoItemCriteria(betterproto.Message):
    item_level: int = betterproto.uint32_field(1)
    item_quality: int = betterproto.int32_field(2)
    item_level_set: bool = betterproto.bool_field(3)
    item_quality_set: bool = betterproto.bool_field(4)
    initial_inventory: int = betterproto.uint32_field(5)
    initial_quantity: int = betterproto.uint32_field(6)
    ignore_enabled_flag: bool = betterproto.bool_field(8)
    conditions: List["CsoItemCriteriaCondition"] = betterproto.message_field(9)
    item_rarity: int = betterproto.int32_field(10)
    item_rarity_set: bool = betterproto.bool_field(11)
    recent_only: bool = betterproto.bool_field(12)


@dataclass(eq=False, repr=False)
class CsoItemRecipe(betterproto.Message):
    def_index: int = betterproto.uint32_field(1)
    name: str = betterproto.string_field(2)
    n_a: str = betterproto.string_field(3)
    desc_inputs: str = betterproto.string_field(4)
    desc_outputs: str = betterproto.string_field(5)
    di_a: str = betterproto.string_field(6)
    di_b: str = betterproto.string_field(7)
    di_c: str = betterproto.string_field(8)
    do_a: str = betterproto.string_field(9)
    do_b: str = betterproto.string_field(10)
    do_c: str = betterproto.string_field(11)
    requires_all_same_class: bool = betterproto.bool_field(12)
    requires_all_same_slot: bool = betterproto.bool_field(13)
    class_usage_for_output: int = betterproto.int32_field(14)
    slot_usage_for_output: int = betterproto.int32_field(15)
    set_for_output: int = betterproto.int32_field(16)
    input_items_criteria: List["CsoItemCriteria"] = betterproto.message_field(20)
    output_items_criteria: List["CsoItemCriteria"] = betterproto.message_field(21)
    input_item_dupe_counts: List[int] = betterproto.uint32_field(22)


@dataclass(eq=False, repr=False)
class CMsgDevNewItemRequest(betterproto.Message):
    receiver: int = betterproto.fixed64_field(1)
    criteria: "CsoItemCriteria" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CMsgIncrementKillCountAttribute(betterproto.Message):
    killer_account_id: int = betterproto.fixed32_field(1)
    victim_account_id: int = betterproto.fixed32_field(2)
    item_id: int = betterproto.uint64_field(3)
    event_type: int = betterproto.uint32_field(4)
    amount: int = betterproto.uint32_field(5)


@dataclass(eq=False, repr=False)
class CMsgApplySticker(betterproto.Message):
    sticker_item_id: int = betterproto.uint64_field(1)
    item_item_id: int = betterproto.uint64_field(2)
    sticker_slot: int = betterproto.uint32_field(3)
    baseitem_defidx: int = betterproto.uint32_field(4)
    sticker_wear: float = betterproto.float_field(5)


@dataclass(eq=False, repr=False)
class CMsgModifyItemAttribute(betterproto.Message):
    item_id: int = betterproto.uint64_field(1)
    attr_defidx: int = betterproto.uint32_field(2)
    attr_value: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class CMsgApplyStatTrakSwap(betterproto.Message):
    tool_item_id: int = betterproto.uint64_field(1)
    item_1_item_id: int = betterproto.uint64_field(2)
    item_2_item_id: int = betterproto.uint64_field(3)


@dataclass(eq=False, repr=False)
class CMsgApplyStrangePart(betterproto.Message):
    strange_part_item_id: int = betterproto.uint64_field(1)
    item_item_id: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class CMsgApplyPennantUpgrade(betterproto.Message):
    upgrade_item_id: int = betterproto.uint64_field(1)
    pennant_item_id: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class CMsgApplyEggEssence(betterproto.Message):
    essence_item_id: int = betterproto.uint64_field(1)
    egg_item_id: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class CsoEconItemAttribute(betterproto.Message):
    def_index: int = betterproto.uint32_field(1)
    value: int = betterproto.uint32_field(2)
    value_bytes: bytes = betterproto.bytes_field(3)


@dataclass(eq=False, repr=False)
class CsoEconItemEquipped(betterproto.Message):
    new_class: int = betterproto.uint32_field(1)
    new_slot: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CsoEconItem(betterproto.Message):
    id: int = betterproto.uint64_field(1)
    account_id: int = betterproto.uint32_field(2)
    inventory: int = betterproto.uint32_field(3)
    def_index: int = betterproto.uint32_field(4)
    quantity: int = betterproto.uint32_field(5)
    level: int = betterproto.uint32_field(6)
    quality: int = betterproto.uint32_field(7)
    flags: int = betterproto.uint32_field(8)
    origin: int = betterproto.uint32_field(9)
    custom_name: str = betterproto.string_field(10)
    custom_desc: str = betterproto.string_field(11)
    attribute: List["CsoEconItemAttribute"] = betterproto.message_field(12)
    interior_item: "CsoEconItem" = betterproto.message_field(13)
    in_use: bool = betterproto.bool_field(14)
    style: int = betterproto.uint32_field(15)
    original_id: int = betterproto.uint64_field(16)
    equipped_state: List["CsoEconItemEquipped"] = betterproto.message_field(18)
    rarity: int = betterproto.uint32_field(19)


@dataclass(eq=False, repr=False)
class CMsgAdjustItemEquippedState(betterproto.Message):
    item_id: int = betterproto.uint64_field(1)
    new_class: int = betterproto.uint32_field(2)
    new_slot: int = betterproto.uint32_field(3)
    swap: bool = betterproto.bool_field(4)


@dataclass(eq=False, repr=False)
class CMsgAdjustItemEquippedStateMulti(betterproto.Message):
    t_equips: List[int] = betterproto.uint64_field(1)
    ct_equips: List[int] = betterproto.uint64_field(2)
    noteam_equips: List[int] = betterproto.uint64_field(3)


@dataclass(eq=False, repr=False)
class CMsgSortItems(betterproto.Message):
    sort_type: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class CsoEconClaimCode(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    code_type: int = betterproto.uint32_field(2)
    time_acquired: int = betterproto.uint32_field(3)
    code: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class CMsgStoreGetUserData(betterproto.Message):
    price_sheet_version: int = betterproto.fixed32_field(1)
    currency: int = betterproto.int32_field(2)


@dataclass(eq=False, repr=False)
class CMsgStoreGetUserDataResponse(betterproto.Message):
    result: int = betterproto.int32_field(1)
    currency_deprecated: int = betterproto.int32_field(2)
    country_deprecated: str = betterproto.string_field(3)
    price_sheet_version: int = betterproto.fixed32_field(4)
    price_sheet: bytes = betterproto.bytes_field(8)


@dataclass(eq=False, repr=False)
class CMsgUpdateItemSchema(betterproto.Message):
    items_game: bytes = betterproto.bytes_field(1)
    item_schema_version: int = betterproto.fixed32_field(2)
    items_game_url_deprecated2013: str = betterproto.string_field(3)
    items_game_url: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class CMsgGcError(betterproto.Message):
    error_text: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class CMsgRequestInventoryRefresh(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CMsgConVarValue(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class CMsgReplicateConVars(betterproto.Message):
    convars: List["CMsgConVarValue"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class CMsgUseItem(betterproto.Message):
    item_id: int = betterproto.uint64_field(1)
    target_steam_id: int = betterproto.fixed64_field(2)
    gift_potential_targets: List[int] = betterproto.uint32_field(3)
    duel_class_lock: int = betterproto.uint32_field(4)
    initiator_steam_id: int = betterproto.fixed64_field(5)


@dataclass(eq=False, repr=False)
class CMsgReplayUploadedToYouTube(betterproto.Message):
    youtube_url: str = betterproto.string_field(1)
    youtube_account_name: str = betterproto.string_field(2)
    session_id: int = betterproto.uint64_field(3)


@dataclass(eq=False, repr=False)
class CMsgConsumableExhausted(betterproto.Message):
    item_def_id: int = betterproto.int32_field(1)


@dataclass(eq=False, repr=False)
class CMsgItemAcknowledgedDeprecated(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    inventory: int = betterproto.uint32_field(2)
    def_index: int = betterproto.uint32_field(3)
    quality: int = betterproto.uint32_field(4)
    rarity: int = betterproto.uint32_field(5)
    origin: int = betterproto.uint32_field(6)
    item_id: int = betterproto.uint64_field(7)


@dataclass(eq=False, repr=False)
class CMsgSetItemPositions(betterproto.Message):
    item_positions: List["CMsgSetItemPositionsItemPosition"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class CMsgSetItemPositionsItemPosition(betterproto.Message):
    legacy_item_id: int = betterproto.uint32_field(1)
    position: int = betterproto.uint32_field(2)
    item_id: int = betterproto.uint64_field(3)


@dataclass(eq=False, repr=False)
class CMsgGcReportAbuse(betterproto.Message):
    target_steam_id: int = betterproto.fixed64_field(1)
    description: str = betterproto.string_field(4)
    gid: int = betterproto.uint64_field(5)
    abuse_type: int = betterproto.uint32_field(2)
    content_type: int = betterproto.uint32_field(3)
    target_game_server_ip: int = betterproto.fixed32_field(6)
    target_game_server_port: int = betterproto.uint32_field(7)


@dataclass(eq=False, repr=False)
class CMsgGcReportAbuseResponse(betterproto.Message):
    target_steam_id: int = betterproto.fixed64_field(1)
    result: int = betterproto.uint32_field(2)
    error_message: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class CMsgGcNameItemNotification(betterproto.Message):
    player_steamid: int = betterproto.fixed64_field(1)
    item_def_index: int = betterproto.uint32_field(2)
    item_name_custom: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class CMsgGcClientDisplayNotification(betterproto.Message):
    notification_title_localization_key: str = betterproto.string_field(1)
    notification_body_localization_key: str = betterproto.string_field(2)
    body_substring_keys: List[str] = betterproto.string_field(3)
    body_substring_values: List[str] = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class CMsgGcShowItemsPickedUp(betterproto.Message):
    player_steamid: int = betterproto.fixed64_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcIncrementKillCountResponse(betterproto.Message):
    killer_account_id: int = betterproto.uint32_field(1)
    num_kills: int = betterproto.uint32_field(2)
    item_def: int = betterproto.uint32_field(3)
    level_type: int = betterproto.uint32_field(4)


@dataclass(eq=False, repr=False)
class CsoEconItemDropRateBonus(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    expiration_date: int = betterproto.fixed32_field(2)
    bonus: float = betterproto.float_field(3)
    bonus_count: int = betterproto.uint32_field(4)
    item_id: int = betterproto.uint64_field(5)
    def_index: int = betterproto.uint32_field(6)


@dataclass(eq=False, repr=False)
class CsoEconItemLeagueViewPass(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    league_id: int = betterproto.uint32_field(2)
    admin: int = betterproto.uint32_field(3)
    itemindex: int = betterproto.uint32_field(4)


@dataclass(eq=False, repr=False)
class CsoEconItemEventTicket(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    event_id: int = betterproto.uint32_field(2)
    item_id: int = betterproto.uint64_field(3)


@dataclass(eq=False, repr=False)
class CMsgGcItemPreviewItemBoughtNotification(betterproto.Message):
    item_def_index: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcStorePurchaseCancel(betterproto.Message):
    txn_id: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcStorePurchaseCancelResponse(betterproto.Message):
    result: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcStorePurchaseFinalize(betterproto.Message):
    txn_id: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcStorePurchaseFinalizeResponse(betterproto.Message):
    result: int = betterproto.uint32_field(1)
    item_ids: List[int] = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class CMsgGcBannedWordListRequest(betterproto.Message):
    ban_list_group_id: int = betterproto.uint32_field(1)
    word_id: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class CMsgGcRequestAnnouncements(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CMsgGcRequestAnnouncementsResponse(betterproto.Message):
    announcement_title: str = betterproto.string_field(1)
    announcement: str = betterproto.string_field(2)
    nextmatch_title: str = betterproto.string_field(3)
    nextmatch: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class CMsgGcBannedWord(betterproto.Message):
    word_id: int = betterproto.uint32_field(1)
    word_type: "GcBannedWordType" = betterproto.enum_field(2)
    word: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class CMsgGcBannedWordListResponse(betterproto.Message):
    ban_list_group_id: int = betterproto.uint32_field(1)
    word_list: List["CMsgGcBannedWord"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CMsgGcToGcBannedWordListBroadcast(betterproto.Message):
    broadcast: "CMsgGcBannedWordListResponse" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcToGcBannedWordListUpdated(betterproto.Message):
    group_id: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class CsoEconDefaultEquippedDefinitionInstanceClient(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    item_definition: int = betterproto.uint32_field(2)
    class_id: int = betterproto.uint32_field(3)
    slot_id: int = betterproto.uint32_field(4)


@dataclass(eq=False, repr=False)
class CMsgGcToGcDirtySdoCache(betterproto.Message):
    sdo_type: int = betterproto.uint32_field(1)
    key_uint64: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class CMsgGcToGcDirtyMultipleSdoCache(betterproto.Message):
    sdo_type: int = betterproto.uint32_field(1)
    key_uint64: List[int] = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class CMsgGcCollectItem(betterproto.Message):
    collection_item_id: int = betterproto.uint64_field(1)
    subject_item_id: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class CMsgSdoNoMemcached(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CMsgGcToGcUpdateSqlKeyValue(betterproto.Message):
    key_name: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcToGcIsTrustedServer(betterproto.Message):
    steam_id: int = betterproto.fixed64_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcToGcIsTrustedServerResponse(betterproto.Message):
    is_trusted: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcToGcBroadcastConsoleCommand(betterproto.Message):
    con_command: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcServerVersionUpdated(betterproto.Message):
    server_version: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcClientVersionUpdated(betterproto.Message):
    client_version: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class CMsgGcToGcWebApiAccountChanged(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CMsgGcToGcRequestPassportItemGrant(betterproto.Message):
    steam_id: int = betterproto.fixed64_field(1)
    league_id: int = betterproto.uint32_field(2)
    reward_flag: int = betterproto.int32_field(3)


@dataclass(eq=False, repr=False)
class CMsgGameServerInfo(betterproto.Message):
    server_public_ip_addr: int = betterproto.fixed32_field(1)
    server_private_ip_addr: int = betterproto.fixed32_field(2)
    server_port: int = betterproto.uint32_field(3)
    server_tv_port: int = betterproto.uint32_field(4)
    server_key: str = betterproto.string_field(5)
    server_hibernation: bool = betterproto.bool_field(6)
    server_type: "CMsgGameServerInfoServerType" = betterproto.enum_field(7)
    server_region: int = betterproto.uint32_field(8)
    server_loadavg: float = betterproto.float_field(9)
    server_tv_broadcast_time: float = betterproto.float_field(10)
    server_game_time: float = betterproto.float_field(11)
    server_relay_connected_steam_id: int = betterproto.fixed64_field(12)
    relay_slots_max: int = betterproto.uint32_field(13)
    relays_connected: int = betterproto.int32_field(14)
    relay_clients_connected: int = betterproto.int32_field(15)
    relayed_game_server_steam_id: int = betterproto.fixed64_field(16)
    parent_relay_count: int = betterproto.uint32_field(17)
    tv_secret_code: int = betterproto.fixed64_field(18)
