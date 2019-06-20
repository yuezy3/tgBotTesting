import pandas as pd
import random
from jtyoui.data import  WeatherForecast
from jtyoui.baidu import  BaiDuInfoSearch

adlist=['需要免费上广告的群主或者群友,请加本机器人为好友', '买优质雪茄和红酒加微信dc17502017830','优质海特产请加微信SL33002',\
        '大陆期货低手续费低保证金服务周到,开户咨询微信canghai397','拉本机器人进一个群,我在10个群展示你的广告,是时候告别单打独斗了',\
        '主营中厚板  普阳文丰 一级代理商  专业接定扎  交货期快  嘉祥友盛商贸有限公司   18953778997闫永刚  24小时为您服务',\
        '招保险兼职打卡专员，30元一次 要求：高中以上学历，居住/工作在天河客运站附近年龄22-50岁。早上/下午各打一次卡，30元/次,福利1：录取成功奖励精美礼品 福利2：自己与家人买重疾保险1折-3折 兼职地址：地铁天河客运站D出口1分钟，新天地旁天汇创意园C2栋207 \
        联系人：陈经理18826415319','趣投趣投代理招募 实力对接更大网红，主播，微商游戏商人及酒吧营销，网吧网管 微信好友多一天 天收入4位数以上 加微信xiaozhaotongzhi6458','全国模特信息即将上线,敬请期待...',\
        '福音app=抖音+趣步 锁粉50,一条线排下去.2扫1,3扫2......50扫49.最后合力一起推广第50人的二维码.迅速扩大团队活跃度.0撸免费,认证费我出,争取做到50人都早早上达人拿奖励分红,加微信O7135246']
templateStr='您所咨询的{key}信息' + '\r\n' + '{result}' + ' \r\n-----------------------------------------------\r\n 为了永久提供免费服务,我们不得不植入广告,请谅解\r\n-----------------------------------------------\r\n{ad}'
df = pd.read_excel('mx.xls')
df_dq = df['地区']
dj = pd.read_excel('xgh.xlsx')     #信息表
dj_dq = dj['地址']
dm = pd.read_excel('mt.xlsx')

def wrapResult(f):
    def inner(*args, **kwargs):
        r = f(*args, **kwargs)
        return templateStr.format(**r)
    return inner
def f1(s):
    tianqi = WeatherForecast()
    tianqi.set_city(s)
    ad = adlist[random.randint(0, len(adlist) - 1)]
    r = {'key':"天气",'result':str(tianqi.get_7day_weather()),'ad':adlist[random.randint(0, len(adlist) - 1)]}
    return r
def f2(s):
    bd = BaiDuInfoSearch(s)
    baike = bd.info()
    r = {'key':"百科",'result':str(baike),'ad':adlist[random.randint(0, len(adlist) - 1)]}
    return r
def f3(s):
    lis_1 = [i for i, data in enumerate(list(df_dq.apply(lambda x: x if s in x else ''))) if data != '']
    lis_2 = random.choice(lis_1)
    r = {'key':"城市伴游",'result':str(df.iloc[lis_2]),'ad':adlist[random.randint(0, len(adlist) - 1)]}
    return r
def f4(s):
    lis_3 = [i for i, data in enumerate(list(dj_dq.apply(lambda x: x if s in x else ''))) if data != '']
    lis_4 = random.choice(lis_3)
    r = {'key':"校花城市",'result':str(dj.iloc[lis_4]),'ad':adlist[random.randint(0, len(adlist) - 1)]}
    return r
def f5(s):
    str_mt = '随机发送五条模特信息（80%联系方式有效）\r\n'+'模特昵称:' + '\t' + '微信QQ号' + '\r\n'
    for i in random.sample(range(0, len(dm) - 1), 5):
        str_mt += str(dm['模特昵称'].iloc[i]) + '\t' + str(dm['微信QQ号'].iloc[i]) + '\r\n'
    r = {'key':"模特",'result':str_mt,'ad':adlist[random.randint(0, len(adlist) - 1)]}
    return r
exportKey = {"天气":wrapResult(f1) , "百科":wrapResult(f2), "伴游":wrapResult(f3), "校花":wrapResult(f4), "模特":wrapResult(f5)}



