SELECT 
m.manager_id,m.manager_name,
count(DISTINCT f.fund_id) amt 
from 
fund_info f join  fund_manager  m on f.fund_id=m.fund_id
where 
f.category='qdii'
GROUP BY m.manager_id,m.manager_name
order by amt desc 