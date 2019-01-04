#-*- coding: utf-8 -*-
import uiautomator2 as u2
from time import sleep
import re


d=u2.connect('127.0.0.1:7555')
d.app_start('com.xiaoma.club')
d(resourceId="com.xiaoma.club:id/ll_tab_item_container").click()
d(resourceId="com.xiaoma.club:id/layout_nearby_group").click()
d(resourceId="com.xiaoma.club:id/btn_filter").click()
title_tv = d(resourceId="com.xiaoma.club:id/title_tv").info['text']
tv_label_name = d(resourceId="com.xiaoma.club:id/tv_label_name").info['text']
d(resourceId="com.xiaoma.club:id/tv_label_name").click()
tv_label_name_enable = d(resourceId="com.xiaoma.club:id/title_label_name").info['text']
tv_label_name_2 = \
d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=1).child(
    resourceId='com.xiaoma.club:id/tv_label_name', instance=0).info['text']
d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=1).child(
    resourceId='com.xiaoma.club:id/tv_label_name', instance=0).click()
tv_label_name_2_enable = \
d(resourceId="com.xiaoma.club:id/title_label_root", className="android.widget.LinearLayout", instance=1).child(
    resourceId='com.xiaoma.club:id/title_label_name').info['text']
tv_label_name_3 = \
d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=2).child(
    resourceId='com.xiaoma.club:id/tv_label_name').info['text']
d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=2).child(
    resourceId='com.xiaoma.club:id/tv_label_name').click()
tv_label_name_3_name = \
d(resourceId="com.xiaoma.club:id/title_label_root", className="android.widget.LinearLayout", instance=2).child(
    resourceId='com.xiaoma.club:id/title_label_name').info['text']
tv_label_name_4 = \
d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=3).child(
    resourceId='com.xiaoma.club:id/tv_label_name', instance=0).info['text']
d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=3).child(
    resourceId='com.xiaoma.club:id/tv_label_name', instance=0).click()
tv_label_name_4_name = \
d(resourceId="com.xiaoma.club:id/title_label_root", className="android.widget.LinearLayout", instance=3).child(
    resourceId='com.xiaoma.club:id/title_label_name').info['text']
d(scrollable=True).scroll(steps=60)
tv_label_name_5 = \
d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=4).child(
    resourceId='com.xiaoma.club:id/tv_label_name', instance=0).info['text']
d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=4).child(
    resourceId='com.xiaoma.club:id/tv_label_name', instance=0).click()
tv_label_name_5_name = \
d(resourceId="com.xiaoma.club:id/title_label_root", className="android.widget.LinearLayout", instance=4).child(
    resourceId='com.xiaoma.club:id/title_label_name').info['text']
# self.d(scrollable=True).scroll(steps=60)
d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=3).child(
    resourceId='com.xiaoma.club:id/tv_label_name').click()
toast = d.toast.get_message(5.0, 10.0, "default message")
d(resourceId="com.xiaoma.club:id/title_label_clear", className="android.widget.ImageView", instance=4).click()
d(resourceId="com.xiaoma.club:id/title_label_clear", className="android.widget.ImageView", instance=3).click()
d(resourceId="com.xiaoma.club:id/title_label_clear", className="android.widget.ImageView", instance=2).click()
d(resourceId="com.xiaoma.club:id/title_label_clear", className="android.widget.ImageView", instance=1).click()
one_label = d(resourceId="com.xiaoma.club:id/title_label_name").info['text']
d(resourceId="com.xiaoma.club:id/btn_filter").click()
label = []
num = 0
for l in range(5):
    try:
        count = d(resourceId="com.xiaoma.club:id/nearby_group_tag").child(className='android.widget.TextView', instance=num).info['text']
        label.append(count)
    except:
        pass
    num += 1
if one_label in label:
    print(True)
else:
    print(False)
title_tv=d(resourceId="com.xiaoma.club:id/title_tv").info['text']
id=d(resourceId="com.xiaoma.club:id/tv_group_id").info['text'][:2]
print(title_tv)
print(id)
