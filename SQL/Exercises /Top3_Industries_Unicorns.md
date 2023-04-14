### Instructions
Your task is to first identify the three best-performing industries based on the number of new unicorns created over the last three years (2019, 2020, and 2021) combined.

From there, you will write a query to return the industry, the year, the number of companies in these industries that became unicorns each year in 2019, 2020, and 2021, along with the average valuation per industry per year, converted to billions of dollars and rounded to two decimal places!

As the firm is interested in trends for the top-performing industries, your results should be displayed by industry, then year in descending order.

<br>

* The final output of your query will look like this:

<br>

|industry|year|num_unicorns|average_valuation_billions|
|-----|---|-------|-------|
|industry1|2021|top1|avg_billions|
|industry1|2020|top1|avg_billions|
|industry1|2019|top1|avg_billions|
|industry2|2021|top1|avg_billions|
|industry2|2020|top1|avg_billions|
|industry2|2019|top1|avg_billions|
|industry3|2021|top1|avg_billions|
|industry3|2020|top1|avg_billions|
|industry3|2019|top1|avg_billions|	


<br><br>

### Assignment Notes/Details
Did you know that the average return from investing in stocks is 10% per year! But who wants to be average?! 

You have been asked to support an investment firm by analyzing trends in high-growth companies. They are interested in understanding which industries are producing the highest valuations and the rate at which new high-value companies are emerging. Providing them with this information gives them a competitive insight as to industry trends and how they should structure their portfolio looking forward.

You have been given access to their `unicorns` database, which contains the following tables:

<br>

`dates`
| Column       | Description                                  |
|------------- |--------------------------------------------- |
| company_id   | A unique ID for the company.                 |
| date_joined  | The date that the company became a unicorn.  |
| year_founded | The year that the company was founded.       |

`funding`
| Column           | Description                                  |
|----------------- |--------------------------------------------- |
| company_id       | A unique ID for the company.                 |
| valuation        | Company value in US dollars.                 |
| funding          | The amount of funding raised in US dollars.  |
| select_investors | A list of key investors in the company.      |

`industries`
| Column       | Description                                  |
|------------- |--------------------------------------------- |
| company_id   | A unique ID for the company.                 |
| industry     | The industry that the company operates in.   |

`companies`
| Column       | Description                                       |
|------------- |-------------------------------------------------- |
| company_id   | A unique ID for the company.                      |
| company      | The name of the company.                          |
| city         | The city where the company is headquartered.      |
| country      | The country where the company is headquartered.   |
| continent    | The continent where the company is headquartered. |


```sql
-- 1) - Identify three best performing industries based on the number of new unicorns created over the last three years
-- 2) - Industry, year, # of companies in thse these industires that became unicorns, average valuation per industry per year
WITH joined_data AS (
	SELECT 
		CAST(EXTRACT(year from d.date_joined) AS integer) AS year, 			ind.company_id, ind.industry AS industry, fnd.valuation AS funding
	FROM dates AS d
	INNER JOIN industries AS ind
		USING(company_id)
	INNER JOIN funding AS fnd
		USING(company_id)
),
grouped_industries AS (
	SELECT
		industry,
		year,
		COUNT(*) AS num_unicorns,
		AVG(funding) AS average_funding		
	FROM joined_data
	WHERE year IN (2019, 2020, 2021)
	GROUP BY industry, year
),
ranked_industries AS (
	SELECT
		industry,
		year,
		num_unicorns,
		average_funding,
		RANK() OVER (
			PARTITION BY year
			ORDER BY num_unicorns DESC
		) AS industry_year_ranking
	FROM grouped_industries
)
SELECT 
	industry, 
	year,
	industry_year_ranking,
	num_unicorns, 
	ROUND(average_funding, 2) AS average_valuation_billions 
FROM ranked_industries
WHERE industry_year_ranking in (1, 2, 3)
ORDER BY industry_year_ranking, year DESC;
```

