select
  year
  , team
  , count(date) as count
from v_matches
group by year, team;