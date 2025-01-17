from pathlib import Path
from typing import Dict
import logging

from discord.ext import commands  # type: ignore

from ...models.crit import CritTableModel, CritTablesModel
from ..utils import get_first_set_match_or_over_under_flow


def _match(table: CritTableModel, roll: int) -> str:
    return get_first_set_match_or_over_under_flow(
        roll, table.crits, lambda c: c.rolls
    ).effect


_CRIT_TABLES: CritTablesModel = CritTablesModel(crit_tables=[])
_PATH: Path = Path(__file__).parent / "crits.json"
if _PATH.exists():
    _CRIT_TABLES = CritTablesModel.parse_file(_PATH)
else:
    logging.warning("Unable to find %s", _PATH)

_TABLES: Dict[int, CritTableModel] = {
    tbl.number: tbl for tbl in _CRIT_TABLES.crit_tables
}


def get_crit_table(number: int):
    return _TABLES[number]


@commands.command()
async def crit(ctx, table: int, roll: int):
    await ctx.send(_match(get_crit_table(table), roll))


@crit.error
async def crit_error(ctx, error):
    await ctx.send(str(error), delete_after=5)
