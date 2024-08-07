select 
  country
  , year
  , count(date) as count
from v_matches
group by country, year;
