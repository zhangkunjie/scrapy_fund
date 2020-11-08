SELECT 
*,
0.5*oneyear+0.3*twoyear+0.2*threeyear  score
from 
dingtou_rank
where 
category='qdii'
and oneyear>0
and twoyear>0
and threeyear>0 
order by 0.5*oneyear+0.3*twoyear+0.2*threeyear desc 







