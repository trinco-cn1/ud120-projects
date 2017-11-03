#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print 'Persons count:', len(enron_data)
print enron_data['METTS MARK']
print 'Attributes count:', len(enron_data['METTS MARK'])

print 'POI:', sum([enron_data[key]['poi'] for key in enron_data if enron_data[key]['poi'] == 1])

print enron_data['PRENTICE JAMES']['total_stock_value']
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print 'Lay:', enron_data['LAY KENNETH L']['total_payments']
print 'Skilling:', enron_data['SKILLING JEFFREY K']['total_payments']
print 'Fastow:', enron_data['FASTOW ANDREW S']['total_payments']

print len([enron_data[key] for key in enron_data if enron_data[key]['salary'] != 'NaN'])
print len([enron_data[key] for key in enron_data if enron_data[key]['email_address'] != 'NaN'])

print len([enron_data[key] for key in enron_data if enron_data[key]['total_payments'] == 'NaN'])
print len(enron_data)
print len([enron_data[key] for key in enron_data if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True])
print len([enron_data[key] for key in enron_data if enron_data[key]['poi'] == True])