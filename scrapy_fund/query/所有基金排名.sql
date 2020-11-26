select 
rank() over(order by t.oneweek_rank+t.onemonth_rank+t.threemonth_rank+t.sixmonth_rank+t.oneyear_rank+t.thisyear_rank+t.twoyear_rank+t.threeyear_rank asc) ranks,
t.fund_id,
t.fund_name,
t.manager_id,
t.manager_name,
t.company_name,
t.oneweek_rank+t.onemonth_rank+t.threemonth_rank+t.sixmonth_rank+t.oneyear_rank+t.thisyear_rank+t.twoyear_rank+t.threeyear_rank 
from 
(
SELECT 
f.fund_id,
f.fund_name,
m.manager_id,
m.manager_name,
m.company_name,
rank()over(order by oneweek    desc)  oneweek_rank,
rank()over(order by onemonth   desc)  onemonth_rank,
rank()over(order by threemonth desc)  threemonth_rank,
rank()over(order by sixmonth   desc)  sixmonth_rank,
rank()over(order by thisyear   desc)  thisyear_rank,
rank()over(order by oneyear    desc)  oneyear_rank,
rank()over(order by twoyear   desc)   twoyear_rank,
rank()over(order by threeyear  desc)  threeyear_rank
from 
fund_info f join fund_manager m on f.fund_id=m.fund_id
) t
order by t.oneweek_rank+t.onemonth_rank+t.threemonth_rank+t.sixmonth_rank+t.oneyear_rank+t.thisyear_rank+t.twoyear_rank+t.threeyear_rank 
asc 
