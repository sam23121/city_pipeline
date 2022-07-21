-- with objects_new as (
--     select * from {{ source('public', 'objects') }}

-- )

-- final as (
--     select * from objects_new
-- )

-- select * from final

select * from public.objects

select distinct(type1), avg(avg_speed), avg(traveled_d) 
from public.objects
GROUP BY type1