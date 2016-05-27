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
        'showpictures': ["/static/images/pic_xuanchuan1.png","/static/images/pic_xuanchuan2.png","/static/images/pic_xuanchuan5.png"],
        'small_desc': u"休闲三消,泰迪正版授权",
        'main_desc': u'''
    《泰迪爱消除》是由泰迪熊正版授权的一款三消类休闲游戏。游戏紧贴《泰迪熊之玩具大战》电影剧情，通过控制三个主角泰迪、小飞和罗巴，一起粉碎巫博士通过控制机甲玩具征服世界的阴谋，并以爽快流畅的消除手感，绚丽缤纷的消除效果，独创的微策略闯关玩法，趣味与挑战并存的关卡，突出主角特色的养成系统，加上清新诱人的美食风格以及泰迪熊电影原版音乐和配音，带给玩家高品质的动感消除体验。''',
        'feature_desc':u''' 
《泰迪熊》正版电影授权
    《泰迪爱消除》由电影《泰迪熊之玩具大战》官方正版授权，游戏剧情紧贴电影，并使用电影原版音乐和配音，完美还原泰迪熊和小伙伴之间的友情、热血和正义。
		
看的见的“美味”
    作为一款轻松休闲的三消游戏，本作采用了可爱的卡通风格画面，并将游戏中的各种基础珠和小孩子最喜欢的美味零食相结合，隔着屏幕都能闻到那美食的香甜气息。
	
创新消除玩法 角色养成系统 战斗系统
    游戏在传统的三消基础上，引入了角色养成玩法和战斗系统，让整个游戏过程更加丰富多彩。除了泰迪、玩家还可以培养如小飞或者罗巴，每个主角都有不同的属性加成以及技能效果，这让每一关都能有不同的通关方法，让玩家感受最完整的泰迪熊世界。''',
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
]


NEWS = [
    {
        'index': 0,
        'title': u"标题标题标题标题标题标题标题标",
        'picture': "/static/images/smallHSSJ.png",
        'content': u"1态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150>    字。动态简介，限150字。",  
        'time': u"2016年5月11日",
    },
   {
        'index': 1,
        'title': u"标题标题标题标题标题标题标题标",
        'picture': "/static/images/smallGems.png",
        'content': u"2态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150>    字。动态简介，限150字。2态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150>    字。动态简介，限150字。2态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150>    字。动态简介，限150字。2态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150>    字。动态简介，限150字。",  
        'time': u"2016年5月12日",
    },
   {
        'index': 2,
        'title': u"标题标题标题标题标题标题标题标",
        'picture': u"/static/images/smallTD.png",
        'content': u"3态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150>    字。动态简介，限150字。",  
        'time': u"2016年5月13日",
    },
   {
        'index': 3,
        'title': u"标题标题标题标题标题标题标题标",
        'picture': u"/static/images/smallTD.png",
        'content': u"4态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150>    字。动态简介，限150字。",  
        'time': u"2016年5月15日",
    },
   {
        'index': 4,
        'title': u"标题标题标题标题标题标题标题标",
        'picture': u"/static/images/smallTD.png",
        'content': u"5态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150字。动态简介，限150>    字。动态简介，限150字。",  
        'time': u"2016年5月16日",
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

