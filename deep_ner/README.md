conda env:deepner
参考自：F:\NER\BERT-NER-Pytorch-master\BERT-NER-Pytorch-master
https://github.com/z814081807/DeepNER
https://github.com/lonePatient/BERT-NER-Pytorch

python main.py \
#--gpu_ids=$GPU_IDS \
--output_dir=./out --mid_data_dir=./data/med_data/mid_data --mode=train --task_type=crf --raw_data_dir=./data/med_data/raw_data --bert_dir=F:\\pretrained_models\\bert_base\\bert-base-chinese --bert_type=bert-base --train_epochs=10 --swa_start=5 --attack_train="" --train_batch_size=6 --dropout_prob=0.1 --max_seq_len=512 --lr=2e-5 --other_lr=2e-3 --seed=123 --weight_decay=0.01 --loss_type='ls_ce' --eval_model
#--use_fp16

指针标注
1.设置C个指针网络
https://jishuin.proginn.com/p/763bfbd3c67a
多头标注（）
1. 如何构建一个n*n span矩阵
2. 如何解析0-1稀疏问题

片段序列
1. 构建n*(n+1)/2的片段序列


学习率预热
warmup_proportion

fp16 
混合精度训练

attack_train： 'pgd' / 'fgm' / '' 对抗训练 fgm 训练速度慢一倍, pgd 慢两倍，pgd 本次数据集效果明显
对抗训练
动机：采用对抗训练缓解模型鲁棒性差的问题，提升模型泛化能力
对抗训练是一种引入噪声的训练方式，可以对参数进行正则化，提升模型鲁棒性和泛化能力
Fast Gradient Method (FGM)：对embedding层在梯度方向添加扰动
Projected Gradient Descent (PGD) [2]：迭代扰动，每次扰动被投影到规定范围内

滑动参数平均：加权平均最后几个epoch模型的权重，得到更加平滑和表现更优的模型



从重采样到数据合成：如何处理机器学习中的不平衡分类问题？
https://www.cnblogs.com/huanjing/p/6789731.html

优化点
https://weibo.com/ttarticle/p/show?id=2309634590108526379451
1.词汇增强：即引入词汇信息，并适配于所对应的标注策略；这种词汇增强的方式常见于NER问题中，具体可参见JayJay之前的推文 《FLAT：中文NER屠榜之作！》。这种方式的关键在于如何引入具体的知识库信息（实体信息）；
 关于词汇增强的文章
https://mp.weixin.qq.com/s?__biz=MzIwNzc2NTk0NQ==&mid=2247497102&idx=1&sn=cedddfa134b0a2e0ca30b3f033560eb2&scene=21#wechat_redirect
2.解决标注不平衡 由于指针标注或多头标注中存在0-1不平衡问题（稀疏问题），可采取focal loss或者幂次惩罚。
loss_type: 'ce'：交叉熵; 'ls_ce'：label_smooth; 'focal': focal loss
3.负采样：缓解漏标问题、稀疏问题

