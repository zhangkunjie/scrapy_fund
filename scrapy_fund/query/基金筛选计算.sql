SELECT
f.fund_id,
f.fund_name,
f.category,
f.ca_score_weighted_rank,
f.ca_weighted_rank,
f.ca_score_weighted_rank+f.ca_weighted_rank all_rank
from
fund_rank f
where 
f.category='qdii'
order  by  all_rank  asc
