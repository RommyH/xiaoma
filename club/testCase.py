from  unittest import  TestCase
from time import sleep
from club.control import connect_device,timeout_time,start_club,stop_club,club_top,click_find,find_page_text,nearby_car_home,car_rank,oneRow_twoCar,click_car_info,send_message
from club.control import temporary_session,filtrate,filtrate_result,group_filtrate_result,filtrate_cache_true,filtrate_cache_false,group_rank,one_group,group_info,add_group,group_detail_info
from club.control import group_jump,back_group,back_group_list,click_group_back,cancel_add_group,null_group_label,max_group_label,delete_group_label,label_filtrate_correct,clear_label
from club.control import two_label,null_search,delete_label_search,search_vague,search_group_id,search_null,search_null_result,search_str_result,short_input_search,long_input_search
from club.control import top_rule,stop_start_app,stop_start_app_default,top_jump,top_show,click_other_name,again_click_good,list_details,like_for_own,score_rank_show,delete_talk
from club.control import create_group_show,create_group_str,create_group_null,null_more_message

class xiaoma_club(TestCase):
    def setUp(self):
        connect_device(self)
        timeout_time(self)

    def testcase001_starClub(self):   #正常打开想聊
        start_club(self)
        assert club_top(self)

    def testcase002_find_page(self):    #发现页面
        click_find(self)
        assert find_page_text(self)

    def testcase003_nearby_car_home(self):  #附近的车页面
        assert nearby_car_home(self)

    def testcase004_car_rank(self): #附近的车 距离倒序排序
        assert car_rank(self)

    def testcase005_oneRow_twoCar(self):   #一行显示两个车主
        assert oneRow_twoCar(self)

    def testcase006_click_car_info(self):  #附近的车 点击头像
        assert click_car_info(self)

    def testcase007_send_message(self):  #发送好友请求
        assert send_message(self)

    def testcase008_temporary_session(self):  #附近的车，临时会话
        assert temporary_session(self)

    def testcase009_filtrate(self): #筛选项
        assert filtrate(self)

    def testcase010_filtrate_result(self): #筛选18-35 有结果
        assert filtrate_result(self)

    def testcase011_group_filtrate_result(self): #多条件筛选 女 18-35 3天
        assert group_filtrate_result(self)

    def testcase012_filtrate_cache_true(self):  #选择筛选条件后点击取消，再次点击筛选，筛选条件不清空
        assert filtrate_cache_true(self)

    def testcase013_filtrate_cache_false(self): #选择筛选条件后退出附近的车，再进入附近的车查看筛选条件清空
        assert filtrate_cache_false(self)

    def testcase014_group_rank(self): #附近的群 按距离倒序排序
        assert group_rank(self)

    def testcase015_one_group(self): #一行显示一个群
        assert one_group(self)

    def testcase016_group_info(self): #群列表信息展示
        assert group_info(self)

    def testcase017_add_group(self): #退出一个附近的群后，附近的群列表新增该群
        assert add_group(self)

    def testcase018_group_detail_info(self):   #点击群查看信息
        assert group_detail_info(self)

    def testcase019_group_jump(self):  #加入该群，并跳转到群聊页面
        assert group_jump(self)

    def testcase020_back_group(self): #返回到发现主页，再进入附近的群，列表页不显示该群
        assert back_group(self)

    def testcase021_back_group_list(self):  #入群后点击返回 列表仍然显示该群
        assert back_group_list(self)

    def testcase022_click_group_back(self):  #入群后点击返回 列表仍然显示该群 点击该群跳转到群聊页面
        assert click_group_back(self)

    def testcase023_cancel_add_group(self):  #点击取消 回到附近的群列表页
        assert cancel_add_group(self)

    def testcase024_null_group_label(self): #空标签筛选
        assert null_group_label(self)

    def testcase025_max_group_label(self):  #可以选择多个标签，选择一个标签，顶部会显示已选择的标签，最多可选择5个标签
        assert max_group_label(self)

    def testcase026_delete_group_label(self):   #已选择标签删除成功
        assert delete_group_label(self)

    def testcase027_label_filtrate_correct(self): #筛选数据正确
        assert label_filtrate_correct(self)

    def testcase028_clear_label(self):  #单标签筛选后删除标签  回到列表页
        assert clear_label(self)

    def testcase029_two_label(self): #多标签筛选 筛选数据正确
        assert two_label(self)

    def testcase030_null_search(self): #筛选结果为空 提示没有搜索到符合条件的群
        assert null_search

    def testcase031_delete_label_search(self): #多标签筛选后删除标签 删除标签后刷新筛选数据，数据正确 删除所有标签后回到列表页
        assert delete_label_search(self)

    def testcase032_search_vague(self):  #支持车牌号模糊搜索 搜索8888有结果
        assert search_vague(self)

    def testcase033_search_group_id(self): #群号需精确搜索
        assert search_group_id(self)

    def testcase034_search_null(self): #输入空点击搜索 提示搜索内容不能为空
        assert search_null(self)

    def testcase035_search_null_result(self): #搜索结果为空 提示无搜索结果
        assert search_null_result(self)

    def testcase036_search_str_result(self):  #输入数字大小写字母特殊字符中文都可以搜索
        assert search_str_result(self)

    def testcase037_short_input_search(self): #输入低于4个字符，注意：中文也算1个字符长度 提示：输入内容过短，
        assert short_input_search(self)

    def testcase038_long_input_search(self): # 输入15个字符后继续输入，注意：中文也算1个字符长度 无法再输入
        assert long_input_search(self)

 #排行榜

    def testcase039_top_rule(self):   #一页显示三条规则，超过三条可以滑动查看
        assert top_rule(self)

    def testcase040_stop_start_app(self): #点击发现/会话/通讯录,退出想聊，重新打开想聊 显示排行榜列表页
        assert stop_start_app(self)

    def testcase041_stop_start_app_default(self): #切换排行榜榜单，退出想聊，重新打开想聊 显示默认的排行榜榜单-全国积分排行榜
        assert stop_start_app_default(self)

    def testcase042_top_jump(self):   #点击左上角个人头像、用户名、标签、获赞次数 跳转到积分详情页面
        assert top_jump(self)

    def testcase043_top_show(self):  #积分排行榜显示用户排名、用户名、标签、积分、赞按钮
        assert top_show(self)

    def testcase044_click_other_name(self):  #点击他人用户名 跳转到该用户的积分详情页面
        assert click_other_name(self)

    def testcase045_again_click_good(self):  #点赞后再次点击赞按钮 无法取消赞，弹出提示：已经点过赞了哦
        assert again_click_good(self)

    def testcase046_list_details(self):  #用户名、获赞次数检查   数据正确，与列表页显示一致
        assert list_details(self)

    def testcase047_like_for_own(self): #为自己点赞检查 弹出提示：不能对自己点赞哦
        assert like_for_own(self)

    def testcase048_score_rank_show(self): #全国排名、个人今日积分 数据正确，与列表页一致
        assert score_rank_show(self)

#会话
    def testcase049_delete_talk(self): #长按会话 出现删除会话按钮，单击会话退出删除，单击删除按钮删除会话
        assert delete_talk(self)

    def testcase050_create_group_show(self):  #点击列表页右上方发起群聊按钮 进入创建群页面
        assert create_group_show(self)

    def testcase051_create_group_str(self): #搜索条件 支持语音、汉字、全拼、英文字母、特殊字符（区分中英文符号）模糊搜索 搜索不存在的好友 提示没有更多数据
        assert create_group_str(self)

    def testcase052_create_group_null(self): #不选择好友直接点击确定 弹出提示成员列表不能为空
        assert create_group_null(self)

    def testcase053_null_more_message(self):  #滑动到最顶部提示没有更多消息
        assert null_more_message(self)

    # def tearDown(self):
        # stop_club(self)