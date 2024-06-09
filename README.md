# Netflix Content Exploration: Genres, Trends, and Popularity


## Find out more about us:


* **Deena Khan** - [GitHub profile Deena-k1](https://github.com/Deena-k1)
* **Evelyn Rees** [GitHub profile EveRefi](https://github.com/EveRefi)
* **Charlotte Taylor** - [GithubHub profile ctaylorsanders](https://github.com/ctaylorsanders)
* **Dosa** - [Github profile dosa29](https://github.com/dosa29)
* **Leila** - [GitHub profile KleilaGj](https://github.com/KleilaGj)


## Project Overview

In this project, our goal is to explore the factors that contribute to the popularity of Netflix content. We aim to gain insights into user preferences to inform content recommendations and strategies that enhance viewer satisfaction and engagement. By examining ratings, genres and content types, we aim to uncover user engagement patterns, preferences, and the factors contributing to the perceived quality of content on Netflix. This information can be leveraged to enhance content recommendations, improve overall viewer satisfaction, and inform future content creation strategies.

## Key Metrics and Benchmarks

Popularity refers to the degree to which a movie, TV show, or any other content attracts attention, interest, and engagement from a large audience over a given period. In the context of Netflix, popularity can be measured through various metrics such as the number of views, user ratings, watchtime, and the frequency of recommendations. Popularity may be influenced by:
- Quality of content
- Genre and theme
- Marketing
- Social influence
- Relevance to current events

**Ratings** refer to the numerical scores or assessments provided by users to movies, TV shows, or other content available on Netflix. Netflix publishes weekly global Top 10 lists for films and TV based on the number of views that week (views for a title is defined as the total hours viewed divided by the total runtime and rounded to 100,000).

**Watchtime** refers to the total amount of time users spend watching a particular movie, TV show, or any other content. It includes metrics like total watchtime, average watchtime, completion rate, session duration, and peak viewing times.

**Data Sources:**
* [TMDB API](https://developer.themoviedb.org/reference/intro/getting-started)
* [Netflix Engagment Report](https://about.netflix.com/en/news/what-we-watched-a-netflix-engagement-report)
* [Netflix Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)


### Overall Utility
By providing targeted groups with actionable insights derived from the analysis, the project helps enhance decision-making processes, optimize content production and marketing strategies, and ultimately improve user satisfaction and retention on Netflix.

## Ethical Considerations
this project used puplically available data set. If this project was to be given more time, we would've implemented data from other streaming services, or retrieve informed consent for more senstive data such as detailed user reports, with emphasis on keeping the data anonymised for privarcy and confidentiality of users. 


### Bias and Fairness
- In this project, we focused exclusively on data from Netflix, which may introduce bias and limit the generalizability of our findings to other streaming platforms. This selection could skew our analysis towards trends and patterns unique to Netflix, potentially overlooking broader industry insights. To mitigate this, we aimed to maintain fairness in our analysis by transparently acknowledging this limitation and refraining from overgeneralizing our conclusions. Recognizing this platform-specific focus allowed us to address potential biases and strive for a balanced and accurate representation of the data.

## Key Data Science Methods and Theories
In this project, we employed comprehensive data collection and cleaning techniques to ensure the integrity and usability of our datasets. We conducted Exploratory Data Analysis (EDA) and data visualization to uncover patterns and insights within the data. Our analysis included rigorous statistical analysis and hypothesis testing to validate our findings. We also implemented machine learning algorithms and predictive analytics to forecast trends and make data-driven predictions. Throughout the project, we adhered to ethical considerations in data handling to ensure privacy and compliance with data protection regulations.

## How to Use TMDb API to Get Ratings

To enrich your dataset with IMDb ratings, follow these steps:

1. **Retrieve IMDb Ratings:** Use the TMDb API to fetch ratings for each title in your dataset.
2. **Merge Ratings with Dataset:** Merge the fetched ratings with your existing dataset based on unique identifiers (e.g., IMDb ID).
3. **Clean and Preprocess Data:** Ensure consistency in the ratings data and handle any missing or erroneous values.
4. **Incorporate Ratings into Analysis:** Use the IMDb ratings to enhance your analysis of user engagement and content popularity.

## Project Management
We imployed an agile framework to navigate this project. we organized various methods of commuication. We did a mixture of group programming/ testing, as well as working on our individual branches. In order to efficently complete out project we used three tools:

- Zoom - To set up meetings, discuss ideas and visual demonstration of coding practise.
- Word Doc - To brainstorm ideas, set up a brief and set meeting agendas.
- Slack - Sending files, updating on progress of research and project.

# Using Git

Using the git command `git clone` followed by the HTTP link of the repository you wish to clone.
<img src="https://github.com/Deena-k1/Netflix_content_analysis/blob/main/docs/git.cloning.png?raw=true" width="600" height="300">

Using `git branch` to check the current branch you're on. Then using `git checkout <branch name>` to switch form main to a new branch.
<img src="https://github.com/Deena-k1/Netflix_content_analysis/blob/main/docs/git.branch.png" width="600" height="200">

Using `git add .`/ `git add <file name>` and commit changes using `git commit -m <message>`. then using `git push origin <branch name>`
<img src="https://github.com/Deena-k1/Netflix_content_analysis/blob/main/docs/git.add.png" width="600" height="200">

Crrating a pull request on the remote repository to review changes, once changes are approved, you can merge to main branch.
<img src="https://github.com/Deena-k1/Netflix_content_analysis/blob/main/docs/github.1.png" width="300" height="200">
