from typing import Union, Optional, List


class HeroMatchup:
    hero_class: str
    """The hero's unique ID."""
    hero_id: int
    hero_name: str
    hero_thumbnail: str
    matches: int
    """The player's win rate with this hero."""
    win_rate: str
    wins: int

    def __init__(self, hero_class: str, hero_id: int, hero_name: str, hero_thumbnail: str, matches: int, win_rate: str, wins: int) -> None:
        self.hero_class = hero_class
        self.hero_id = hero_id
        self.hero_name = hero_name
        self.hero_thumbnail = hero_thumbnail
        self.matches = matches
        self.win_rate = win_rate
        self.wins = wins


class MainAttack:
    hits: int
    total: int

    def __init__(self, hits: int, total: int) -> None:
        self.hits = hits
        self.total = total


class HeroesRanked:
    assists: int
    damage: Union[float, int]
    damage_taken: Union[float, int]
    deaths: int
    heal: Union[float, int]
    hero_id: int
    hero_name: str
    hero_thumbnail: str
    kills: int
    main_attack: MainAttack
    matches: int
    mvp: int
    play_time: float
    svp: int
    wins: int

    def __init__(self, assists: int, damage: Union[float, int], damage_taken: Union[float, int], deaths: int, heal: Union[float, int], hero_id: int, hero_name: str, hero_thumbnail: str, kills: int, main_attack: MainAttack, matches: int, mvp: int, play_time: float, svp: int, wins: int) -> None:
        self.assists = assists
        self.damage = damage
        self.damage_taken = damage_taken
        self.deaths = deaths
        self.heal = heal
        self.hero_id = hero_id
        self.hero_name = hero_name
        self.hero_thumbnail = hero_thumbnail
        self.kills = kills
        self.main_attack = main_attack
        self.matches = matches
        self.mvp = mvp
        self.play_time = play_time
        self.svp = svp
        self.wins = wins


class Map:
    assists: int
    deaths: int
    kills: int
    map_id: int
    map_thumbnail: str
    matches: int
    play_time: float
    wins: int

    def __init__(self, assists: int, deaths: int, kills: int, map_id: int, map_thumbnail: str, matches: int, play_time: float, wins: int) -> None:
        self.assists = assists
        self.deaths = deaths
        self.kills = kills
        self.map_id = map_id
        self.map_thumbnail = map_thumbnail
        self.matches = matches
        self.play_time = play_time
        self.wins = wins


class IsWin:
    is_win: bool
    score: int

    def __init__(self, is_win: bool, score: int) -> None:
        self.is_win = is_win
        self.score = score


class PlayerPerformance:
    assists: int
    camp: int
    deaths: int
    disconnected: bool
    hero_id: int
    hero_name: str
    hero_type: str
    is_win: IsWin
    kills: int
    level: int
    new_level: int
    new_score: float
    player_uid: int
    score_change: Union[float, int]

    def __init__(self, assists: int, camp: int, deaths: int, disconnected: bool, hero_id: int, hero_name: str, hero_type: str, is_win: IsWin, kills: int, level: int, new_level: int, new_score: float, player_uid: int, score_change: Union[float, int]) -> None:
        self.assists = assists
        self.camp = camp
        self.deaths = deaths
        self.disconnected = disconnected
        self.hero_id = hero_id
        self.hero_name = hero_name
        self.hero_type = hero_type
        self.is_win = is_win
        self.kills = kills
        self.level = level
        self.new_level = new_level
        self.new_score = new_score
        self.player_uid = player_uid
        self.score_change = score_change


class ScoreInfo:
    the_0: int
    the_1: int

    def __init__(self, the_0: int, the_1: int) -> None:
        self.the_0 = the_0
        self.the_1 = the_1


