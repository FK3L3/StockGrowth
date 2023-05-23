# STOCK Data Fetcher

This is a Python script that retrieves real-time data for AnyStock (symbol: #@$%) using the Alpha Vantage API. It fetches information such as the current stock price and trading volume.

## Prerequisites

Before running this script, make sure you have the following:

- Python 3.x installed on your system.
- An API key from Alpha Vantage. You can sign up for a free API key on their website: [Alpha Vantage](https://www.alphavantage.co/)

## Installation

1. Clone the repository or download the script file directly.

```shell
git clone https://github.com/your-username/your-repository.git
```

2. Install the required dependencies. In this case, there are no external dependencies to install.

## Usage

1. Open the script file `fetch_amazon_data.py` in a text editor.

2. Replace `'<your_api_key>'` with your Alpha Vantage API key. You can find the line of code near the end of the script:
 
3. Save the changes to the file.

4. Open a terminal or command prompt and navigate to the directory where the script is located.

5. Run the script using the following command:

```shell
python fetch_amazon_data.py
```

## Output

The script will retrieve data for Amazon from the Alpha Vantage API and display it on the console. The following information will be printed:

- Symbol: The stock symbol (AMZN).
- Price: The current stock price.
- Volume: The trading volume.

## Troubleshooting
```shell
hello world
```

- If you encounter any errors while making the API request, check your internet connection and make sure the Alpha Vantage API is accessible.
- If you see an error message stating "Global Quote not found in response," it means that the API response did not contain the expected data. Double-check the symbol and API key used.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.
