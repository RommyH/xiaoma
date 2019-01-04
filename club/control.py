import uiautomator2 as u2
from time import sleep
import re
def connect_device(self):
    self.d=u2.connect('127.0.0.1:7555')  #连接pad

def timeout_time(self):
    self.d.wait_timeout = 6.0   #设置默认等待时间
    self.d.click_post_delay =1.0  #设置点击后1.5秒才能点击
def start_club(self):
    self.d.app_start('com.xiaoma.club')  #打开想聊
    sleep(3)
def stop_club(self):
    self.d.app_stop('com.xiaoma.club')   #关闭想聊

def club_top(self):
    return self.d(resourceId="com.xiaoma.club:id/rb_button", text=u"排行榜").exists(timeout=5)   #排行榜元素是否存在

def click_find(self):
    self.d(resourceId="com.xiaoma.club:id/rb_button").click()   #点击发现

def find_page_text(self):
    sleep(2)
    car_text=self.d(resourceId="com.xiaoma.club:id/layout_nearby_car").child(className="android.widget.TextView",instance=0).info['text']
    group_text=self.d(resourceId="com.xiaoma.club:id/layout_nearby_group").child(className="android.widget.TextView", instance=0).info['text']
    search_text=self.d(resourceId="com.xiaoma.club:id/layout_search").child(className="android.widget.TextView",instance=0).info['text']
    if car_text == '附近的车' and group_text == '附近的群' and search_text == '搜索':
        return True
    else:
        return False

def nearby_car_home(self):
    self.d(resourceId="com.xiaoma.club:id/layout_nearby_car").click()  #点击附近的车
    sleep(3)
    user_head=self.d(resourceId="com.xiaoma.club:id/iv_user_head").exists(timeout=5)
    tv_name=self.d(resourceId="com.xiaoma.club:id/tv_name").exists(timeout=5)
    iv_sex=self.d(resourceId="com.xiaoma.club:id/iv_sex").exists(timeout=5)
    tv_age=self.d(resourceId="com.xiaoma.club:id/tv_age").exists(timeout=5)
    tv_car_type=self.d(resourceId="com.xiaoma.club:id/tv_car_type").exists(timeout=5)
    tv_distance=self.d(resourceId="com.xiaoma.club:id/tv_distance").exists(timeout=5)
    if user_head == True and tv_name == True and iv_sex == True and tv_age == True and tv_car_type == True and tv_distance == True:
        return True
    else:
        return False

def car_rank(self):
    distance = self.d(resourceId="com.xiaoma.club:id/tv_distance").info['text'][2:][0:-2]
    while True:
        self.d(scrollable=True).scroll(steps=60)
        distance2 =self.d(className="android.widget.LinearLayout", instance=28).child(resourceId="com.xiaoma.club:id/tv_distance").info['text'][2:][0:-2]
        if distance2 != distance:
            break
    if distance < distance2:
        return True
    else:
        return False

def oneRow_twoCar(self):   #一行显示两个车主
    try:
        left=self.d(className="android.widget.LinearLayout", instance=5).right(className="android.widget.LinearLayout").exists(timeout=5)
        if left == True:
            pass
        else:
            return False
        right = self.d(className="android.widget.LinearLayout", instance=11).left(className="android.widget.LinearLayout").exists(timeout=5)
        if right == True:
            pass
        else:
            return False
        right2 = self.d(className="android.widget.LinearLayout", instance=11).right(className="android.widget.LinearLayout").exists(timeout=5)
        if right2 == True:
            return False
        else:
            pass
    except:
        return True

def click_car_info(self):
    name = self.d(resourceId="com.xiaoma.club:id/tv_name").info['text']
    age2 = self.d(resourceId="com.xiaoma.club:id/tv_age").info['text']
    age = re.compile('(\d+)').search(age2).group(1)
    type = self.d(resourceId="com.xiaoma.club:id/tv_car_type").info['text']
    sleep(2)
    self.d(resourceId="com.xiaoma.club:id/tv_name").click()
    sleep(2)
    nametab = self.d(text=u"姓    名：").exists(timeout=5)
    agetab = self.d(text=u"年    龄：").exists(timeout=5)
    typetab = self.d(text=u"车    型：").exists(timeout=5)
    num = self.d(text=u"车牌号：").exists(timeout=5)
    toolsname = self.d(resourceId="com.xiaoma.club:id/tv_name").info['text']
    toolsage = self.d(resourceId="com.xiaoma.club:id/tv_age").info['text']
    toolstype = self.d(resourceId="com.xiaoma.club:id/tv_car_type").info['text']
    add_friend = self.d(resourceId="com.xiaoma.club:id/btn_add_friend").info['text']
    start_chat = self.d(resourceId="com.xiaoma.club:id/btn_start_chat").info['text']
    if name == toolsname and age == toolsage and type == toolstype and nametab == True and agetab == True and typetab ==True and num ==True and add_friend == '加为好友' and start_chat == '发起对话':
        return True
    else:
        return False
