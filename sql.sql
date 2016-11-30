###De Duplicate 
WITH cte
         AS (SELECT ROW_NUMBER() OVER (PARTITION BY startDate, endDate, adwordsCampaignID,adwordsAdGroupID,adwordsCreativeID,adCost
                                           ORDER BY ( SELECT 0)) RN
             FROM   test_yang.dbo.googleADWordsData
			 )
      DELETE FROM cte
      WHERE  RN > 1;


##Query to Find Column From All Tables of Database
USE AdventureWorks
GO
SELECT t.name AS table_name,
SCHEMA_NAME(schema_id) AS schema_name,
c.name AS column_name
FROM sys.tables AS t
INNER JOIN sys.columns c ON t.OBJECT_ID = c.OBJECT_ID
WHERE c.name LIKE '%EmployeeID%'
ORDER BY schema_name, table_name;
