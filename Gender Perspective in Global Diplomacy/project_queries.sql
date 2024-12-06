use diplomacyDB;

-- 1. Get all data from the csv:
select * from gender_diplomacy;

-- 2. Get Turkiye's female diplomats send
SELECT * FROM gender_diplomacy
Where cname_send = "Turkiye" and gender = 1;

-- 3. Try to get the highest 5 GDP correlation with gender representation
select gender, cname_send
from gender_diplomacy
Where cname_send = ("China", "Japan","Germany","India","France")
group by gender, cname_send;