def send_message(self):
    self.d(resourceId="com.xiaoma.club:id/btn_add_friend").click()
    toast = self.d.toast.get_message(5.0, 10.0, "default message")
    if toast == '请求发送成功':
        return True
    else:
        return False
def temporary_session(self):
    self.d(resourceId="com.xiaoma.club:id/btn_start_chat").click()
    self.d(resourceId="com.xiaoma.club:id/btn_more").click()
    toast = self.d.toast.get_message(5.0, 10.0, "default message")
    self.d.press('back')
    if toast == '未添加为好友，无法使用此功能':
        return True
    else:
        return False
def filtrate(self):
    sleep(3)
    self.d(resourceId="com.xiaoma.club:id/btn_filter").click()
    toastView = self.d(className="android.widget.RelativeLayout", instance=1).exists(timeout=5.0)
    sex = self.d(text=u"性别").info['text']
    selected_other = self.d(resourceId="com.xiaoma.club:id/selected_other").info['text']
    selected_man = self.d(resourceId="com.xiaoma.club:id/selected_man").info['text']
    selected_woman = self.d(resourceId="com.xiaoma.club:id/selected_woman").info['text']
    age = self.d(text=u"年龄").info['text']
    selected_age_other = self.d(resourceId="com.xiaoma.club:id/selected_age_other").info['text']
    selected_1 = self.d(resourceId="com.xiaoma.club:id/selected_1").info['text']
    selected_2 = self.d(resourceId="com.xiaoma.club:id/selected_2").info['text']
    selected_3 = self.d(resourceId="com.xiaoma.club:id/selected_3").info['text']
    active = self.d(text=u"活跃").info['text']
    selected_m_other = self.d(resourceId="com.xiaoma.club:id/selected_m_other").info['text']
    fifteen_m = self.d(resourceId="com.xiaoma.club:id/fifteen_m").info['text']
    one_hour = self.d(resourceId="com.xiaoma.club:id/one_hour").info['text']
    one_day = self.d(resourceId="com.xiaoma.club:id/one_day").info['text']
    three_day = self.d(resourceId="com.xiaoma.club:id/three_day").info['text']
    btn_sure_selected = self.d(resourceId="com.xiaoma.club:id/btn_sure_selected").info['text']
    btn_cancel_selected = self.d(resourceId="com.xiaoma.club:id/btn_cancel_selected").info['text']
    if toastView==True and sex=='性别' and selected_other=='不限' and selected_man=='男' and selected_woman=='女' and age=='年龄' and selected_age_other=='不限' and selected_1=='18~35' and  selected_2=='36~50' and selected_3=='51以上' and active=='活跃' and selected_m_other=='不限' and fifteen_m=='15分钟' and one_hour=='1小时' and one_day=='1天' and three_day=='3天' and btn_sure_selected=='确定' and btn_cancel_selected=='取消':
        return True
    else:
        return False

def filtrate_result(self):
    sleep(1)
    self.d(resourceId="com.xiaoma.club:id/selected_1").click()
    sleep(1)
    self.d(resourceId="com.xiaoma.club:id/btn_sure_selected").click()
    sleep(3)
    first_result = self.d(className="android.widget.LinearLayout", instance=5).exists(timeout=5.0)
    if first_result == True:
        return True
    else:
        return False
def group_filtrate_result(self):
    self.d(resourceId="com.xiaoma.club:id/btn_filter").click()
    self.d(resourceId="com.xiaoma.club:id/selected_woman").click()
    self.d(resourceId="com.xiaoma.club:id/three_day").click()
    self.d(resourceId="com.xiaoma.club:id/btn_sure_selected").click()
    sleep(3)
    first_result = self.d(className="android.widget.LinearLayout", instance=5).exists(timeout=5.0)
    if first_result == True:
        return True
    else:
        return False

def filtrate_cache_true(self):
    self.d(resourceId="com.xiaoma.club:id/btn_filter").click()
    self.d(resourceId="com.xiaoma.club:id/selected_man").click()
    self.d(resourceId="com.xiaoma.club:id/selected_3").click()
    self.d(resourceId="com.xiaoma.club:id/one_hour").click()
    self.d(resourceId="com.xiaoma.club:id/btn_cancel_selected").click()
    self.d(resourceId="com.xiaoma.club:id/btn_filter").click()
    man = self.d(resourceId="com.xiaoma.club:id/selected_man").info['checked']
    age = self.d(resourceId="com.xiaoma.club:id/selected_3").info['checked']
    active = self.d(resourceId="com.xiaoma.club:id/one_hour").info['checked']
    if man==True and age==True and active==True:
        return True
    else:
        return False

