import json
import glob

def merge_json_files(user_info_file, similar_authors_file, res_file):
    # 初始化空的列表用于存放所有的 JSON 数据
    merged_data = []
    error_data = []

    # 遍历满足文件名模式的所有文件
    with open(similar_authors_file, 'r') as file:
        authors_list = json.load(file)
    with open(user_info_file, 'r') as file:
        user_info_list = json.load(file)
        user_info_dicts = dict(user_info_list)

        
    for author in authors_list:
        print(author) 


    # 将合并的数据写入到输出文件
    with open(output_filename, 'w') as output_file:
        json.dump(merged_data, output_file)

    with open(error_filename, 'w') as error_file:
        json.dump(error_data, error_file)

merge_json_files('user_info.json','res-play_100k_2_authors_r500_new_30-zh.json'
                 'merged.json', 'errors.json')