class MatchHistory:
    """The number of assists made by the player in the match."""
    assists: Optional[int]
    """The date the match was played."""
    date: Optional[str]
    """The number of deaths the player had in the match."""
    deaths: Optional[int]
    duration: float
    game_mode_id: int
    """The number of kills made by the player in the match."""
    kills: Optional[int]
    map_id: int
    map_thumbnail: str
    """The unique identifier for the match."""
    match_id: Optional[str]
    match_time_stamp: int
    match_uid: str
    mvp_uid: int
    play_mode_id: int
    player_performance: PlayerPerformance
    """The result of the match (e.g., win, loss)."""
    result: Optional[str]
    score_info: ScoreInfo
    season: int
    svp_uid: int
    winner_side: int

    def __init__(self, assists: Optional[int], date: Optional[str], deaths: Optional[int], duration: float, game_mode_id: int, kills: Optional[int], map_id: int, map_thumbnail: str, match_id: Optional[str], match_time_stamp: int, match_uid: str, mvp_uid: int, play_mode_id: int, player_performance: PlayerPerformance, result: Optional[str], score_info: ScoreInfo, season: int, svp_uid: int, winner_side: int) -> None:
        self.assists = assists
        self.date = date
        self.deaths = deaths
        self.duration = duration
        self.game_mode_id = game_mode_id
        self.kills = kills
        self.map_id = map_id
        self.map_thumbnail = map_thumbnail
        self.match_id = match_id
        self.match_time_stamp = match_time_stamp
        self.match_uid = match_uid
        self.mvp_uid = mvp_uid
        self.play_mode_id = play_mode_id
        self.player_performance = player_performance
        self.result = result
        self.score_info = score_info
        self.season = season
        self.svp_uid = svp_uid
        self.winner_side = winner_side


class Ranked:
    total_assists: int
    total_deaths: int
    total_kills: int
    total_matches: int
    total_mvp: int
    total_svp: int
    total_time_played: str
    total_time_played_raw: float
    total_wins: int

    def __init__(self, total_assists: int, total_deaths: int, total_kills: int, total_matches: int, total_mvp: int, total_svp: int, total_time_played: str, total_time_played_raw: float, total_wins: int) -> None:
        self.total_assists = total_assists
        self.total_deaths = total_deaths
        self.total_kills = total_kills
        self.total_matches = total_matches
        self.total_mvp = total_mvp
        self.total_svp = total_svp
        self.total_time_played = total_time_played
        self.total_time_played_raw = total_time_played_raw
        self.total_wins = total_wins


class Unranked:
    total_assists: int
    total_deaths: int
    total_kills: int
    total_matches: int
    total_mvp: int
    total_svp: int
    total_time_played: str
    total_time_played_raw: int
    total_wins: int

    def __init__(self, total_assists: int, total_deaths: int, total_kills: int, total_matches: int, total_mvp: int, total_svp: int, total_time_played: str, total_time_played_raw: int, total_wins: int) -> None:
        self.total_assists = total_assists
        self.total_deaths = total_deaths
        self.total_kills = total_kills
        self.total_matches = total_matches
        self.total_mvp = total_mvp
        self.total_svp = total_svp
        self.total_time_played = total_time_played
        self.total_time_played_raw = total_time_played_raw
        self.total_wins = total_wins


class OverallStats:
    """The overall statistics of the player."""
    ranked: Ranked
    total_matches: int
    total_wins: int
    unranked: Unranked

    def __init__(self, ranked: Ranked, total_matches: int, total_wins: int, unranked: Unranked) -> None:
        self.ranked = ranked
        self.total_matches = total_matches
        self.total_wins = total_wins
        self.unranked = unranked


class Icon:
    player_icon: str
    player_icon_id: str

    def __init__(self, player_icon: str, player_icon_id: str) -> None:
        self.player_icon = player_icon
        self.player_icon_id = player_icon_id


class The1001001:
    diff_score: float
    level: int
    max_level: int
    max_rank_score: float
    protect_score: int
    rank_game_id: int
    rank_score: float
    update_time: int
    win_count: int

    def __init__(self, diff_score: float, level: int, max_level: int, max_rank_score: float, protect_score: int, rank_game_id: int, rank_score: float, update_time: int, win_count: int) -> None:
        self.diff_score = diff_score
        self.level = level
        self.max_level = max_level
        self.max_rank_score = max_rank_score
        self.protect_score = protect_score
        self.rank_game_id = rank_game_id
        self.rank_score = rank_score
        self.update_time = update_time
        self.win_count = win_count


class The1001002:
    diff_score: float
    level: int
    max_level: int
    max_rank_score: float
    protect_score: int
    rank_game_id: int
    rank_score: float
    update_time: int
    win_count: int

    def __init__(self, diff_score: float, level: int, max_level: int, max_rank_score: float, protect_score: int, rank_game_id: int, rank_score: float, update_time: int, win_count: int) -> None:
        self.diff_score = diff_score
        self.level = level
        self.max_level = max_level
        self.max_rank_score = max_rank_score
        self.protect_score = protect_score
        self.rank_game_id = rank_game_id
        self.rank_score = rank_score
        self.update_time = update_time
        self.win_count = win_count


