import os
import json
import csv
import pickle

os.system('CLS')#clear для систем Linux

def recursive_dir(path: str, output_dir: str):
    def save_results_as_json(results):
        with open(os.path.join(output_dir, 'itog.json'), 'w', encoding='utf-8') as json_file:
            json.dump(results, json_file, ensure_ascii=False, indent=4)

    def save_results_as_csv(results):
        csv_file = os.path.join(output_dir, 'itog.csv')
        with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
            csv_write = csv.DictWriter(csv_file, fieldnames=["Type", "Name", "Size"], dialect='excel-tab',
quoting=csv.QUOTE_ALL)
            csv_write.writeheader()
            for result in results:
                csv_write.writerow(result)

    def save_results_as_pickle(results):
        with open(os.path.join(output_dir, 'itog.pkl'), 'wb') as pickle_file:
            pickle.dump(results, pickle_file)

    results = []
    for root, dirs, files in os.walk(path):
        path = root.split(os.sep)
        total_size = sum(os.path.getsize(os.path.join(root, file)) for file in files)
        #print((len(path) - 1) * '---', os.path.basename(root), 'Размер директории: ', total_size)
        results.append({'Type': 'Dir', 'Name': os.path.basename(root), 'Size': total_size})

        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            #print(len(path) * '---', file, 'Размер файла : ' ,file_size)
            results.append({'Type': 'Folder', 'Name': file, 'Size': file_size})

    save_results_as_json(results)
    save_results_as_csv(results)
    save_results_as_pickle(results)


path = 'Dir'
output_directory = 'Itog'
os.makedirs(output_directory, exist_ok=True)

recursive_dir(path, output_directory)