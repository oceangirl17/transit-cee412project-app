import streamlit as st
import pandas as pd

st.title("Analysis")


st.write("""After creating the E/R diagram and database schema, we made plots to show the relationships between **passenger miles traveled (PMT)**, **operating expenses**, and **year** for King County and Snohomish County. Figures 2 and 4 show these relationships. We also created plots comparing **PMT and fares**, along with their ratio, shown in Figures 3 and 5.

Figure 2 shows that operating expenses slowly increased from **2015 to 2019**, leveled off in **2020**, dropped in **2021**, and then increased again through **2023**. PMT increased from **2015 to 2017**, slightly decreased from **2017 to 2019**, and then dropped sharply from **2019 to 2021** before rising again after **2021**. The ratio of operating expenses to PMT generally increases over time, with a small decrease after 2021. This increase means that it is costing transit operators more money per passenger mile to run the system.""")


st.image("photos/kingcounty1.png", caption="Above shows the King County operating expense vs. passenger miles traveled and Operating expenses to PMT Ratio")

st.write("The passenger miles traveled and total fares for King County depict very similar patterns with steady inclines from 2015-2020 and then a rapid decline until 2021 and then a steady increase again after 2023. The average fare also slowly increased until 2019 dipped down in 2020-2021 and rapidly increased again and have slowly increased since 2021.")


st.image("photos/kingcountyfares.png", caption="Above shows the average cost of fare in King County, as well as the relationship between passenger miles travelled and total fares.")

st.write("Once we dissected the data for Snohomish County we analyzed from Figure 4 that the operating expenses had a steady incline until 2019, dipped down until 2021 and saw an increase again after 2021. There was a very similar trend for PMT which had a larger drop off in 2020. The ratio between operating expenses and PMT show a gradual increase from 2015 to 219 and then significant increases until 2022 where there is a decrease in expenses and then a slow incline again.")

st.image("photos/snohomish1.png", caption="Above shows the Snohomish County operating expense vs. passenger miles traveled and Operating expenses to PMT Ratio")

st.write("When assessing the data for the passenger miles traveled and total fares as well as the average fares based on Figure 5. We can see that the PMT and total fares have essentially the same pattern such as they both increase slowly until 2019 drop off at 2020 and start to slowly increase again after 2021. The average fare has been continuously decreasing since 2019.")


st.image("photos/snohomishfare.png", caption="Above shows the average cost of fare in Snohomish County, as well as the relationship between passenger miles travelled and total fares.")
