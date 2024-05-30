from app.db.database import db
import calendar, datetime


def get_statistics(month, year):
    total_frequency = 0
    statistics = {}
    # Search how many days are in a specific given month
    month_days = calendar.monthrange(datetime.datetime.now().year, month)

    # Iterate trough every day borrow to see statistics in a specific day
    daily = {}
    for day in range(1, month_days[1]+1):
        frequency = []
        returned_object = {
            "male_readers": 0,
            "female_readers": 0,
            "under_14": 0,
            "over_14": 0,
            "frequency": 0
        }
        daily_borrows, error = db.get_daily_borrows(month, year, day)
        if daily_borrows:
            for daily_borrow in daily_borrows:
                borrow_person = daily_borrow["person_id"]
                if borrow_person not in frequency:
                    frequency.append(borrow_person)
                    returned_object["frequency"] += 1
                borrow_person_info, error = db.get_person(borrow_person)
                if borrow_person_info.get("gender") == "male":
                    returned_object["male_readers"] += 1
                else:
                    returned_object["female_readers"] += 1

                if borrow_person_info.get("year") > 8:
                    returned_object["over_14"] += 1
                else:
                    returned_object["under_14"] += 1

                returned_object["total_readers"] = returned_object["male_readers"] + returned_object["female_readers"]

                daily[day] = returned_object
            total_frequency += returned_object["frequency"]
        else:
            daily[day] = returned_object
    monthly_borrows, error = db.get_monthly_borrows(month, year)
    monthly = {
        "male_readers": 0,
        "female_readers": 0,
        "under_14": 0,
        "over_14": 0,
        "monthly_frequency": total_frequency/month_days[1]
    }
    if monthly_borrows:
        for borrow in monthly_borrows:
            borrow_person = borrow["person_id"]
            borrow_person_info, error = db.get_person(borrow_person)

            if borrow_person_info.get("gender") == "male":
                monthly["male_readers"] += 1
            else:
                monthly["female_readers"] += 1

            if borrow_person_info.get("year") > 8:
                monthly["over_14"] += 1
            else:
                monthly["under_14"] += 1

        monthly["total_readers"] = monthly["male_readers"] + monthly["female_readers"]
    statistics["daily"] = daily
    statistics["monthly"] = monthly

    return statistics, None
