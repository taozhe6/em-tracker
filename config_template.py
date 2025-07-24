# config_template.py
import os

# ==============================================================================
# 模块 1: 账户配置
# ==============================================================================
# 请在这里填入您的账户信息
# 您可以添加多个账户，程序运行时会提供选择

ACCOUNTS = [
    # 示例账户配置 - 请复制并修改以下模板
    {
        'journal_short_name': 'GASTRO',           # 期刊简称，用于显示
        'journal_full_name': 'Gastroenterology',  # 期刊全名
        'username': 'your_username_here',         # 替换为您的用户名
        'password': 'your_password_here'          # 替换为您的密码
    },
    {
        'journal_short_name': 'GUT',
        'journal_full_name': 'Gut',
        'username': 'your_username_here',
        'password': 'your_password_here'
    },
    # 添加更多账户...
    # {
    #     'journal_short_name': 'IBD',
    #     'journal_full_name': 'Inflammatory Bowel Diseases',
    #     'username': 'your_username_here',
    #     'password': 'your_password_here'
    # },
]

# ==============================================================================
# 模块 2: 网络请求常量
# ==============================================================================
BASE_URL = "https://www.editorialmanager.com"
LOGIN_SUCCESS_FLAG = "Default.aspx?pg=AuthorMainMenu.aspx"
DEFAULT_RETRY_COUNT = 3
RETRY_DELAY_SECONDS = 5
DEFAULT_TIMEOUT = 20

# ==============================================================================
# 模块 3: 模拟浏览器头
# ==============================================================================
BROWSER_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
}
