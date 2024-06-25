import csv
def write_holiday_cities(first_letter):
    with open('travel-notes.csv', 'r') as f:
        reader = csv.DictReader(f, fieldnames=['Name', 'have_visit', 'want_to_visit'])
        want_to_visit = set()
        have_visit = set()
        for data in reader:
            if data['Name']:
                if data['Name'][0] == str(first_letter.upper()):
                        visit = data['have_visit'].split(';')
                        have_visit.update(visit)
                        want = data['want_to_visit'].split(';')
                        want_to_visit.update(want)
        not_visit = want_to_visit.difference(have_visit)
        want_to_visit = list(want_to_visit)
        want_to_visit.sort()
        not_visit = list(not_visit)
        not_visit.sort()
        have_visit = list(have_visit)
        have_visit.sort()
        have_visit.insert(0,'Посетили:')
        want_to_visit.insert(0, 'Хотят посетить:')
        want_go = ['Следующим городом будет:']
        if not_visit:
            want_go.append(not_visit[0])
        not_visit.insert(0, 'Никогда не были в:')
        with open('holiday.csv', 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows([have_visit, want_to_visit, not_visit, want_go])
