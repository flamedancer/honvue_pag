#-*- coding: utf-8 -*- 

"""
GAMES list => dict
    解释
        'index' int  序号
        'bigpicture' str  首页轮换图
        'smpicture'  str 首页产品展示图
        'name'       str 游戏名 
        'showpictures' list => str 详情展示图
        'small_desc' str 首页展示描述
        'main_desc'  str 详情主要描述
        'feature_desc' str 详情特色描述
        'download_tags' list => str [首页下载图 详情下载图  下载名 下载地址]  列表为空时显示"敬请期待"
        'type_tags' list => str 产品展示也游戏类型标签
   例如：
        'bigpicture': "/static/images/bannerTD.png",
        'smpicture': "/static/images/smallTD.png",
        'name': u'泰迪爱消除',
        'showpictures': ["/static/images/smallTD.png","/static/images/smallTD.png","/static/images/smallTD.png"],
        'small_desc': u"休闲三消,6月9日，与电影同步上线!",
        'main_desc': "我是游戏简介111111111",
        'feature_desc': "我是游戏特色11111111",
        'download_tags': [ ["/static/images/apple.png", "/static/images/apple1.png", "IOS", ""], ["/static/images/android.png", "/static/images/android1.png", u"安卓", ""]],
        'type_tags': [u'休闲', u'三消'],
"""

GAMES = [
    {
        'index': 0,
        'bigpicture': "/static/images/bannerTD.png",
        'smpicture': "/static/images/smallTD.png",
        'name': u'泰迪爱消除',
        'showpictures': ["/static/images/smallTD.png","/static/images/smallTD.png","/static/images/smallTD.png"],
        'small_desc': u"休闲三消,6月9日，与电影同步上线!",
        'main_desc': "我是游戏简介111111111",
        'feature_desc': "我是游戏特色11111111",
        'download_tags': [ ["/static/images/apple.png", "/static/images/apple1.png", "IOS", ""], ["/static/images/android.png", "/static/images/android1.png", u"安卓", ""]],
        'type_tags': [u'休闲', u'三消'],
    },
    {
        'index': 1,
        'bigpicture': "/static/images/bannerGems.png",
        'smpicture': "/static/images/smallGems.png",
        'name': u'水晶传说',
        'showpictures': ["/static/images/smallGems.png", "/static/images/smallGems.png", "/static/images/smallGems.png"],
        'small_desc': u"竞技策略类游戏,火热删档封测中",
        'main_desc': "我是游戏简介222222222",
        'feature_desc': "我是游戏特色22222222",
        'download_tags': [ ["/static/images/apple.png", "/static/images/apple1.png", "IOS", ""], ["/static/images/android.png", "/static/images/android1.png", u"安卓", ""]],
        'type_tags': [u'竞技', u'三消除'],
    },
    {
        'index': 2,
        'bigpicture': "/static/images/bannerHSSJ.png",
        'smpicture': "/static/images/smallHSSJ.png",
        'name': u'幻世神姬',
        'showpictures': [],
        'small_desc': u"二次元手游,策略类玩法",
        'main_desc': "我是游戏简介33333333",
        'feature_desc': "我是游戏特色333333333",
        'download_tags': [],
        'type_tags': [u'二次元'],
    },
    {
        'index': 3,
        'bigpicture': "/static/images/bannerHSSJ.png",
        'smpicture': "/static/images/smallHSSJ.png",
        'name': u'幻世神姬',
        'showpictures': [],
        'small_desc': u"二次元手游,策略类玩法",
        'main_desc': "我是游戏简介33333333",
        'feature_desc': "我是游戏特色333333333",
        'download_tags': [],
        'type_tags': [u'二次元'],
    },
]


NEWS = [
    {
        'index': 0,
        'title': u"标题标题标题标题标题标题标题标",
        'picture': "/static/images/smallHSSJ.png",
        'desc': u"1态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150>    字。动态简介，限150字。",  
        'time': u"2016年5月11日",
    },
   {
        'index': 1,
        'title': u"标题标题标题标题标题标题标题标",
        'picture': "/static/images/smallGems.png",
        'desc': u"2态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150>    字。动态简介，限150字。",  
        'time': u"2016年5月11日",
    },
   {
        'index': 2,
        'title': u"标题标题标题标题标题标题标题标",
        'picture': u"/static/images/smallTD.png",
        'desc': u"3态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150>    字。动态简介，限150字。",  
        'time': u"2016年5月11日",
    },
]


JOBS = [
   {
       'category': u"策划类", 
       'info': [
           {
               'name': u"系统策划",     
               'desc': u'''
岗位职责：
1、根据主策要求，完成策划相关设计工作；
2、与程序美术协同工作，保证开发结果符合设计要求；
3、熟悉Excel表格，完成Excel配置；
4、利用CocoStudio编辑器完成界面设计；
5、协助完成测试工作


任职要求：
1、做事认真，责任心强；
2、热爱游戏制作，熟悉各类游戏，思维活跃，创意丰富；
3、对游戏设计和剧情编写很有热情；
4、具有一定的文学知识理论基础；
5、能够熟练使用Axure、CocoStudio等工具；
6、拥有手游成功上线项目者优先系统策划",     
''',
            },
            {
                'name': u"数值策划",     
                'desc': u'''
岗位职责：

1、根据主策要求，完成策划相关设计工作；

2、与程序美术协同工作，保证开发结果符合设计要求；

3、熟悉Excel表格，完成Excel配置；

4、利用CocoStudio编辑器完成界面设计；

5、协助完成测试工作



任职要求：

1、做事认真，责任心强；

2、热爱游戏制作，熟悉各类游戏，思维活跃，创意丰富；

3、对游戏设计和剧情编写很有热情；

4、具有一定的文学知识理论基础；

5、能够熟练使用Axure、CocoStudio等工具；

6、拥有手游成功上线项目者优先
''',
            },
            {
                'name': u"cocos2dx程序",     
                'desc': u'''  ''',
            },
            {
                'name': u"cocos2dx程序",     
                'desc': u'''  ''',
            },
            {
                'name': u"cocos2dx程序程序程序程序程序",     
                'desc': u'''  ''',
            },
            {
                'name': u"cocos2dx程序程序程序程序程序",     
                'desc': u'''  ''',
            },
        ],
    },


    {
        'category': u"美术类", 
        'info': [
            {
                'name': u"场景原画师",     
                'desc': u'''  ''',
            },
            {
                'name': u"特效师",     
                'desc': u'''  ''',
            },
        ]
    },



    {
        'category': u"技术类", 
        'info': [
            {
                'name': u"cocos2dx程序",     
                'desc': u'''  ''',
            },
        ]
    },





]

