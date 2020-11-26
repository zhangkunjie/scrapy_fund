truncate table fund_rank;
insert into  fund_rank
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
rank() over (partition by t.category order by   0.05*t.ca_oneweek_rank+0.1*t.ca_onemonth_rank+0.15*t.ca_threemonth_rank+0.2*t.ca_sixmonth_rank+0.2*t.ca_oneyear_rank+0.3*t.ca_thisyear_rank asc),
t.oneweek_rank,
t.onemonth_rank,
t.threemonth_rank,
t.sixmonth_rank,
t.oneyear_rank,
t.thisyear_rank,
t.total_score_weighted_rank,
rank() over (order by 0.05*t.oneweek_rank+0.1*t.onemonth_rank+0.15*t.threemonth_rank+0.2*t.sixmonth_rank+0.2*t.oneyear_rank+0.3*t.thisyear_rank asc)
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
) t