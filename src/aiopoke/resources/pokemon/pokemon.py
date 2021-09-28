from typing import List
from ...minimal_resources import (
    MinimalAbility,
    MinimalGeneration,
    MinimalMove,
    MinimalMoveLearnMethod,
    MinimalNaturalGiftType,
    MinimalPokemonSpecies,
    MinimalPokemonForm,
    MinimalItem,
    MinimalStat,
    MinimalVersion,
    MinimalVersionGroup,
    MinimalLocationArea
)
from ..games.version_group import VersionGroupDetail
from ...utility.common_models.sprites import Sprites
from ...utility import NamedResource, VersionGameIndex, VersionEncounterDetail


class Pokemon(NamedResource):
    abilities: List["PokemonAbility"]
    base_experience: int
    forms: List["MinimalPokemonForm"]
    game_indices: List["VersionGameIndex"]
    height: int
    items: List["PokemonHeldItem"]
    is_default: bool
    location_area_encounters: List["PokemonLocationArea"]
    moves: List["PokemonMove"]
    order: int
    past_types: List["PastType"]
    species: "MinimalPokemonSpecies"
    sprites: "Sprites"
    stats: List["PokemonStat"]
    types: List["PokemonType"]
    weight: int

    def __init__(self, data) -> None:
        super().__init__(data)
        self.abilities = [
            PokemonAbility(ability_data) for ability_data in data["abilities"]
        ]
        self.base_experience = data["base_experience"]
        self.forms = [MinimalPokemonForm(form_data) for form_data in data["forms"]]
        self.game_indices = [
            VersionGameIndex(game_indice_data) for game_indice_data in data["game_indices"]
        ]
        self.height = data["height"]
        self.held_items = [PokemonHeldItem(item_data) for item_data in data["held_items"]]
        self.is_default = data["is_default"]
        self.location_area_encounters = [PokemonLocationArea(location_area_encounter_data) for location_area_encounter_data in data["location_area_encounters"]]
        self.moves = [PokemonMove(move_data) for move_data in data["moves"]]
        self.order = data["order"]
        self.past_types = [PastType(past_type_data) for past_type_data in data["past_types"]]
        self.species = MinimalPokemonSpecies(data["species"])
        self.sprites = Sprites(data["sprites"])
        self.stats = [PokemonStat(stat_data) for stat_data in data["stats"]]
        self.types = [
            PokemonType(type_data) for type_data in data["types"]
        ]
        self.weight = data["weight"]

    def __repr__(self) -> str:
        return (
            f"<Pokemon abilities={self.abilities} base_experience={self.base_experience} forms={self.forms} "
            f"game_indices={self.game_indices} height={self.height} id_={self.id_} items={self.items} "
            f"is_default={self.is_default} location_area_encounters={self.location_area_encounters} moves={self.moves} name='{self.name}' "
            f"order={self.order} past_types={self.past_types} species={self.species} sprites={self.sprites} "
            f"stats={self.stats} types={self.types} weight={self.weight}>"
        )


class PokemonAbility:
    is_hidden: bool
    slot: int
    pokemon: "MinimalAbility"

    def __init__(self, data) -> None:
        self.is_hidden = data["is_hidden"]
        self.slot = data["slot"]
        self.pokemon = MinimalAbility(data["ability"])

    def __repr__(self) -> str:
        return f"<PokemonAbility is_hidden={self.is_hidden} slot={self.slot} pokemon={self.pokemon}>"


class PokemonType:
    slot: int
    type_: "MinimalNaturalGiftType"

    def __init__(self, data) -> None:
        self.slot = data["slot"]
        self.type_ = MinimalNaturalGiftType(data["type"])

    def __repr__(self) -> str:
        return f"<PokemonType slot={self.slot} type_={self.type_}>"


class PokemonHeldItem:
    item: "MinimalItem"
    version_details: List["PokemonHeldItemVersion"]

    def __init__(self, data) -> None:
        self.item = MinimalItem(data["item"])
        self.version_details = [PokemonHeldItemVersion(version_detail_data) for version_detail_data in data["version_details"]]

    def __repr__(self) -> str:
        return f"<PokemonHeldItem item={self.item} version_details={self.version_details}>"


class PokemonHeldItemVersion:
    rarity: int
    version: "MinimalVersion"

    def __init__(self, data) -> None:
        self.rarity = data["rarity"]
        self.version = MinimalVersion(data["version"])

    def __repr__(self) -> str:
        return f"<PokemonHeldItemVersion rarity={self.rarity} version={self.version}>"


class PokemonMove:
    move: "MinimalMove"
    version_group_details: List["VersionGroupDetail"]

    def __init__(self, data) -> None:
        self.move = MinimalMove(data["move"])
        self.version_group_details = [VersionGroupDetail(version_group_detail_data) for version_group_detail_data in data["version_group_details"]]

    def __repr__(self) -> str:
        return f"<PokemonMove move={self.move} version_group_details={self.version_group_details}>"


class PokemonMoveVersion:
    move_learn_method: "MinimalMoveLearnMethod"
    version_group: "MinimalVersionGroup"
    level_learned_at: int

    def __init__(self, data) -> None:
        self.move_learn_method = MinimalMoveLearnMethod(data["move_learn_method"])
        self.version_group = MinimalVersionGroup(data["version_group"])
        self.level_learned_at = data["level_learned_at"]

    def __repr__(self) -> str:
        return f"<PokemonHeldItem move_learn_method={self.move_learn_method} version_group={self.version_group} level_learned_at={self.level_learned_at}>"


class PokemonStat:
    base_stat: int
    effort: int
    stat: "MinimalStat"

    def __init__(self, data) -> None:
        self.base_stat = data["base_stat"]
        self.effort = data["effort"]
        self.stat = MinimalStat(data["stat"])

    def __repr__(self) -> str:
        return f"<PokemonStat base_stat={self.base_stat} effort={self.effort} stat={self.stat}>"


class PastType:
    generation: "MinimalGeneration"
    types: List["PokemonType"]

    def __init__(self, data) -> None:
        self.generation = MinimalGeneration(data["generation"])
        self.types = [PokemonType(type_data) for type_data in data["types"]]

    def __repr__(self) -> str:
        return f"<PastType generation={self.generation} types={self.types}>"


class PokemonLocationArea:
    location_area: "MinimalLocationArea"
    version_details: List["VersionEncounterDetail"]

    def __init__(self, data) -> None:
        self.location_area = MinimalLocationArea(data["location_area"])
        self.version_details = [
            VersionEncounterDetail(version_detail_data)
            for version_detail_data in data["version_details"]
        ]

    def __repr__(self) -> str:
        return f"<PokemonLocationArea location_area={self.location_area} version_details={self.version_details}>"