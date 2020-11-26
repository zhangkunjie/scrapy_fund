
select 
t.fund_id,
rank() over(partition by t.fsrq order by t.increment desc) ranks,
i.fund_name,
substring(t.fsrq,6,10) fsrq
from 
(
select 
a.fund_id,
b.fsrq,
round((b.dwjz-a.dwjz)*100/a.dwjz,2)increment
from 
(
SELECT 
f.fund_id,
f.dwjz
from
fund_value f
where 
f.fsrq='2020-11-02'
) a join 
(
SELECT 
f.fund_id,
f.dwjz,
f.fsrq
from
fund_value f
where f.fsrq>='2020-11-02'
and   f.fsrq<='2020-11-23'
) b 
on a.fund_id=b.fund_id
) t join 
(
SELECT 
f.fund_id,f.fund_name
from 
fund_info f 
group by f.fund_id,f.fund_name
) i
on t.fund_id=i.fund_id
order by fsrq asc 