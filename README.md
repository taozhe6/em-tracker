# em-tracker
🔬 **Editorial Manager 期刊稿件状态追踪工具**

专为使用 Editorial Manager 系统的学术期刊设计的稿件状态自动追踪工具。

## ✨ 功能特点

- 🏥 **Editorial Manager专用**: 专门适配EM系统的期刊网站
- 📊 **Excel记录**: 自动生成格式化的历史追踪表格  
- 🎨 **彩色界面**: 友好的命令行交互体验
- 🔄 **智能重试**: 网络异常时自动重试机制
- 📁 **数据管理**: 按用户和稿件自动组织本地数据
- 🔒 **隐私保护**: 支持临时账户查询，无需保存敏感信息
- 📱 **状态变更追踪**: 自动检测并记录稿件状态变化

## 🎯 支持的期刊系统

本工具专门为 **Editorial Manager (EM)** 系统设计，支持大多数使用EM系统的医学期刊，包括但不限于：

- Gastroenterology 
- The Lancet系列期刊
- American Journal of Gastroenterology
- Inflammatory Bowel Diseases
- 其他使用EM系统的期刊

## 🚀 快速开始

### 1. Python环境准备

#### 选项A：使用虚拟环境（推荐）

```bash
# 创建新的Python环境
python -m venv journal-tracker-env

# 激活环境
# Windows:
journal-tracker-env\Scripts\activate
# macOS/Linux:
source journal-tracker-env/bin/activate

# 升级pip
python -m pip install --upgrade pip
```

#### 选项B：使用Conda（如果你有Anaconda）

```bash
# 创建新环境
conda create -n journal-tracker python=3.9
conda activate journal-tracker
```

### 2. 获取代码

```bash
# 克隆或下载项目
git clone https://github.com/yourusername/journal-manuscript-tracker.git
cd journal-manuscript-tracker

# 或者直接下载ZIP文件并解压
```

### 3. 安装依赖

```bash
# 安装所需库
pip install -r requirements.txt
```

### 4. 配置设置

```bash
# 运行配置助手
python add_config.py
```

按提示输入您的期刊账户信息：
- 期刊全名（如：Gastroenterology）
- 期刊简称（如：GASTRO，通常在EM网址中能看到）
- 用户名和密码

### 5. 开始使用

```bash
python main.py
```

## 📖 使用指南

### 🎯 基本操作流程

1. **启动程序**: `python main.py`
2. **选择用户**: 从已配置的账户中选择
3. **选择期刊**: 如果用户有多个期刊账户，选择要查询的期刊
4. **等待查询**: 程序自动登录并获取稿件状态
5. **查看结果**: 
   - 命令行显示实时状态
   - Excel文件自动保存到本地

### 📁 数据组织结构

```
data/
├── username1/
│   ├── MS001_Your-Paper-Title/
│   │   └── Your-Paper-Title_投稿追踪.xlsx
│   ├── MS002_Another-Paper/
│   │   └── Another-Paper_投稿追踪.xlsx
│   └── ...
└── username2/
    └── ...
```

### 🔄 状态追踪逻辑

- **首次运行**: 创建Excel文件，记录当前状态
- **后续运行**: 
  - 状态无变化 → 显示"状态未变"
  - 状态有变化 → 新增记录行，显示变更详情

### 💡 临时查询功能

选择"手动输入临时账户"适用于：
- 🎯 偶尔查询其他期刊
- 🔒 不想保存账户信息  
- 📝 测试新的期刊配置

### 📊 Excel报告内容

每个稿件的Excel文件包含：
- `Timestamp`: 查询时间
- `SubmissionBeganDate`: 投稿开始日期
- `StatusDate`: 状态更新日期  
- `Status`: 当前状态
- `ManuscriptNumber`: 稿件编号
- `Title`: 稿件标题

## 🔧 配置说明

### config.py 结构

```python
# 基本配置
BASE_URL = "https://www.editorialmanager.com"
LOGIN_SUCCESS_FLAG = "Author Main Menu"
DEFAULT_RETRY_COUNT = 3
RETRY_DELAY_SECONDS = 2
DEFAULT_TIMEOUT = 30

# 账户配置
ACCOUNTS = [
    {
        'journal_full_name': 'Gastroenterology',
        'journal_short_name': 'GASTRO',  # EM网址中的简称
        'username': 'your_username',
        'password': 'your_password'
    },
    # 可以添加更多期刊账户
]

# 浏览器头信息
BROWSER_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
```

## 🚨 常见问题

### Q: 如何找到期刊的简称(journal_short_name)？
**A**: 查看EM期刊登录页面URL，如：
- `https://www.editorialmanager.com/gastro/` → 简称是 `GASTRO`
- `https://www.editorialmanager.com/ibd/` → 简称是 `IBD`

### Q: 登录失败怎么办？
**A**: 检查以下几点：
1. 用户名密码是否正确
2. 期刊简称是否正确
3. 网络连接是否稳定
4. 期刊网站是否正常

### Q: 为什么建议使用虚拟环境？
**A**: 虚拟环境的好处：
- 🔒 隔离项目依赖，避免版本冲突
- 🧹 保持系统Python环境干净
- 📦 便于项目迁移和分享
- 🛡️ 避免权限问题

### Q: Excel文件被占用怎么办？
**A**: 程序会自动检测文件占用并提示：
1. 关闭Excel文件
2. 按Enter继续
3. 程序会自动重试写入

## 🔒 隐私与安全

- ✅ 所有数据存储在本地
- ✅ 不上传任何个人信息
- ✅ 支持临时账户查询
- ✅ 配置文件不会被git跟踪
- ⚠️ 请妥善保管config.py文件

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

### 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/yourusername/journal-manuscript-tracker.git
cd journal-manuscript-tracker

# 创建开发环境
python -m venv dev-env
source dev-env/bin/activate  # Linux/macOS
# dev-env\Scripts\activate     # Windows

# 安装开发依赖
pip install -r requirements.txt
```

## 📜 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

感谢所有使用和改进这个工具的研究者们！

---

**⚡ 快速命令参考**

```bash
# 完整设置流程
python -m venv journal-tracker-env
source journal-tracker-env/bin/activate  # Linux/macOS
# journal-tracker-env\Scripts\activate   # Windows
pip install -r requirements.txt
python add_config.py
python main.py
```

如有问题，请提交Issue或联系维护者。

Happy Research! 🔬📊