def filtrate_cache_false(self):
    self.d.press('back')
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/layout_nearby_car").click()
    self.d(resourceId="com.xiaoma.club:id/btn_filter").click()
    man = self.d(resourceId="com.xiaoma.club:id/selected_man").info['checked']
    age = self.d(resourceId="com.xiaoma.club:id/selected_3").info['checked']
    active = self.d(resourceId="com.xiaoma.club:id/one_hour").info['checked']
    if man==False and age==False and active==False:
        return True
    else:
        return False

def group_rank(self):
    self.d.press('back')
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/layout_nearby_group").click()
    first_group = self.d(resourceId="com.xiaoma.club:id/tv_distance").info['text'][2:][0:-2]
    while True:
        self.d(scrollable=True).scroll(steps=30)
        second_group = self.d(resourceId="com.xiaoma.club:id/tv_distance").info['text'][2:][0:-2]
        if second_group == first_group:
            self.d(scrollable=True).scroll(steps=30)
        else:
            break
    if first_group<second_group:
        return True
    else:
        return False

def one_group(self):
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/layout_nearby_group").click()
    try:
        left = self.d(className="android.widget.LinearLayout", instance=6).right(className="android.widget.LinearLayout").exists(timeout=5)
        if left == True:
            return False
        else:
            return True
    except:
        return True
def group_info(self):
    image = self.d(className="android.widget.ImageView", instance=1).exists(timeout=5.0)
    group_name = self.d(resourceId="com.xiaoma.club:id/title_share").exists(timeout=5.0)
    group_id = self.d(resourceId="com.xiaoma.club:id/tv_group_id").info['text'][:2]
    group_member = self.d(resourceId="com.xiaoma.club:id/tv_group_member").info['text'][:3]
    distance = self.d(resourceId="com.xiaoma.club:id/tv_distance").info['text'][:2]
    if image==True and group_name==True and group_id=='群号' and group_member=='群人数' and distance=='距离':
        return True
    else:
        return False
def add_group(self):
    id = self.d(resourceId="com.xiaoma.club:id/tv_group_id").info['text'][3:]
    self.d(className="android.widget.LinearLayout", instance=6).click()
    self.d(resourceId="com.xiaoma.club:id/dialog_left_button").click()
    sleep(1)
    self.d.press('back')
    sleep(1)
    self.d.press('back')
    sleep(1)
    self.d(resourceId="com.xiaoma.club:id/layout_nearby_group").click()
    id2 = self.d(resourceId="com.xiaoma.club:id/tv_group_id").info['text'][3:]
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/rb_button", text=u"会话    ").click()
    self.d(resourceId="com.xiaoma.club:id/item_list_head_bg").click()
    self.d(className="android.widget.ImageButton", instance=1).click()
    self.d(scrollable=True).scroll(steps=10)
    self.d(resourceId="com.xiaoma.club:id/btn_quit_qun").click()
    self.d(resourceId="com.xiaoma.club:id/dialog_left_button").click()
    self.d(resourceId="com.xiaoma.club:id/rb_button").click()
    self.d(resourceId="com.xiaoma.club:id/layout_nearby_group").click()
    id3 = self.d(resourceId="com.xiaoma.club:id/tv_group_id").info['text'][3:]
    if id != id2 and id==id3 :
        return True
    else:
        return False
def group_detail_info(self):
    self.d(className="android.widget.LinearLayout", instance=13).click()
    group_head = self.d(resourceId="com.xiaoma.club:id/iv_group_head").exists(timeout=5.0)
    group_name = self.d(text=u"群名称：").info['text']
    group_id = self.d(text=u"群    号：").info['text']
    group_count = self.d(text=u"群人数：").info['text']
    left_button = self.d(resourceId="com.xiaoma.club:id/dialog_left_button").info['text']
    right_button = self.d(resourceId="com.xiaoma.club:id/dialog_right_button").info['text']
    if group_head==True and group_name=='群名称：' and group_id=='群    号：' and group_count=='群人数：' and left_button=='进入' and right_button=='取消':
        return True
    else:
        return False
def group_jump(self):
    self.d.press('back')
    self.d(className="android.widget.RelativeLayout", instance=3).click()
    self.d(resourceId="com.xiaoma.club:id/dialog_left_button").click()
    record_voice = self.d(resourceId="com.xiaoma.club:id/btn_record_voice").exists(timeout=5.0)
    assistant = self.d(resourceId="com.xiaoma.club:id/ll_assistant").exists(timeout=5.0)
    if record_voice==True and assistant==True:
        return True
    else:
        return False

def back_group(self):
    self.d(className="android.widget.ImageButton", instance=1).click()
    self.d(scrollable=True).scroll(steps=60)
    id = self.d(className="android.widget.LinearLayout", instance=8).child(resourceId='com.xiaoma.club:id/tv_item_info').info['text']
    self.d.press('back')
    self.d.press('back')
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/layout_nearby_group").click()
    id2 = self.d(resourceId="com.xiaoma.club:id/tv_group_id").info['text'][3:]
    if id != id2:
        return True
    else:
        return False