class The1001003:
    diff_score: float
    level: int
    max_level: int
    max_rank_score: float
    protect_score: int
    rank_game_id: int
    rank_score: float
    update_time: int
    win_count: int

    def __init__(self, diff_score: float, level: int, max_level: int, max_rank_score: float, protect_score: int, rank_game_id: int, rank_score: float, update_time: int, win_count: int) -> None:
        self.diff_score = diff_score
        self.level = level
        self.max_level = max_level
        self.max_rank_score = max_rank_score
        self.protect_score = protect_score
        self.rank_game_id = rank_game_id
        self.rank_score = rank_score
        self.update_time = update_time
        self.win_count = win_count


class The1001004:
    diff_score: float
    level: int
    max_level: int
    max_rank_score: float
    protect_score: int
    rank_game_id: int
    rank_score: float
    update_time: int
    win_count: int

    def __init__(self, diff_score: float, level: int, max_level: int, max_rank_score: float, protect_score: int, rank_game_id: int, rank_score: float, update_time: int, win_count: int) -> None:
        self.diff_score = diff_score
        self.level = level
        self.max_level = max_level
        self.max_rank_score = max_rank_score
        self.protect_score = protect_score
        self.rank_game_id = rank_game_id
        self.rank_score = rank_score
        self.update_time = update_time
        self.win_count = win_count


class The1001005:
    diff_score: float
    level: int
    max_level: int
    max_rank_score: float
    protect_score: int
    rank_game_id: int
    rank_score: float
    update_time: int
    win_count: int

    def __init__(self, diff_score: float, level: int, max_level: int, max_rank_score: float, protect_score: int, rank_game_id: int, rank_score: float, update_time: int, win_count: int) -> None:
        self.diff_score = diff_score
        self.level = level
        self.max_level = max_level
        self.max_rank_score = max_rank_score
        self.protect_score = protect_score
        self.rank_game_id = rank_game_id
        self.rank_score = rank_score
        self.update_time = update_time
        self.win_count = win_count


class The1001006:
    diff_score: float
    level: int
    max_level: int
    max_rank_score: float
    protect_score: int
    rank_game_id: int
    rank_score: float
    update_time: int
    win_count: int

    def __init__(self, diff_score: float, level: int, max_level: int, max_rank_score: float, protect_score: int, rank_game_id: int, rank_score: float, update_time: int, win_count: int) -> None:
        self.diff_score = diff_score
        self.level = level
        self.max_level = max_level
        self.max_rank_score = max_rank_score
        self.protect_score = protect_score
        self.rank_game_id = rank_game_id
        self.rank_score = rank_score
        self.update_time = update_time
        self.win_count = win_count


class RankGameSeason:
    the_1001001: The1001001
    the_1001002: The1001002
    the_1001003: The1001003
    the_1001004: The1001004
    the_1001005: The1001005
    the_1001006: The1001006

    def __init__(self, the_1001001: The1001001, the_1001002: The1001002, the_1001003: The1001003, the_1001004: The1001004, the_1001005: The1001005, the_1001006: The1001006) -> None:
        self.the_1001001 = the_1001001
        self.the_1001002 = the_1001002
        self.the_1001003 = the_1001003
        self.the_1001004 = the_1001004
        self.the_1001005 = the_1001005
        self.the_1001006 = the_1001006


class Info:
    completed_achievements: str
    login_os: str
    rank_game_season: RankGameSeason

    def __init__(self, completed_achievements: str, login_os: str, rank_game_season: RankGameSeason) -> None:
        self.completed_achievements = completed_achievements
        self.login_os = login_os
        self.rank_game_season = rank_game_season


class Rank:
    color: str
    image: str
    rank: str

    def __init__(self, color: str, image: str, rank: str) -> None:
        self.color = color
        self.image = image
        self.rank = rank


class Team:
    club_team_id: str
    club_team_mini_name: str
    club_team_type: str

    def __init__(self, club_team_id: str, club_team_mini_name: str, club_team_type: str) -> None:
        self.club_team_id = club_team_id
        self.club_team_mini_name = club_team_mini_name
        self.club_team_type = club_team_type


