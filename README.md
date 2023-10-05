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
This column is required by the Henry team to create a specific KPI called "Crew Fatality Rate".

The libraries utilized for this project are listed in the file requeriments.txt.