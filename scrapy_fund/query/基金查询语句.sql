SELECT
q.fund_id,
q.category,
q.fund_name,
q.score_weighted_rank,
q.total_weighted_rank,
q.score_weighted_rank+q.total_weighted_rank total_rank
from 
(
SELECT
t.fund_id,
t.fund_name,
t.category,
t.ca_oneweek_rank,
t.ca_onemonth_rank,
t.ca_threemonth_rank,
t.ca_sixmonth_rank,
t.ca_oneyear_rank,
t.ca_thisyear_rank,
t.ca_score_weighted_rank,
rank() over (partition by t.category order by   0.05*t.ca_oneweek_rank+0.1*t.ca_onemonth_rank+0.15*t.ca_threemonth_rank+0.2*t.ca_sixmonth_rank+0.2*t.ca_oneyear_rank+0.3*t.ca_thisyear_rank asc )score_weighted_rank,
t.oneweek_rank,
t.onemonth_rank,
t.threemonth_rank,
t.sixmonth_rank,
t.oneyear_rank,
t.thisyear_rank,
t.total_score_weighted_rank,
rank() over (order by 0.05*t.oneweek_rank+0.1*t.onemonth_rank+0.15*t.threemonth_rank+0.2*t.sixmonth_rank+0.2*t.oneyear_rank+0.3*t.thisyear_rank asc) total_weighted_rank
FROM
(
SELECT
fund_id,
fund_name,
category,
rank()over(PARTITION by category order by oneweek    desc)     ca_oneweek_rank,
rank()over(PARTITION by category order by onemonth   desc)     ca_onemonth_rank,
rank()over(PARTITION by category order by threemonth desc)     ca_threemonth_rank,
rank()over(PARTITION by category order by sixmonth   desc)     ca_sixmonth_rank,
rank()over(PARTITION by category order by oneyear    desc)     ca_oneyear_rank,
rank()over(PARTITION by category order by thisyear   desc)     ca_thisyear_rank,
rank()over (PARTITION by category order by 0.05*oneweek+0.1*onemonth+0.15*threemonth+0.2*sixmonth+0.2*oneyear+0.3*thisyear desc)    ca_score_weighted_rank,
rank()over(order by oneweek    desc)  oneweek_rank,
rank()over(order by onemonth   desc)  onemonth_rank,
rank()over(order by threemonth desc)  threemonth_rank,
rank()over(order by sixmonth   desc)  sixmonth_rank,
rank()over(order by oneyear    desc)  oneyear_rank,
rank()over(order by thisyear   desc)  thisyear_rank,
rank()over(order by 0.05*oneweek+0.1*onemonth+0.15*threemonth+0.2*sixmonth+0.2*oneyear+0.3*thisyear desc)  total_score_weighted_rank
FROM
fund_info f
where
f.onemonth>0
and f.threemonth>8
and f.sixmonth>20
and f.thisyear>30
and f.oneyear>50
and f.twoyear>70
and f.threeyear>90
and f.setup>80
and f.fund_name like '%易方达%'
) t
) q
ORDER BY total_rank asc




