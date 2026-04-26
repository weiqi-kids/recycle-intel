"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .abtc import AbtcFetcher
from .aurubis import AurubisFetcher
from .boliden import BolidenFetcher
from .glencore import GlencoreFetcher
from .kunding import KundingFetcher
from .renewi import RenewiFetcher
from .republic import RepublicFetcher
from .sims import SimsFetcher
from .tomra import TomraFetcher
from .umicore import UmicoreFetcher
from .veolia import VeoliaFetcher
from .waste_connections import WasteConnectionsFetcher
from .waste_mgmt import WasteMgmtFetcher

FETCHERS = {
    "abtc": AbtcFetcher,
    "aurubis": AurubisFetcher,
    "boliden": BolidenFetcher,
    "glencore": GlencoreFetcher,
    "kunding": KundingFetcher,
    "renewi": RenewiFetcher,
    "republic": RepublicFetcher,
    "sims": SimsFetcher,
    "tomra": TomraFetcher,
    "umicore": UmicoreFetcher,
    "veolia": VeoliaFetcher,
    "waste_connections": WasteConnectionsFetcher,
    "waste_mgmt": WasteMgmtFetcher,
}
