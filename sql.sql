      WITH cte
         AS (SELECT ROW_NUMBER() OVER (PARTITION BY startDate, endDate, adwordsCampaignID,adwordsAdGroupID,adwordsCreativeID,adCost
                                           ORDER BY ( SELECT 0)) RN
             FROM   test_yang.dbo.googleADWordsData
			 )
      DELETE FROM cte
      WHERE  RN > 1;
