def Logger(initializedRecords: int, category: str):

    if initializedRecords > 0:
        print(f"{initializedRecords} {category} inserted.")

    else:
        print(f"No new {category} data available.")