import argparse
import csv
from services.addAllTypes import add_all_types
import asyncio

loop = asyncio.get_event_loop()

async def main():
    parser = argparse.ArgumentParser(description="Read CSV file and output 'long' and 'lat' columns.")
    parser.add_argument("csv_file", help="Path to the CSV file")
    args = parser.parse_args()

    with open(args.csv_file, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        if 'long' in csv_reader.fieldnames and 'lat' in csv_reader.fieldnames:
            points = []
            for row in csv_reader:
                points.append([row['long'],row['lat']])
            await add_all_types(points)
        else:
            print("CSV file does not contain 'long' and 'lat' columns.")


def job():
    loop.run_until_complete(main())

if __name__ == "__main__":
    job()
