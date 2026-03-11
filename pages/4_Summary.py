import streamlit as st
import pandas as pd

st.title("Summary")

st.write("""For King County, we found that operating expenses have continued to increase even when ridership dropped, meaning it has become more expensive to maintain transit services. However, fares generally follow the same trend as passenger miles traveled (PMT). When transit use increases, fare revenue also increases, suggesting that higher ridership can help cover operating costs.

For Snohomish County, we saw that when PMT decreases, operating expenses increase. PMT and fares follow very similar patterns, meaning that when ridership increases, revenue from fares also increases.

One clear pattern in all the data was a large drop in ridership and fares in **2020 and 2021**, which is likely due to the COVID-19 pandemic. If we ignore those years, we see a steady increase in ridership, operating costs, and fares. This suggests that there is still potential for continued growth in public transit.

Our results were slightly different from our hypothesis. We found a **positive relationship between operating costs and PMT** when excluding 2020–2021. However, we expected fares to decrease as PMT increased, but instead they moved together. This means that when ridership increases, transit agencies also receive more revenue.

Another interesting finding was that **Snohomish County’s average fare has steadily decreased**, while **King County’s fare dropped sharply in 2020–2021 and then slowly declined afterward**. This raises a future question about what policies or incentives Snohomish County may have used to lower fares even while operating costs increased.""")