def back_group_list(self):
    id = self.d(resourceId="com.xiaoma.club:id/tv_group_id").info['text'][3:]
    self.d(className="android.widget.LinearLayout", instance=13).click()
    self.d(resourceId="com.xiaoma.club:id/dialog_left_button").click()
    self.d.press('back')
    id2 = self.d(resourceId="com.xiaoma.club:id/tv_group_id").info['text'][3:]
    if id == id2 :
        return True
    else:
        return False
def click_group_back(self):
    self.d(className="android.widget.LinearLayout", instance=13).click()
    record_voice = self.d(resourceId="com.xiaoma.club:id/btn_record_voice").exists(timeout=5.0)
    assistant = self.d(resourceId="com.xiaoma.club:id/ll_assistant").exists(timeout=5.0)
    if record_voice==True and assistant==True:
        return True
    else:
        return False
def cancel_add_group(self):
    self.d.press('back')
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/layout_nearby_group").click()
    self.d(className="android.widget.LinearLayout", instance=13).click()
    self.d(resourceId="com.xiaoma.club:id/dialog_right_button").click()
    filter=self.d(resourceId="com.xiaoma.club:id/btn_filter").exists(timeout=5.0)
    if filter == True:
        return True
    else:
        return False
def null_group_label(self):
    id1 = self.d(resourceId="com.xiaoma.club:id/tv_group_id").info['text'][3:]
    id2 = self.d(className="android.widget.RelativeLayout", instance=8).child(resourceId='com.xiaoma.club:id/tv_group_id').info['text'][3:]
    self.d(resourceId="com.xiaoma.club:id/btn_filter").click()
    self.d(resourceId="com.xiaoma.club:id/btn_filter").click()
    id11 = self.d(resourceId="com.xiaoma.club:id/tv_group_id").info['text'][3:]
    id22 = self.d(className="android.widget.RelativeLayout", instance=8).child(resourceId='com.xiaoma.club:id/tv_group_id').info['text'][3:]
    if id1==id11 and id2==id22:
        return True
    else:
        return False
def max_group_label(self):
    self.d(resourceId="com.xiaoma.club:id/btn_filter").click()
    title_tv = self.d(resourceId="com.xiaoma.club:id/title_tv").info['text']
    tv_label_name = self.d(resourceId="com.xiaoma.club:id/tv_label_name").info['text']
    self.d(resourceId="com.xiaoma.club:id/tv_label_name").click()
    tv_label_name_enable = self.d(resourceId="com.xiaoma.club:id/title_label_name").info['text']
    tv_label_name_2 = self.d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=1).child(resourceId='com.xiaoma.club:id/tv_label_name', instance=0).info['text']
    self.d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=1).child(resourceId='com.xiaoma.club:id/tv_label_name', instance=0).click()
    tv_label_name_2_enable = self.d(resourceId="com.xiaoma.club:id/title_label_root", className="android.widget.LinearLayout", instance=1).child(resourceId='com.xiaoma.club:id/title_label_name').info['text']
    tv_label_name_3 = self.d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=2).child(resourceId='com.xiaoma.club:id/tv_label_name').info['text']
    self.d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=2).child(resourceId='com.xiaoma.club:id/tv_label_name').click()
    tv_label_name_3_name = self.d(resourceId="com.xiaoma.club:id/title_label_root", className="android.widget.LinearLayout", instance=2).child(resourceId='com.xiaoma.club:id/title_label_name').info['text']
    tv_label_name_4 = self.d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=3).child(resourceId='com.xiaoma.club:id/tv_label_name', instance=0).info['text']
    self.d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=3).child(resourceId='com.xiaoma.club:id/tv_label_name', instance=0).click()
    tv_label_name_4_name = self.d(resourceId="com.xiaoma.club:id/title_label_root", className="android.widget.LinearLayout", instance=3).child(resourceId='com.xiaoma.club:id/title_label_name').info['text']
    self.d(scrollable=True).scroll(steps=60)
    tv_label_name_5 = self.d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=4).child(resourceId='com.xiaoma.club:id/tv_label_name', instance=0).info['text']
    self.d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=4).child(resourceId='com.xiaoma.club:id/tv_label_name', instance=0).click()
    tv_label_name_5_name = self.d(resourceId="com.xiaoma.club:id/title_label_root", className="android.widget.LinearLayout", instance=4).child(resourceId='com.xiaoma.club:id/title_label_name').info['text']
    # self.d(scrollable=True).scroll(steps=60)
    self.d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=3).child(resourceId='com.xiaoma.club:id/tv_label_name').click()
    toast = self.d.toast.get_message(5.0, 10.0, "default message")
    if title_tv=='筛选标签' and tv_label_name==tv_label_name_enable and tv_label_name_2==tv_label_name_2_enable and tv_label_name_3==tv_label_name_3_name and tv_label_name_4==tv_label_name_4_name and tv_label_name_5==tv_label_name_5_name and toast=='最多只能选择5个标签!':
        return True
    else:
        return False
