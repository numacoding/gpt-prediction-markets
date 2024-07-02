# GPT Prediction Markets

This project is designed to capture and process market trends from various sources to create dynamic prediction markets based on current data. Using natural language processing technologies and web applications, this tool facilitates the creation and evaluation of prediction markets without the need for experts in each topic.

## Project Description

### Trend Capture

- **Google Trends** (`trend_capturer.py`): This script fetches market trends from Google Trends, allowing you to capture the most popular and emerging searches in various regions.
- **Twitter Trends** (`twitter_trends.py`): Similarly, this script captures Twitter trends, providing insight into the most discussed topics in real-time.

### Information Processing

- **Geolocation**: The captured information is processed and categorized based on geographic distribution, allowing you to select specific trends by region.
- **News Search** (`news_capturer.py`): This script takes the identified trends and searches for relevant news to provide broader context on each trend.

### Prediction Market Generation

- **GPT Prompter** (`gpt_prompter.py`): Using natural language models (LLMs), this script creates prediction markets based on the collected trends and news, ready to be published.

### Notion Integration

- **Notion Connection** (`notion_connection.py`): This script connects the pipeline to the Notion space of the Zeitgeist Advisory Committee.
- **Notion Interaction** (`notion_interaction.py`): Using this script, committee members can add any number of markets to their database.

### User Experience

- **Streamlit Application** (`app.py`): A web application developed with Streamlit (https://streamlit.io/) allows users to select prediction market proposals. These proposals can be added to the Notion space of the Zeitgeist Advisory Committee for evaluation and potential publication. The application is designed to be easily used by team members without programming knowledge.

## Objective

The objective of this project is to provide a tool capable of dynamically creating prediction markets based on current trends. This eliminates the need for experts in each topic, facilitating efficient and accurate creation and evaluation of prediction markets. The R&D of 'permissioned' prediction markets is solely the responsibility of the Advisory Committee. Given the fast pace of news, manual handling of this process represented a bottleneck and a significant workload for the Committee members. This repository aims to alleviate their burden.

## Usage

1. **Trend Capture**:
    - Run `trend_capturer.py` to fetch data from Google Trends.
    - Run `twitter_trends.py` to fetch Twitter trend data.

2. **Processing and News Search**:
    - Run `news_capturer.py` to search for news related to the captured trends.

3. **Prediction Market Generation**:
    - Run `gpt_prompter.py` to generate prediction markets based on the collected trends and news.

4. **Notion Integration**:
    - Run `notion_connection.py` to connect to the Notion space of the Zeitgeist Advisory Committee.
    - Run `notion_interaction.py` to add prediction markets to the Committee's database.

5. **Streamlit Application**:
    - Run `app.py` to start the web application and select prediction market proposals.

6. **Evaluation and Publication**:
    - Use the application to add proposals to the Notion space of the Zeitgeist Advisory Committee for evaluation.

## Contributions

Contributions are welcome. If you wish to improve the project, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
