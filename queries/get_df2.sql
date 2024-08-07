select
  team
  , year
  , count(date) as count
from v_matches
group by team, year