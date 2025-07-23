import requests
import time
import csv
import html
import os

def Fetch_Data(QUESTIONS,BATCH_SIZE=50):
    '''This API Fetchs Data from OPENTDB 
    '''

    if BATCH_SIZE > 50:
        print("Batch size must be less then 50")
        print("for preventing program intruption limit set to 50")
        BATCH_SIZE = 50
    
    print("Downloading Data....")

    API_URL = f"https://opentdb.com/api.php?amount={BATCH_SIZE}"
    CSV_PATH = 'data/data.csv'

    # Ensure directory exists
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)

    # Write CSV header
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Question', 'Category', 'Difficulty', 'Answer'])

    fetched = 0

    while fetched < QUESTIONS:
        try:
            response = requests.get(API_URL)

            if response.status_code == 429:
                print(f"❌ Rate limited - Sleeping for 10 seconds...")
                time.sleep(4)
                continue

            if response.status_code != 200:
                print(f"❌ HTTP Error {response.status_code} - Sleeping for 2 seconds...")
                time.sleep(2)
                continue

            data = response.json()

            if data.get("response_code") != 0 or not data.get("results"):
                print("❌ API returned invalid data - Skipping...")
                time.sleep(1)
                continue

            with open(CSV_PATH, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)

                for result in data['results']:
                    question = html.unescape(result['Question'])
                    category = html.unescape(result['Category'])
                    difficulty = result['Difficulty']
                    correct_answer = html.unescape(result['Answer'])

                    writer.writerow([question, category, difficulty, correct_answer])
                    fetched += 1

                    if fetched >= QUESTIONS:
                        break

            print(f"✅ Fetched: {fetched}/{QUESTIONS}")
            time.sleep(1.5)  # Respect API
            return os.path.abspath(CSV_PATH)

        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            time.sleep(2)


if __name__ == "__main__":
    QUESTIONS = 10
    BATCH_SIZE=5
    # Fetch_Data(QUESTIONS,BATCH_SIZE=50)













