select 
DISTINCT
rank() over (order by t.onemonth_rank+t.threemonth_rank+t.sixmonth_rank+t.oneyear_rank+t.thisyear_rank  asc ) ranks,
t.fund_id,
t.fund_name,
t.onemonth_rank+t.threemonth_rank+t.sixmonth_rank+t.oneyear_rank+t.thisyear_rank 
from 
(
SELECT 
f.fund_id,
f.fund_name,
rank()over(order by oneweek    desc)  oneweek_rank,
rank()over(order by onemonth   desc)  onemonth_rank,
rank()over(order by threemonth desc)  threemonth_rank,
rank()over(order by sixmonth   desc)  sixmonth_rank,
rank()over(order by oneyear    desc)  oneyear_rank,
rank()over(order by thisyear   desc)  thisyear_rank
from 
fund_info f
where 
f.fund_id in 
(
161725,
110011,
110022,
110013,
163406,
163402,
340007,
001938,
166002,
003095,
166011,
519712,
519772,
519736,
161005,
000513,
270002,
005911,
162605,
260116,
519068,
000173,
000362,
160215,
000566,
460005,
000577,
040008,
000136,
000127,
206009,
001875,
377240,
001410,
180031,
540006,
169101
)
)
t
order by t.onemonth_rank+t.threemonth_rank+t.sixmonth_rank+t.oneyear_rank+t.thisyear_rank 
asc 
