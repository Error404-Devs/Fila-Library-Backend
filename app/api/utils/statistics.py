from app.db.database import db
import calendar, datetime


def get_monthly_statistics(month, year):
    monthly_borrows, error = db.get_monthly_borrows(month, year)
    returned_object = {
        "male_readers": 0,
        "female_readers": 0,
        "under_14": 0,
        "over_14": 0
    }
    if error:
        return None, error
    else:
        for borrow in monthly_borrows:
            borrow_person = borrow["person_id"]
            borrow_person_info, error = db.get_person(borrow_person)

            if borrow_person_info.get("gender") == "male":
                returned_object["male_readers"] += 1
            else:
                returned_object["female_readers"] += 1

            if borrow_person_info.get("year") > 8:
                returned_object["over_14"] += 1
            else:
                returned_object["under_14"] += 1

        month_days = calendar.monthrange(datetime.datetime.now().year, month)
        returned_object["total_readers"] = returned_object["male_readers"] + returned_object["female_readers"]
        returned_object["frequency"] = returned_object["total_readers"] / month_days[1]
        return returned_object, None