def delete_group_label(self):
    self.d(resourceId="com.xiaoma.club:id/title_label_clear", className="android.widget.ImageView", instance=4).click()
    five_label = self.d(resourceId="com.xiaoma.club:id/tag_horizontal_list_view").child(resourceId='com.xiaoma.club:id/title_label_root', instance=4).exists(timeout=5.0)
    if five_label==False:
        return True
    else:
        return False
def label_filtrate_correct(self):
    self.d(resourceId="com.xiaoma.club:id/title_label_clear", className="android.widget.ImageView", instance=3).click()
    self.d(resourceId="com.xiaoma.club:id/title_label_clear", className="android.widget.ImageView", instance=2).click()
    self.d(resourceId="com.xiaoma.club:id/title_label_clear", className="android.widget.ImageView", instance=1).click()
    one_label=self.d(resourceId="com.xiaoma.club:id/title_label_name").info['text']
    self.d(resourceId="com.xiaoma.club:id/btn_filter").click()
    label = []
    num = 0
    for l in range(5):
        try:
            count = self.d(resourceId="com.xiaoma.club:id/nearby_group_tag").child(className='android.widget.TextView',instance=num).info['text']
            label.append(count)
        except:
            pass
        num += 1
    if one_label in label:
        return True
    else:
        return False
def clear_label(self):
    self.d(resourceId="com.xiaoma.club:id/title_label_clear").click()
    title_tv=self.d(resourceId="com.xiaoma.club:id/title_tv").info['text']
    id=self.d(resourceId="com.xiaoma.club:id/tv_group_id").info['text'][:2]
    if title_tv=='附近的群' and id =='群号':
        return True
    else:
        return False
def two_label(self):
    self.d(resourceId="com.xiaoma.club:id/btn_filter").click()
    tv_label_name_1 = self.d(resourceId="com.xiaoma.club:id/tv_label_name").info['text']
    tv_label_name_2 = self.d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=1).child(resourceId='com.xiaoma.club:id/tv_label_name').info['text']
    self.d(resourceId="com.xiaoma.club:id/tv_label_name").click()
    self.d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=1).child(resourceId='com.xiaoma.club:id/tv_label_name').click()
    self.d(resourceId="com.xiaoma.club:id/btn_filter").click()
    label = []
    num = 0
    for l in range(5):
        try:
            count = self.d(resourceId="com.xiaoma.club:id/nearby_group_tag").child(className='android.widget.TextView',instance=num).info['text']
            label.append(count)
        except:
            pass
        num += 1
    if tv_label_name_1 in label and tv_label_name_2 in label:
        return True
    else:
        return False
def null_search(self):
    self.d(resourceId="com.xiaoma.club:id/btn_filter").click()
    self.d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=2).child(resourceId='com.xiaoma.club:id/tv_label_name', instance=0).click()
    self.d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=3).child(resourceId='com.xiaoma.club:id/tv_label_name', instance=0).click()
    self.d(resourceId="com.xiaoma.club:id/item_labels", className="android.widget.GridView", instance=4).child(resourceId='com.xiaoma.club:id/tv_label_name', instance=0).click()
    self.d(resourceId="com.xiaoma.club:id/btn_filter").click()
    empty =self.d(resourceId="com.xiaoma.club:id/tv_data_empty").info['text']
    if empty=='没有搜索到符合条件的群':
        return True
    else:
        return False
def delete_label_search(self):
    self.d(resourceId="com.xiaoma.club:id/title_label_clear", className="android.widget.ImageView", instance=1).click()
    label_name = self.d(resourceId="com.xiaoma.club:id/title_label_name").info['text']
    label = []
    num = 0
    for l in range(5):
        try:
            count = self.d(resourceId="com.xiaoma.club:id/nearby_group_tag").child(className='android.widget.TextView',instance=num).info['text']
            label.append(count)
        except:
            pass
        num += 1
    self.d(resourceId="com.xiaoma.club:id/title_label_clear").click()
    title_tv=self.d(resourceId="com.xiaoma.club:id/title_tv").info['text']
    id=self.d(resourceId="com.xiaoma.club:id/tv_group_id").info['text'][:2]
    if title_tv=='附近的群' and id =='群号' and label_name in label:
        return True
    else:
        return False

#搜索模块
def search_vague(self):
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/layout_search").click()
    self.d(resourceId="com.xiaoma.club:id/et_search_content").send_keys('8888')
    self.d(resourceId="com.xiaoma.club:id/btn_search").click()
    res = self.d(className="android.widget.LinearLayout", instance=13).exists(timeout=5.0)
    if res==True:
        return True
    else:
        return False

