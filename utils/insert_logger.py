def Logger(initializedRecords: int, category: str):

    if initializedRecords > 0:
        print(f"No new {category} data available.")
    else:
        print(f"{initializedRecords} {category} inserted.")