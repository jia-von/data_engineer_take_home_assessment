
select distinct account_name, utm_source, utm_medium from
(select utm_s.account_id, utm_source, utm_medium from
(select account_id, utm_value as utm_source
from sources 
where utm_name = 'utmcsr') AS utm_s
full outer join 
(select account_id, utm_value as utm_medium
from sources 
where utm_name = 'utmcmd') AS utm_m on utm_s.account_id = utm_m.account_id) as exp_out
left join accounts on exp_out.account_id = accounts.account_id