def search_group_id(self):
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/layout_nearby_group").click()
    id = self.d(resourceId="com.xiaoma.club:id/tv_group_id").info['text'][3:]
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/layout_search").click()
    self.d(resourceId="com.xiaoma.club:id/et_search_content").send_keys(id)
    self.d(resourceId="com.xiaoma.club:id/btn_search").click()
    id2 = self.d(resourceId="com.xiaoma.club:id/tv_group_id").info['text'][3:]
    if id==id2:
        return True
    else:
        return False
def search_null(self):
    self.d(resourceId="com.xiaoma.club:id/ivClearText").click()
    self.d(resourceId="com.xiaoma.club:id/btn_search").click()
    text_empty = self.d(resourceId="com.xiaoma.club:id/tv_text_empty").info['text']
    if text_empty=='搜索内容不能为空':
        return True
    else:
        return False
def search_null_result(self):
    self.d(resourceId="com.xiaoma.club:id/et_search_content").send_keys(u'一二三四')
    self.d(resourceId="com.xiaoma.club:id/btn_search").click()
    data_view = self.d(resourceId="com.xiaoma.club:id/empty_data_view").info['text']
    if data_view=='无搜索结果':
        return True
    else:
        return False
def search_str_result(self):
    self.d(resourceId="com.xiaoma.club:id/ivClearText").click()
    self.d(resourceId="com.xiaoma.club:id/et_search_content").send_keys(u'!@#qweQWE一二三')
    self.d(resourceId="com.xiaoma.club:id/btn_search").click()
    data_view = self.d(resourceId="com.xiaoma.club:id/empty_data_view").info['text']
    if data_view=='无搜索结果':
        return True
    else:
        return False
def short_input_search(self):
    self.d(resourceId="com.xiaoma.club:id/ivClearText").click()
    self.d(resourceId="com.xiaoma.club:id/et_search_content").send_keys('12一')
    self.d(resourceId="com.xiaoma.club:id/btn_search").click()
    text=self.d(resourceId="com.xiaoma.club:id/tv_text_num").info['text']
    if text=='输入内容过短':
        return True
    else:
        return False
def long_input_search(self):
    self.d(resourceId="com.xiaoma.club:id/ivClearText").click()
    self.d(resourceId="com.xiaoma.club:id/et_search_content").send_keys('012345678912345')
    self.d(resourceId="com.xiaoma.club:id/btn_search").click()
    text=self.d(resourceId="com.xiaoma.club:id/et_search_content").info['text']
    self.d(resourceId="com.xiaoma.club:id/ivClearText").click()
    try:
        self.d(resourceId="com.xiaoma.club:id/et_search_content").send_keys('0123456789123456')
        self.d(resourceId="com.xiaoma.club:id/btn_search").click()
        text2 = self.d(resourceId="com.xiaoma.club:id/et_search_content").info['text']
        if text2 =='0123456789123456':
            return False
        else:
            pass
    except:
        if text == '012345678912345':
            return True
        else:
            return False


'''排行榜'''
def top_rule(self):
    self.d(resourceId="com.xiaoma.club:id/ll_tab_item_container", className="android.widget.RelativeLayout",instance=1).click()
    sleep(2)
    self.d(className="android.widget.ImageButton", instance=1).click()
    text = self.d(resourceId="com.xiaoma.club:id/number").info['text']
    text2 = self.d(resourceId="com.xiaoma.club:id/number", text=u"02").info['text']
    text3 = self.d(resourceId="com.xiaoma.club:id/number", text=u"03").info['text']
    text4 = self.d(resourceId="com.xiaoma.club:id/number", text=u"04").exists(timeout=5.0)
    self.d(scrollable=True).scroll(steps=60)
    text5 = self.d(resourceId="com.xiaoma.club:id/number", text=u"04").info['text']
    if text=='01' and text2=='02' and text3=='03' and text4==False and text5=='04':
        return True
    else:
        return False
def stop_start_app(self):
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/ll_tab_item_container").click()
    self.d.app_stop('com.xiaoma.club')
    self.d.app_start('com.xiaoma.club')
    sleep(3)
    text = self.d(resourceId="com.xiaoma.club:id/tv_top_rank_type").info['text']
    self.d(resourceId="com.xiaoma.club:id/ll_tab_item_container", className="android.widget.RelativeLayout",instance=2).click()
    self.d.app_stop('com.xiaoma.club')
    self.d.app_start('com.xiaoma.club')
    sleep(3)
    text2 = self.d(resourceId="com.xiaoma.club:id/tv_top_rank_type").info['text']
    self.d(resourceId="com.xiaoma.club:id/ll_tab_item_container", className="android.widget.RelativeLayout",instance=3).click()
    self.d.app_stop('com.xiaoma.club')
    self.d.app_start('com.xiaoma.club')
    sleep(3)
    text3 = self.d(resourceId="com.xiaoma.club:id/tv_top_rank_type").info['text']
    if text==text2==text3:
        return True
    else:
        return False
