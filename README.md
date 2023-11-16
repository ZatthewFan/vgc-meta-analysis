# VGC Meta Analysis
Teambuilding is half the game in Pokemon VGC. It requires extensive knowledge about the metagame and also the game itself. I decided to alleviate a part of that challenge by creating this project, an attempt to solve the current VGC metagame by applying my knowledge about said metagame, *and some fancy ML magic*.


## How it works
This program uses Selenium to automate data collection of VGC teams with tournament results. The data is stored in a PostgreSQL database which is then analyzed using machine learning to report results.

### Fetching
The main file that fetches data is <a href="fetch_and_parse.py">fetch_and_parse.py</a>

It fetches all https://pokepast.es/ link from a chosen website (in this case, https://victoryroadvgc.com/sv-rental-teams/). Each pokepaste is a Team object and there are up to 6 Pokemon objects within a Team.

### Data Storing
The file that deals with stooring the data into a database is <a href="database.py">database.py</a>

The database system I chose is PostgreSQL because it would complement the OOP paradigm that I chose for this project.

### Machine Learning Analysis
The file that deals with the machine learning analysis is <a href="meta-analysis.ipynb">meta-analysis.ipynb</a>

I chose to use a Jupyter Notebook to do data analysis because it offers an easy way to visualize data by allowing the code to be executed step-by-step, and thus making it easier to follow when plotting data with matplotlib or viewing dataframes with pandas.


<!---Modify this after I make a decision--->
I chose to do go with a supervised machine learning approach because it is possible to train my models with existing top performing teams in the metagame.

I have yet to choose an ML model for the analysis, but I would be grouping teams with similar archetypes together, so my initial thought would be a classification or clustering model.
<!------>

### Extras
#### <a href="defense-type-chart.json">defense-type-chart.json</a>: every type and its defensive properties
- Feel free to use it. **[*defending-type*][*attacking-type*]** will give you *defending-type*'s damage multiplier against *attacking-type*
    - [fire][water] will result in 2 (fire takes double damage from water)

#### <a href="nature-val.json">nature-val.json</a>: every nature and its stat boost / stat lower
- Also feel free to use it
- all lower case

### End Goal
- Finding options for a sixth member of a team
- Finding the favorable and poor matchups for a given team
- Flowcharting a given team's gameplan
- General data about the metagame (best pokemon to use; best types to have for offense/defense)


### Minimum TODO list:
- [x] Data Collection
- [x] Data Parsing
- [ ] Store data in database
- [ ] Analysis using ML
    - [ ] Choose a ML model
    - [ ] Categorize teams

### Additional features to add
- [ ] Suggesting a sixth member for a team
- [ ] Adding functionality for google sheets
- [ ] Analyzing OTS teams
- [ ] Find hardest matchup (what not to bring against certain matchups)
- [ ] Input enemy team, and find the best mons to bring
- [ ] Make an extension to collect data from pokemon showdown OTS battles
- [ ] Add teams through discord bot
- [ ] Fetch data from google sheets (download sheets as csv or through google api)