from gensim.models import Word2Vec
from sklearn.cluster import KMeans
import numpy as np

# 假设我们有一些视频标签
tags = [["游戏", "动画"], ["游戏", "设计"], ["游戏", "开发"], ["动画", "设计"], ["动画", "制作"]]

# 训练Word2Vec模型
model = Word2Vec(tags, min_count=1)

# 获取每个视频的标签向量的平均值
video_vectors = [np.mean([model.wv[tag] for tag in video_tags], axis=0) for video_tags in tags]

# 使用KMeans进行聚类
kmeans = KMeans(n_clusters=2)
kmeans.fit(video_vectors)

# 打印每个视频的聚类结果
for i, video_tags in enumerate(tags):
    print(f"Video: {video_tags}, Cluster: {kmeans.predict([video_vectors[i]])[0]}")

