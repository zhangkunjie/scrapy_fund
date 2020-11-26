select 
*
from 
(
SELECT 
rank() over (order by cast(f.now_best_fund_yields as double )  desc  ) ranks,
f.manager_id,
f.manager_name,
f.now_best_fund_id,
f.now_best_fund_name,
f.now_best_fund_yields
from 
fund_manager f
where f.now_best_fund_yields>0
GROUP BY f.manager_id,
f.manager_name,
f.now_best_fund_id,
f.now_best_fund_name,
f.now_best_fund_yields
) t 
order by t.ranks asc 