def stop_start_app_default(self):
    text = self.d(resourceId="com.xiaoma.club:id/tv_top_rank_type").info['text']
    self.d(resourceId="com.xiaoma.club:id/rl_choose_rank_type").child(className='android.widget.ImageView').click()
    sleep(3)
    self.d(className="android.widget.RelativeLayout", instance=1).child(resourceId='com.xiaoma.club:id/tv_rank_type').click()
    sleep(3)
    self.d.app_stop('com.xiaoma.club')
    self.d.app_start('com.xiaoma.club')
    sleep(3)
    text2 = self.d(resourceId="com.xiaoma.club:id/tv_top_rank_type").info['text']
    sleep(3)
    self.d(resourceId="com.xiaoma.club:id/rl_choose_rank_type").child(className='android.widget.ImageView').click()
    sleep(3)
    self.d(className="android.widget.RelativeLayout", instance=2).child(resourceId='com.xiaoma.club:id/tv_rank_type').click()
    sleep(3)
    self.d.app_stop('com.xiaoma.club')
    self.d.app_start('com.xiaoma.club')
    sleep(3)
    text4 = self.d(resourceId="com.xiaoma.club:id/tv_top_rank_type").info['text']
    if text==text2==text4:
        return True
    else:
        return False
def top_jump(self):
    self.d(resourceId="com.xiaoma.club:id/iv_user_icon").click()
    sleep(4)
    text1 = self.d(resourceId="com.xiaoma.club:id/message").info['text']
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/tv_user_name").click()
    sleep(4)
    text2 = self.d(resourceId="com.xiaoma.club:id/message").info['text']
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/iv_user_label").click()
    sleep(4)
    text3 = self.d(resourceId="com.xiaoma.club:id/message").info['text']
    self.d.press('back')
    self.d(className="android.widget.LinearLayout", instance=8).click()
    sleep(4)
    text4 = self.d(resourceId="com.xiaoma.club:id/message").info['text']
    self.d.press('back')
    if text1==text2==text3==text4=='积分详情':
        return True
    else:
        return False
def top_show(self):
    decide = self.d(className="android.widget.RelativeLayout", instance=10).child(resourceId='com.xiaoma.club:id/ll_user_head').exists(timeout=5.0)
    decide2 = self.d(className="android.widget.RelativeLayout", instance=10).child(resourceId='com.xiaoma.club:id/tv_user_name').exists(timeout=5.0)
    decide3 = self.d(className="android.widget.RelativeLayout", instance=10).child(resourceId='com.xiaoma.club:id/iv_label').exists(timeout=5.0)
    decide4 = self.d(className="android.widget.RelativeLayout", instance=10).child(resourceId='com.xiaoma.club:id/tv_data').exists(timeout=5.0)
    decide5 = self.d(className="android.widget.RelativeLayout", instance=10).child(resourceId='com.xiaoma.club:id/iv_thumbs_up').exists(timeout=5.0)
    if decide==decide2==decide3==decide4==decide5==True:
        return True
    else:
        return False
def click_other_name(self):
    sleep(5)
    self.d(className="android.widget.RelativeLayout", instance=10).child(resourceId='com.xiaoma.club:id/tv_user_name').click()
    sleep(4)
    text = self.d(resourceId="com.xiaoma.club:id/message").info['text']
    self.d.press('back')
    if text=='积分详情':
        return True
    else:
        return False
def again_click_good(self):
    sleep(5)
    self.d(resourceId="com.xiaoma.club:id/iv_thumbs_up", className="android.widget.ImageView", instance=1).click()
    sleep(3)
    self.d(resourceId="com.xiaoma.club:id/iv_thumbs_up", className="android.widget.ImageView", instance=1).click()
    toast = self.d.toast.get_message(5.0, 10.0, "default message")
    if toast=='已经点过赞了哦':
        return True
    else:
        return False
def list_details(self):
    user_name = self.d(resourceId="com.xiaoma.club:id/tv_user_name").info['text']
    thumbs_number =  self.d(resourceId="com.xiaoma.club:id/tv_thumbs_number").info['text']
    self.d(resourceId="com.xiaoma.club:id/tv_user_name").click()
    sleep(4)
    rank_name = self.d(resourceId="com.xiaoma.club:id/rank_name").info['text']
    like_count = self.d(resourceId="com.xiaoma.club:id/like_count").info['text']
    if user_name==rank_name and thumbs_number==like_count:
        return True
    else:
        return False
def like_for_own(self):
    self.d(resourceId="com.xiaoma.club:id/layout_thumbs").click()
    toast = self.d.toast.get_message(5.0, 10.0, "default message")
    if toast=='不能对自己点赞哦':
        return True
    else:
        return False
