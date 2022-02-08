conda env:deepner
参考自：F:\NER\BERT-NER-Pytorch-master\BERT-NER-Pytorch-master



python main.py \
#--gpu_ids=$GPU_IDS \
--output_dir=./out --mid_data_dir=./data/med_data/mid_data --mode=train --task_type=crf --raw_data_dir=./data/med_data/raw_data --bert_dir=F:\\pretrained_models\\bert_base\\bert-base-chinese --bert_type=bert-base --train_epochs=10 --swa_start=5 --attack_train="" --train_batch_size=6 --dropout_prob=0.1 --max_seq_len=512 --lr=2e-5 --other_lr=2e-3 --seed=123 --weight_decay=0.01 --loss_type='ls_ce' --eval_model
#--use_fp16