1. Question:

Which statement sounds better?

A)
People who viewed more pages caused conversion.

B)
Converted users tended to view more pages on average.

Pick A or B and tell me why.

B, because A sounds like it is conclusive of the fact that viewing more page cause conversion but we still have no proof of the fact

That is exactly correct.

This distinction is one of the most important habits in data science.

What we observed:

Converters viewed ~20 pages
Non-converters viewed ~14 pages

What we can say:

✅ Converted users tended to view more pages.

What we cannot say:

❌ Viewing more pages causes conversion.

Why?

Because many other possibilities exist:

interested users naturally browse more
users with discounts browse more
referral users browse more
purchase intent causes both

EDA finds patterns, not proof.

2. | Column       | Median |
| ------------ | -----: |
| Age          |     41 |
| Income       |  70171 |
| Time_On_Site | 11.145 |


  Question:

Why did I ask for median and not mean?

Go back mentally.

Earlier we found:

Time_On_Site
mean = 13.67
median = 11.145
max = 607

Remember that suspicious outlier?

If we fill missing values using mean:

13.67

that gets pulled upward.

Median:

11.145

is more resistant.

Same logic applies to Income too.

So our current candidate preprocessing policy becomes:

Numeric missing values
→ fill with median



3. 🛠️ The Feature Selection Experiment
Here is the breakdown of the 3 sets we will test, focusing strictly on your high-value behavioral and demographic metrics:

Set 1 (Pure Engagement): Age, Income, Pages_Viewed, Products_Viewed, Time_On_Site, Time_On_Site_missing

Set 2 (Intent & History): Age, Income, Previous_Purchases, Discount_Seen, Time_On_Site, Time_On_Site_missing

Set 3 (Mixed Signals): Income, Pages_Viewed, Discount_Seen, Previous_Purchases, Time_On_Site, City_Tier