def score_rank_show(self):
    rank_value = self.d(resourceId="com.xiaoma.club:id/tv_rank_value").info['text']
    sleep(3)
    rank_value2 = self.d(className="android.widget.LinearLayout", instance=13).child(resourceId='com.xiaoma.club:id/tv_rank_value').info['text']
    self.d.press('back')
    rank_value3 = self.d(resourceId="com.xiaoma.club:id/tv_rank_value").info['text']
    rank_value4 = self.d(className="android.widget.LinearLayout", instance=12).child(resourceId='com.xiaoma.club:id/tv_rank_value').info['text']
    if rank_value==rank_value3 and rank_value2==rank_value4:
        return True
    else:
        return False
def delete_talk(self):
    self.d(resourceId="com.xiaoma.club:id/ll_tab_item_container", className="android.widget.RelativeLayout",instance=2).click()
    self.d(resourceId="com.xiaoma.club:id/ll_tab_item_container").click()
    self.d(resourceId="com.xiaoma.club:id/layout_nearby_group").click()
    self.d(className="android.widget.LinearLayout", instance=6).click()
    self.d(resourceId="com.xiaoma.club:id/dialog_left_button").click()
    sleep(3)
    self.d.press('back')
    sleep(1)
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/ll_tab_item_container").click()
    self.d(resourceId="com.xiaoma.club:id/layout_nearby_group").click()
    self.d(className="android.widget.LinearLayout", instance=6).click()
    self.d(resourceId="com.xiaoma.club:id/dialog_left_button").click()
    sleep(3)
    self.d.press('back')
    sleep(1)
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/ll_tab_item_container", className="android.widget.RelativeLayout", instance=2).click()
    sleep(3)
    self.d(resourceId="com.xiaoma.club:id/item_list_head_bg").long_click(2)
    delete = self.d(resourceId="com.xiaoma.club:id/tvDel").exists(timeout=5.0)
    self.d(resourceId="com.xiaoma.club:id/item_list_head_bg").click()
    sleep(3)
    delete2 = self.d(resourceId="com.xiaoma.club:id/tvDel").exists(timeout=5.0)
    self.d(resourceId="com.xiaoma.club:id/group_head_view").click()
    self.d(className="android.widget.ImageButton", instance=1).click()
    self.d(scrollable=True).scroll(steps=60)
    text = self.d(resourceId="com.xiaoma.club:id/siv_group_id").child(className="android.widget.LinearLayout").child(resourceId='com.xiaoma.club:id/tv_item_info').info['text']
    self.d.press('back')
    sleep(1)
    self.d.press('back')
    self.d(resourceId="com.xiaoma.club:id/item_list_head_bg").long_click(2)
    sleep(3)
    self.d(resourceId="com.xiaoma.club:id/tvDel").click()
    sleep(3)
    self.d(resourceId="com.xiaoma.club:id/group_head_view").click()
    self.d(className="android.widget.ImageButton", instance=1).click()
    self.d(scrollable=True).scroll(steps=60)
    text2 = self.d(resourceId="com.xiaoma.club:id/siv_group_id").child(className="android.widget.LinearLayout").child(resourceId='com.xiaoma.club:id/tv_item_info').info['text']
    self.d.press('back')
    sleep(1)
    self.d.press('back')
    if delete==True and delete2==False and text!=text2:
        return True
    else:
        return False
def create_group_show(self):
    self.d(resourceId="com.xiaoma.club:id/btn_group_chat").click()
    text = self.d(resourceId="com.xiaoma.club:id/message").info['text']
    if text=='创建群':
        return True
    else:
        return False
def create_group_str(self):
    self.d(resourceId="com.xiaoma.club:id/et_search").send_keys('123!@#$qwZ一')
    text2 = self.d(resourceId="com.xiaoma.club:id/lv_contacts").child(className='android.widget.TextView').info['text']
    if text2=='没有更多数据了':
        return True
    else:
        return False
def create_group_null(self):
    self.d(resourceId="com.xiaoma.club:id/ivClearText").click()
    self.d(resourceId="com.xiaoma.club:id/btn_right").click()
    toast = self.d.toast.get_message(5.0, 10.0, "default message")
    if toast=='成员列表不能为空':
        return True
    else:
        return False
def null_more_message(self):
    self.d.press('back')
    # self.d(resourceId="com.xiaoma.club:id/ll_tab_item_container", className="android.widget.RelativeLayout", instance=2).click()
    self.d(resourceId="com.xiaoma.club:id/item_list_head_bg").click()
    sleep(3)
    self.d(resourceId="com.xiaoma.club:id/common_content_layout").swipe("down", steps=10)
    self.d(resourceId="com.xiaoma.club:id/common_content_layout").swipe("down", steps=10)
    toast = self.d.toast.get_message(5.0, 10.0, "default message")
    if toast=='没有更多消息了。':
        return True
    else:
        return False


