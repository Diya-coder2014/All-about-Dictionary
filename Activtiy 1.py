student_data = {
    id1 : {'Name' : 'Sara', 'Class' : 5, 'Sub-integration' : 'English, Math, Science'},
    id2 : {'Name' : 'Suraj', 'Class' : 5, 'Sub-integration' : 'English, Math, Science'},
    id3 : {'Name' : 'Samantha', 'Class' : 5, 'Sub-integration' : 'English, Math, Science'},
    id4 : {'Name' : 'Sara', 'Class' : 5, 'Sub-integration' : 'English, Math, Science'}
    }

result = {}
seen_keys = []

for sudent_id, details in student_data.items():
    unique_key = (details['Name'], details['Class'], details['Sub-integration'])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result['student_id'] = details

for k, v in result.items():
    print(f'{k} : {v}')
