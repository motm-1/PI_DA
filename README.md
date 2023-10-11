This project is based in data about airplanes crashes arround the world from 1908 to 2021 that the Henry Team provided me, the original dataset contains 5008 rows and 18 columns, but, for this project, i'll use only 8 of the original columns and i'll add new rows with the accidents that ocurred after the 09/21/2021 and before 2023.

The objective is to analyse and comprehend in depth the relationship between the number of accidents and fatalities and the variables, in order to identify possible improvements that could be implemented to reduce the number of accidents and fatalities.
It might also be interesting to identify what needs to be considered if you want to have the safest possible flight from a probabilistic perspective.

Once the data is fully understood and depured, i need to accompany the analysis with a clean presentation using interactive graphics and good metrics that explain the behaviour of the data in order to define KPIs that facilitate the alignment of our actions today with our goals in the future.

The dataset doesn't come with a dictionary, but I've made one for you.
Here are the columns from the original dataset that I've chosen for this project, what they mean and why I chose them:

- *Date* : Date of accident in the format YYYY-MM-DD (datetime) .
Key value to understand the evolution of the data over the years and how it behaves when you use a closed time period or filters like month or day.

- *Location* : City, Country or a description in case of an accident outside any country (object).
Important column for demographic analysis, specifically, for a demographic map.

- *Operator* : Airline (object).
It might be interesting to find patterns of which airlines have the most accidents or victims and the characterisctics of those.

- *Route* : Route of the flight before the crash or objetive in case of non comercial flights e.g. Training. (object)
This column could also show interesting patterns to explain the occurrence of accidents.

- *AC Type* : AirCraft type (object).
This column shows how the different aircrafts perform against accidents and could be an interesting parameter to elaborate metrics to reduce failures in them and produce aircrafts of better quality.

- *Aboard* : Amount of passengers and crew members abboard (float).
Key parameter for elaborating possible KPI's.

- *Fatalities* : Number of people who died in the accident (float).
This column is also a key parameter in the development of KPI's.

- *Fatalities* Crew : Number of crew members who died in the accident (float).
This column is required by the Henry team to create a specific metric called "Crew Fatality Rate".

The ETL and EDA process was made in Python. The libraries utilized for this project are listed in the file requeriments.txt.

After a depth analysis of the information, the conclusions are reduced to a dashboard that consists of 3 pages:

In the first one we can see the total amount of affected flights and humans in a certain period of time.
The objective of this page is to understand where is the root of the problem and how it's affecting us today.
Yo can see that a big amount of the crashes are concentrated between the years 1940 (when the comercial aviation started to get popular) and 2000, with a total of 3736 crashes, 76% of the total take place in 52% of the amount of time that we have measured.
What does this mean? This mean that today, the problem that we're facing is not the amount of crashes, that's a problem of the past.
When i saw this, i started to investigate what information could be useful to define our goal, but before show you the indicator that i chose to measure our progress towards that goal i want to you to see the information that i analyse to get to that conclusion.

<p align="center">
<img src="_src/images/img_1.png"  height=450>
</p>

In this page of the dashboard, we have different charts in which i filtered the data by the most important variables to see if there are any countries, operators or aircrafts that can be useful to understand the behaviour of the fatalities and crashes.
What i've found is that:
U.S.A accumulate the higher number of fatalities and crashes, also is the country most present in crashes occured in military operations.
Russia is the second country in this ranking.
Aeroflot is the worst Airline from the past century in number of fatalities, but you dont need to worry about that today because they only had one crash since 1997
The aircraft with the higher number of fatalities, by far is the Douglas DC-3, but i won't affirm that it's a bad aircraft because it was one of the most popular and we don't have the total amount of flights that were made with this aircraft, so, we can't calculate how often the ratio between crashes and succesful flights. Also, this aircraft was used for military operations across the world, where the conditions might be favorable for a crash.
Another thing that caught my atention was that 29% of the accidents were related to climatic reasons as Storms, Rains, Tornados or Fog, that could be an useful metric to define our goals, but the one that i've chose is The survival rate.

<p align="center">
<img src="_src/images/img_2.png"  height=450>
</p>

I chose this metric because the crashes and fatalities have a marked downtrend but the survival rate isn't going that well, so, in order to improve the security of the flights, is a good idea to take care of this metric.
The KPI that i've proposed is:
Evaluate the 20% improvement in the survival rate in the last year compared to the previous year.
As you can see in the metrics, the 2022 the goal has been achieved but it's something that we need to pay attention closely.

This second KPI was proposed by the Henry Team:
Evaluate the 10% decrease in the Fatality Crew Ratio in the last decade compared to the previous decade.
We can see in the graphs that only 3 decades of 11 (without counting the first) reaches the goal.

<p align="center">
<img src="_src/images/img_3.png"  height=450>
</p>

What this analysis shows is that the challenge for the next years is to introduce new security measures to improve the survival rate and at least mantain the ongoig trend in the amount of crashes