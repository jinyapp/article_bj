import os
import json

import numpy as np
from tqdm import trange


def get_crf_labels(data_dir):
    labels = ["O"]
    tails = [
        "MedCheck",
        "Drug",
        "Degree",
        "Nature",
        "Symptom",
        "Disease",
        "Position",
        "BodyParts",
        "Negative",
        "CheckKey",
        "CheckVal",
        "People",
        "DiseaseHistoryTrigger",
        "Time",
        "Frequency",
        "BodyFunction",
        "BodyFunctionSym",
    ]
    for tail in tails:
        for head in ['B', 'I', 'E', 'S']:
            labels.append(head + "-" + tail)
    label_list = {}
    for idx,label in enumerate(labels):
        label_list[label]=idx
    print(len(label_list))
    save_info(data_dir,label_list, 'crf_ent2id')

def save_infos(data_dir, datas):
    ratio_train = 0.8  # 训练集比例
    ratio_trainval = 0.1  # 验证集比例
    ratio_val = 0.1  # 测试集比例
    assert (ratio_train + ratio_trainval + ratio_val) == 1.0, 'Total ratio Not equal to 1'  ##检查总比例是否等于1
    np.random.shuffle(datas)  ##打乱文件列表
    datas = datas[0:10000]  #  取前10k数据
    cnt_val = round(len(datas) * ratio_val, 0)
    cnt_trainval = round(len(datas) * ratio_trainval, 0)
    cnt_train = len(datas) - cnt_val - cnt_trainval
    print("val Sample:" + str(cnt_val))
    print("trainval Sample:" + str(cnt_trainval))
    print("train Sample:" + str(cnt_train))
    train_list = []
    dev_list = []
    test_list = []

    for i in range(int(cnt_train)):
        train_list.append(datas[i])

    for i in range(int(cnt_train), int(cnt_train + cnt_trainval)):
        dev_list.append(datas[i])

    for i in range(int(cnt_train + cnt_trainval), int(cnt_train + cnt_trainval + cnt_val)):
        test_list.append(datas[i])

    save_info(data_dir,train_list, 'train')
    save_info(data_dir,dev_list, 'dev')
    save_info(data_dir,test_list, 'test')

def save_info(data_dir, data, desc):
    with open(os.path.join(data_dir, f'{desc}.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def convert_test_data_to_json(raw_dir, save_dir):

    test_examples = []
    f = open(os.path.join(raw_dir, f'train.line.txt'),encoding="utf-8")
    for id,line in enumerate(f):
        labels = []
        jline = json.loads(line)
        sentence = jline["originalText"]
        if(len(sentence)<100):
            continue
        for idx,label_json in enumerate(jline["entities"]):
            labels.append(["T"+str(idx), label_json["label_type"],label_json["start_pos"], label_json["end_pos"], label_json["entity"]])
        test_examples.append({
            'id': id,
            'text':sentence,
            'labels':labels,
            'pseudo': 0,
            'candidate_entities': []
        })
    print(len(test_examples))
    print(test_examples[0])
    save_infos(save_dir, test_examples)


if __name__ == '__main__':
    # start

    # test_dir = './data/med_data/data'
    # save_dir = './data/med_data/raw_data'
    # convert_test_data_to_json(test_dir, save_dir)
    # print('测试数据转换完成')

    #end

    # start
    get_crf_labels('./data/med_data/mid_data')