class Player:
    """The processed player data."""
    icon: Icon
    info: Info
    """Whether the player's profile is private."""
    is_private: Optional[bool]
    level: str
    name: str
    """The player's nickname."""
    nickname: Optional[str]
    """The player ID."""
    player_id: Optional[str]
    rank: Rank
    team: Team
    uid: int

    def __init__(self, icon: Icon, info: Info, is_private: Optional[bool], level: str, name: str, nickname: Optional[str], player_id: Optional[str], rank: Rank, team: Team, uid: int) -> None:
        self.icon = icon
        self.info = info
        self.is_private = is_private
        self.level = level
        self.name = name
        self.nickname = nickname
        self.player_id = player_id
        self.rank = rank
        self.team = team
        self.uid = uid


class LevelProgression:
    level_progression_from: int
    to: int

    def __init__(self, level_progression_from: int, to: int) -> None:
        self.level_progression_from = level_progression_from
        self.to = to


class ScoreProgression:
    add_score: float
    total_score: float

    def __init__(self, add_score: float, total_score: float) -> None:
        self.add_score = add_score
        self.total_score = total_score


class RankHistory:
    level_progression: LevelProgression
    match_time_stamp: int
    """The points the player had in the season."""
    points: Optional[int]
    """The player's rank in the season."""
    rank: Optional[str]
    score_progression: ScoreProgression
    """The season number."""
    season: Optional[int]

    def __init__(self, level_progression: LevelProgression, match_time_stamp: int, points: Optional[int], rank: Optional[str], score_progression: ScoreProgression, season: Optional[int]) -> None:
        self.level_progression = level_progression
        self.match_time_stamp = match_time_stamp
        self.points = points
        self.rank = rank
        self.score_progression = score_progression
        self.season = season


class PlayerInfo:
    nick_name: str
    player_icon: str
    player_uid: int

    def __init__(self, nick_name: str, player_icon: str, player_uid: int) -> None:
        self.nick_name = nick_name
        self.player_icon = player_icon
        self.player_uid = player_uid


class TeamMate:
    matches: int
    """The teammate's nickname."""
    nickname: Optional[str]
    player_info: PlayerInfo
    """The unique ID of the teammate."""
    teammate_id: Optional[str]
    win_rate: str
    wins: int

    def __init__(self, matches: int, nickname: Optional[str], player_info: PlayerInfo, teammate_id: Optional[str], win_rate: str, wins: int) -> None:
        self.matches = matches
        self.nickname = nickname
        self.player_info = player_info
        self.teammate_id = teammate_id
        self.win_rate = win_rate
        self.wins = wins


class Updates:
    """Information about the player's updates."""
    info_update_time: str
    last_history_update: str
    last_inserted_match: str
    last_update_request: str

    def __init__(self, info_update_time: str, last_history_update: str, last_inserted_match: str, last_update_request: str) -> None:
        self.info_update_time = info_update_time
        self.last_history_update = last_history_update
        self.last_inserted_match = last_inserted_match
        self.last_update_request = last_update_request


class ApidogModel:
    """The list of hero matchups for the player."""
    hero_matchups: List[HeroMatchup]
    """The player's ranked heroes."""
    heroes_ranked: List[HeroesRanked]
    """The player's unranked heroes."""
    heroes_unranked: List[str]
    is_private: bool
    """Map statistics for the player."""
    maps: List[Map]
    """List of the player's match history."""
    match_history: List[MatchHistory]
    """The player's name."""
    name: str
    """The overall statistics of the player."""
    overall_stats: OverallStats
    """The processed player data."""
    player: Player
    """List of the player's rank history."""
    rank_history: List[RankHistory]
    """The player's teammates in recent matches."""
    team_mates: List[TeamMate]
    """The unique identifier for the player."""
    uid: int
    """Information about the player's updates."""
    updates: Updates

    def __init__(self, hero_matchups: List[HeroMatchup], heroes_ranked: List[HeroesRanked], heroes_unranked: List[str], is_private: bool, maps: List[Map], match_history: List[MatchHistory], name: str, overall_stats: OverallStats, player: Player, rank_history: List[RankHistory], team_mates: List[TeamMate], uid: int, updates: Updates) -> None:
        self.hero_matchups = hero_matchups
        self.heroes_ranked = heroes_ranked
        self.heroes_unranked = heroes_unranked
        self.is_private = is_private
        self.maps = maps
        self.match_history = match_history
        self.name = name
        self.overall_stats = overall_stats
        self.player = player
        self.rank_history = rank_history
        self.team_mates = team_mates
        self.uid = uid
        self.updates = updates