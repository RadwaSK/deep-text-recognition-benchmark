import os
import numpy as np
import cv2 as cv

images_path_1 = 'dataset/obtained_data/'
images1 = sorted(os.listdir(images_path_1))

train_labels_file = open('dataset/train_labels2.txt', 'w')
valid_labels_file = open('dataset/valid_labels2.txt', 'w')
test_labels_file = open('dataset/test_labels2.txt', 'w')

labels1 = np.load('dataset/labels.npy')
size1 = len(labels1)
limit1, limit2 = int(0.7*size1), int(0.9*size1)
train_labels1, train_images1 = labels1[0:limit1], images1[0 : limit1]
val_labels1, val_images1 = labels1[limit1:limit2], images1[limit1:limit2]
test_labels1, test_images1 = labels1[limit2:], images1[limit2:]

total_train_labels = []
total_val_labels = []
total_test_labels = []

for i in range(len(train_images1)):
	img_path = os.path.join(images_path_1, train_images1[i])
	text = str(img_path + '\t' + train_labels1[i] + '\n')
	print('Processing:', text, end='')
	total_train_labels.append(text)

for i in range(len(val_images1)):
	img_path = os.path.join(images_path_1, val_images1[i])
	text = str(img_path + '\t' + val_labels1[i] + '\n')
	print('Processing:', text, end='')
	total_val_labels.append(text)

for i in range(len(test_images1)):
	img_path = os.path.join(images_path_1, test_images1[i])
	text = str(img_path + '\t' + test_labels1[i] + '\n')
	print('Processing:', text, end='')
	total_test_labels.append(text)


train_labels2 = open('dataset/orig_dataset/annotation_train.txt', 'r').readlines()
val_labels2 = open('dataset/orig_dataset/annotation_val.txt', 'r').readlines()
test_labels2 = open('dataset/orig_dataset/annotation_test.txt', 'r').readlines()


for i in range(min(len(train_labels2), len(train_labels1) * 9)):
	img_path, label = train_labels2[i].split(' ')
	limit1 = img_path.find('_')
	limit2 = img_path.rfind('_')
	label = img_path[limit1 + 1:limit2]
	if img_path[0] == '.':
		img_path = 'dataset/orig_dataset' + img_path[1:]
	text = str(img_path + '\t' + label + '\n')
	print('Processing:', text, end='')
	total_train_labels.append(text)

for i in range(min(len(val_labels2), len(val_labels1) * 9)):
	img_path, label = val_labels2[i].split(' ')
	limit1 = img_path.find('_')
	limit2 = img_path.rfind('_')
	label = img_path[limit1 + 1:limit2]
	if img_path[0] == '.':
		img_path = 'dataset/orig_dataset' + img_path[1:]
	text = str(img_path + '\t' + label + '\n')
	print('Processing:', text, end='')
	total_val_labels.append(text)

for i in range(min(len(test_labels2), len(test_labels1) * 9)):
	img_path, label = test_labels2[i].split(' ')
	limit1 = img_path.find('_')
	limit2 = img_path.rfind('_')
	label = img_path[limit1 + 1:limit2]
	if img_path[0] == '.':
		img_path = 'dataset/orig_dataset' + img_path[1:]
	text = str(img_path + '\t' + label + '\n')
	print('Processing:', text, end='')
	total_test_labels.append(text)


np.random.shuffle(total_train_labels)
np.random.shuffle(total_val_labels)
np.random.shuffle(total_test_labels)

print('\nSaving train dataset of size:', len(total_train_labels))
for i in range(len(total_train_labels)):
	train_labels_file.write(total_train_labels[i])
print('Saving validation dataset of size:', len(total_val_labels))
for i in range(len(total_val_labels)):
	valid_labels_file.write(total_val_labels[i])
print('Saving test dataset of size:', len(total_test_labels))
for i in range(len(total_test_labels)):
	test_labels_file.write(total_test_labels[i])