|industry|year|industry_year_ranking|num_unicorns|average_valuation_billions|
|-----|-----|------|------|-------|
|Fintech|2021|1|138|2753623188.41|
|Internet software & services|2020|1|20|4350000000|
|Fintech|2019|1|20|6800000000|
|Internet software & services|2021|2|119|2151260504.2|
|E-commerce & direct-to-consumer|2020|2|16|4000000000|
|Artificial intelligence|2019|2|14|4500000000|
|E-commerce & direct-to-consumer|2021|3|47|2468085106.38|
|Fintech|2020|3|15|4333333333.33|
|Internet software & services|2019|3|13|4230769230.77|

* Wording of the question tripped me up a bit (I grabbed the top three industries here regardless of industry for each particular year using the `RANK` window function so as to rank each industry by the group count of new unicorns grouped by (partitioned by the year)
* Solution the question intended is below along with the provider's sample solution

<br>

#### Second Query
```sql
WITH top_three_industries AS ( 
	SELECT
		ind.industry AS industry,
		COUNT(*) AS unc_three_year
	FROM public.dates AS unc_year
	INNER JOIN public.industries AS ind 
		ON unc_year.company_id = ind.company_id
	WHERE EXTRACT(YEAR FROM unc_year.date_joined) IN ('2019', '2020', '2021')
	GROUP BY industry
	ORDER BY unc_three_year DESC  
	LIMIT 3
)
SELECT
	ind.industry AS industry,
	EXTRACT(YEAR FROM uni_years.date_joined) AS year, 
	COUNT(*) AS num_unicorns, 
	ROUND(AVG(year_fnd.valuation/1000000000), 2) AS average_valuation_billions
FROM public.industries AS ind 
INNER JOIN public.dates AS uni_years
	USING(company_id)
INNER JOIN public.funding AS year_fnd
	USING(company_id)
WHERE industry in (SELECT DISTINCT(industry) FROM top_three_industries) AND EXTRACT(YEAR FROM uni_years.date_joined) in ('2019', '2020', '2021')
GROUP BY industry, year
ORDER BY industry, year DESC;
```
|industry|year|num_unicorns|average_valuation_billions|
|----|----|------|-----|
|E-commerce & direct-to-consumer|2021|47|2.47|
|E-commerce & direct-to-consumer|2020|16|4|
|E-commerce & direct-to-consumer|2019|12|2.58|
|Fintech|2021|138|2.75|
|Fintech|2020|15|4.33|
|Fintech|2019|20|6.8|
|Internet software & services|2021|119|2.15|
|Internet software & services|2020|20|4.35|
|Internet software & services|2019|13|4.23|


<br>


* DCamp Solution
```sql
WITH top_industries AS
(
    SELECT i.industry, 
        COUNT(i.*)
    FROM industries AS i
    INNER JOIN dates AS d
        ON i.company_id = d.company_id
    WHERE EXTRACT(year FROM d.date_joined) in ('2019', '2020', '2021')
    GROUP BY industry
    ORDER BY count DESC
    LIMIT 3
),

yearly_rankings AS 
(
    SELECT COUNT(i.*) AS num_unicorns,
        i.industry,
        EXTRACT(year FROM d.date_joined) AS year,
        AVG(f.valuation) AS average_valuation
    FROM industries AS i
    INNER JOIN dates AS d
        ON i.company_id = d.company_id
    INNER JOIN funding AS f
        ON d.company_id = f.company_id
    GROUP BY industry, year
)

SELECT industry,
    year,
    num_unicorns,
    ROUND(AVG(average_valuation / 1000000000), 2) AS average_valuation_billions
FROM yearly_rankings
WHERE year in ('2019', '2020', '2021')
    AND industry in (SELECT industry
                    FROM top_industries)
GROUP BY industry, num_unicorns, year, average_valuation
ORDER BY industry, year DESC
```