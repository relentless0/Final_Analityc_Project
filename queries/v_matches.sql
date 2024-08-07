create view v_matches as(
select 
  t.team_long_name as team
  , c.name as country
  , m.date
  , EXTRACT(year from m.date) as year
from match m
left join Country c on c.country_id=m.country_id
left join Team t on t.team_api_id=m.home_team_api_id
);