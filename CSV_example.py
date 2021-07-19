import csv
while True:
 option=input(f'Please select your option:\n'\
              f'1.Read the file\n'\
              f'2.Write the file')

 if option == '1':
  with open('csv_example.csv','r') as f:
   csv_list=csv.reader(f)
   for row in csv_list:
    print(row)

 if option == '2':
  model=input(f'Device Model:\t')
  version=input(f'Device Version:\t')
  ip=input(f'Device IP:\t')

  device=[model,version,ip]

  with open('csv_example.csv', 'a') as f:
   csv_writer=csv.writer(f,quoting=csv.QUOTE_ALL)
   csv_writer.writerow(device)



