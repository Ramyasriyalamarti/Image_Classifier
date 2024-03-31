#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


# In[18]:


data_train_path=r"C:\Users\hp\OneDrive\Desktop\Fruits_Vegetables\Fruits_Vegetables\train"
data_test_path=r"C:\Users\hp\OneDrive\Desktop\Fruits_Vegetables\Fruits_Vegetables\test"
data_val_path=r"C:\Users\hp\OneDrive\Desktop\Fruits_Vegetables\Fruits_Vegetables\validation"


# In[19]:


img_width=180
img_height=180


# In[20]:


data_train=tf.keras.utils.image_dataset_from_directory(data_train_path,shuffle=True,image_size=(img_width,img_height),batch_size=32,validation_split=False)


# In[21]:


data_cat=data_train.class_names


# In[22]:


data_val=tf.keras.utils.image_dataset_from_directory(data_val_path,image_size=(img_height,img_width),batch_size=32,shuffle=False,validation_split=False)


# In[23]:


data_test=tf.keras.utils.image_dataset_from_directory(data_test_path,image_size=(img_height,img_width),batch_size=32,shuffle=False,validation_split=False)


# In[24]:


import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
for image, labels in data_train.take(1):
    for i in range(9):
        plt.subplot(3, 3, i+1)
        plt.imshow(image[i].numpy().astype('uint8'))
        plt.title(data_cat[labels[i]])  # Assuming data_cat contains category names
        plt.axis('off')
plt.show()


# In[25]:


from tensorflow.keras.models import Sequential


# In[26]:


data_train


# In[30]:


model=Sequential([layers.Rescaling(1./255),
                 layers.Conv2D(16,3,padding='same',activation="relu"),
                 layers.MaxPooling2D(),
                 layers.Conv2D(32,3,padding='same',activation="relu"),
                 layers.MaxPooling2D(),
                 layers.Conv2D(64,3,padding='same',activation="relu"),
                 layers.MaxPooling2D(),
                 layers.Flatten(),
                 layers.Dropout(0.2),
                 layers.Dense(128),
                 layers.Dense(len(data_cat))
                 ])


# In[31]:


model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])


# In[32]:


epochs=25
history=model.fit(data_train,validation_data=data_val,epochs=epochs_size)


# In[36]:


epochs_range=range(epochs_size)
plt.figure(figsize=(8,8))
plt.subplot(1,2,2)
plt.plot(epochs_range,history.history['accuracy'],label='Training Accuracy')
plt.plot(epochs_range,history.history['val_accuracy'],label='Validation Accuracy')
plt.title('Accuracy')
plt.subplot(1,2,2)
plt.plot(epochs_range,history.history['loss'],label='Training Loss')
plt.plot(epochs_range,history.history['val_loss'],label='Validation Loss')
plt.title('Accuracy')


# In[42]:


image=r"C:\Users\hp\OneDrive\Desktop\Fruits_Vegetables\Fruits_Vegetables\test\apple\Image_1.jpg"
image=tf.keras.utils.load_img(image,target_size=(img_height,img_width))
img_arr=tf.keras.utils.array_to_img(image)
img_bat=tf.expand_dims(img_arr,0)


# In[43]:


predict=model.predict(img_bat)


# In[44]:


score=tf.nn.softmax(predict)


# In[45]:


print('Veg/Fruit in image is {} with accuracy of {:0.2f}'.format(data_cat[np.argmax(score)],np.max(score)*100))


# In[41]:


model.save('Image_classify.keras')


# In[ ]:




