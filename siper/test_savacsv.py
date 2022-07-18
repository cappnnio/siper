import csv

with open('data.csv','w') as csvfile:
    write =csv.writer(csvfile)
    write.writerow(['id','name','age'])
    write.writerow(['1', 'name1', 'age1'])
    write.writerow(['2', 'name2', 'age2'])
    write.writerow(['3', 'name3', 'age3'])

print('ok')