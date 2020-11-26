SELECT 
rank() over (order by now_best_fund_yields desc ) ranks,
m.manager_id,
m.manager_name,
m.now_best_fund_id,
m.now_best_fund_name,
m.now_best_fund_yields
from 
fund_manager m
GROUP BY
m.manager_id,
m.manager_name,
m.now_best_fund_id,
m.now_best_fund_name,
m.now_best_fund_yields
order by  m.now_best_fund_yields desc