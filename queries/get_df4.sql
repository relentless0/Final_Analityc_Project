select
  year
  , count(date) as count
from v_matches
group by year;
