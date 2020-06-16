
import csv
import os


def main():
    pwd = os.path.dirname(os.getcwd())
    csv_file = open(pwd + "/APITesting/dataincsvformat.csv","r")
    file_reader = csv.reader(csv_file) 
    file_data = []
    for line in file_reader:
        file_data.append(line)

    chart_data = [["TestName","DiffFromAverage"]]
    table_data = ["TestName","RunTime (s)"]
    for item in file_data[1:]: #skip first line is header
        test_name = item[0]
        item[1].rstrip()
        item[2].rstrip()
        if not item[1] or not item[2]:
            continue
        else:
            latest_run_time = float(item[1])
            average_run_time = float(item[2])
        diff_from_average = average_run_time - latest_run_time
        chart_data.append([test_name,diff_from_average])  
        table_data.append([test_name,latest_run_time])    

        print(chart_data)
        print(table_data)  

if __name__ == "__main__":main()


